"""
Extracting features from sensor data for HAR, with multiple methods and flexible sensor selection.
"""
import numpy as np
import scipy.stats


class FeatureExtractor:
    """Extract and manage features for HAR."""

    METHODS = [
        'original',      # Method originally used in "Few-Shot Learning for Hand-Based Micro Activity Recognition" by Demrozi and Al Machot (2025)
        'temporal',           # Temporal features only
        'frequency',          # Frequency features only
        'temporal_frequency', # Combined temporal + frequency
    ]


    def extract_features(self, data, method, sensor_columns=None, window_seconds=4.0,
                         overlap_ratio=0.0, fs=100, strategy="retain_short", verbose=True):
        """
        Extract features from sensor data using specified method.
        """
        if method not in self.METHODS:
            raise ValueError(
                f"Unsupported method: {method}. "
                f"Supported methods: {self.METHODS}"
            )

        if sensor_columns is None:
            sensor_columns = [
                column for column in data.columns
                if column not in ['timestamp', 'adl', 'session', 'subject', 'fileID']
            ]
        else:
            missing_cols = set(sensor_columns) - set(data.columns)
            if missing_cols:
                raise ValueError(f"Sensor columns not found in data: {missing_cols}")

        if not (0.0 <= overlap_ratio < 1.0):
            raise ValueError("overlap_ratio must be in the range [0.0, 1.0).")

        window_size = int(window_seconds * fs)
        stride = max(1, int(window_size * (1 - overlap_ratio)))

        if verbose:
            print(f"\nExtracting features: {method}")
            print(f"  Window: {window_seconds}s")
            print(f"  Overlap: {overlap_ratio} ({stride} stride)")
            print(f"  Sampling rate: {fs} Hz")

            print("\nCreating windows per fileID...")
        windows, labels, fileIDs, subjects = self._create_windows_per_fileid(
            data, sensor_columns, window_size, stride, strategy, verbose=verbose
        )
        if verbose:
            print(f"  Created {len(windows)} windows")
            print(f"\nExtracting features using method: {method}...")
        features_array = self._extract_features_from_windows(windows, method, verbose=verbose)
        
        if verbose:
            print(f"  Feature shape: {features_array.shape}")

        return features_array, labels, fileIDs, subjects


    def _create_windows_per_fileid(self, data, sensor_columns, window_size, stride, strategy="retain_short", verbose=True):
        """Create windows respecting fileID boundaries."""
        windows, labels, fileIDs, subjects = [], [], [], []
        total_count = 0
        short_count = 0

        for (subj, sess, adl, fid), group in data.groupby(['subject', 'session', 'adl', 'fileID']):
            arr = group[sensor_columns].to_numpy()
            seq_len = len(arr)

            if seq_len < window_size:
                short_count += 1

                if strategy == "retain_short":
                    windows.append(arr.copy())
                    labels.append(adl)
                    fileIDs.append(fid)
                    subjects.append(subj)

                elif strategy == "padding":
                    padded = np.pad(
                        arr,
                        ((0, window_size - seq_len), (0, 0)),
                        mode='edge'
                    )
                    windows.append(padded)
                    labels.append(adl)
                    fileIDs.append(fid)
                    subjects.append(subj)

                elif strategy in (None, "drop_short"):
                    pass

                else:
                    raise ValueError(
                        "strategy must be one of: 'retain_short', 'padding', 'drop_short'"
                    )

            else:
                for start in range(0, seq_len - window_size + 1, stride):
                    window = arr[start:start + window_size]
                    windows.append(window.copy())
                    labels.append(adl)
                    fileIDs.append(fid)
                    subjects.append(subj)

            total_count += 1

        if verbose:
            print(f"  Found {short_count} files that are shorter than the window size ({short_count/total_count:0.2%} of the available files)")
        return windows, labels, fileIDs, subjects


    def _extract_features_from_windows(self, windows, method, verbose=True):
        """Extract features from all windows using specified method."""
        features = []

        for i, window_2d in enumerate(windows):
            if verbose:
                if i % 1000 == 0:
                    if i == 0:
                        print(f"  Processing window {i}/{len(windows)}")
                    else:
                        print(f"                    {i}/{len(windows)}")

            if method == 'original':
                feat = self._extract_original(window_2d)
            elif method == 'temporal':
                feat = self._extract_temporal(window_2d)
            elif method == 'frequency':
                feat = self._extract_frequency(window_2d)
            elif method == 'temporal_frequency':
                temporal = self._extract_temporal(window_2d)
                frequency = self._extract_frequency(window_2d)
                feat = np.concatenate([temporal, frequency])
            else:
                raise ValueError(f"Unknown method: {method}")

            features.append(feat)

        return np.array(features)


    def _extract_original(self, data):
        """
        Feature extraction following the method used in "Few-Shot Learning for Hand-Based Micro Activity Recognition" by Demrozi and Al Machot (2025).
        For each sensor channel, computes mean, standard deviation, minimum, maximum, median, variance, range, IQR, RMS, mean absolute value, 
        and mean absolute successive difference. The same statistics are also computed for the first-order difference of the signal.
        """
        def calc_stats(x):
            return np.concatenate([
                np.mean(x, axis=0),
                np.std(x, axis=0),
                np.min(x, axis=0),
                np.max(x, axis=0),
                np.median(x, axis=0),
                np.var(x, axis=0),
                np.ptp(x, axis=0),
                scipy.stats.iqr(x, axis=0),
                np.sqrt(np.mean(np.square(x), axis=0)),
                np.sum(np.abs(x), axis=0) / x.shape[0],
                np.mean(np.abs(np.diff(x, axis=0)), axis=0) if x.shape[0] > 1 else np.zeros(x.shape[1])
            ])

        features = [calc_stats(data)]

        if data.shape[0] > 1:
            features.append(calc_stats(np.diff(data, axis=0)))

        return np.concatenate(features)


    def _extract_temporal(self, data):
        """
        Extract temporal features only.
        Includes: mean, std, min, max, median, var, skew, kurtosis.
        """
        if data.size == 0 or data.shape[1] == 0:
            return np.zeros(8 * data.shape[1] if data.shape[1] > 0 else 8)

        return np.concatenate([
            np.nan_to_num(np.mean(data, axis=0)),
            np.nan_to_num(np.std(data, axis=0)),
            np.nan_to_num(np.min(data, axis=0)),
            np.nan_to_num(np.max(data, axis=0)),
            np.nan_to_num(np.median(data, axis=0)),
            np.nan_to_num(np.var(data, axis=0)),
            np.nan_to_num(scipy.stats.skew(data, axis=0, nan_policy='omit')),
            np.nan_to_num(scipy.stats.kurtosis(data, axis=0, nan_policy='omit'))
        ])


    def _extract_frequency(self, data):
        """
        Extract frequency domain features using FFT.
        Includes: mean, std, max, min of FFT magnitudes.
        """
        if data.size == 0 or data.shape[1] == 0:
            return np.zeros(4 * data.shape[1] if data.shape[1] > 0 else 4)

        fft_vals = np.fft.fft(data, axis=0)
        fft_mag = np.abs(fft_vals[:data.shape[0] // 2])

        return np.concatenate([
            np.nan_to_num(np.mean(fft_mag, axis=0)),
            np.nan_to_num(np.std(fft_mag, axis=0)),
            np.nan_to_num(np.max(fft_mag, axis=0)),
            np.nan_to_num(np.min(fft_mag, axis=0))
        ])