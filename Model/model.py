"""
Implementing the ZSL/GZSL Model.
"""

from pathlib import Path
import numpy as np
from sklearn.preprocessing import StandardScaler
from scipy.linalg import solve_sylvester
from scipy import spatial


class IP_SAE_MODEL:
    """
    The model uses the direct projection approach based on the Sylvester equation,
    heavily inspired by An Integral Projection-Based Semantic Autoencoder (IP-SAE) by Heyden et al. (2023).
    """
    def __init__(self, lambda_reg=0.001, scale_features=True):
        self.lambda_reg = lambda_reg
        self.scale_features = scale_features
        self.scaler = StandardScaler() if scale_features else None
        self.W = None
        self.seen_classes = None

    def fit(self, X_train, y_train, class_embeddings, verbose=0):
        if self.scale_features:
            if verbose:
                print("Scaling features with StandardScaler...")
            X_train_scaled = self.scaler.fit_transform(X_train)
        else:
            X_train_scaled = X_train

        self.seen_classes = sorted(np.unique(y_train))
        S = np.array([class_embeddings[label] for label in y_train])

        if verbose:
            s_norms = np.linalg.norm(S, axis=1)
            print(f"Semantic embedding norms: min={s_norms.min():.6f}, max={s_norms.max():.6f}")

        # Integral projection
        X_aug = np.concatenate([X_train_scaled, S], axis=1)

        if verbose:
            print("Computing projection matrix W using Sylvester equation...")
            print(f" Input feature dim: {X_train_scaled.shape[1]}")
            print(f" Augmented feature dim: {X_aug.shape[1]}")
            print(f" Semantic dim: {S.shape[1]}")
            print(f" Regularization λ: {self.lambda_reg}")

        # SAE Sylvester setup
        A = S.T @ S                               # (emb_dim, emb_dim)
        B = self.lambda_reg * (X_aug.T @ X_aug)   # (feat_dim_aug, feat_dim_aug)
        C = (1 + self.lambda_reg) * (S.T @ X_aug) # (emb_dim, feat_dim_aug)

        self.W = solve_sylvester(A, B, C)   # W shape: (emb_dim, feat_dim_aug)

        if verbose:
            print(f" Projection matrix W computed: {self.W.shape}")
    
    def predict_zsl(self, X_test, unseen_class_embeddings, unseen_class_labels, n_runs=35, fixed_seed=True):
        """
        Predict unseen-class labels by averaging cosine similarities over repeated augmented inference runs.
        """
        if n_runs < 1:
            raise ValueError("n_runs must be at least 1.")
        if self.scale_features:
            X_test_scaled = self.scaler.transform(X_test)
        else:
            X_test_scaled = X_test

        S_projected = unseen_class_embeddings @ self.W

        avg_similarities = np.zeros((X_test_scaled.shape[0], len(unseen_class_labels)))
        run_predictions = []
        for run in range(n_runs):
            rng = np.random.default_rng(seed=run) if fixed_seed else np.random.default_rng()  # fixed seed schedule for reproducible inference
            random_indices = rng.choice(
                len(unseen_class_embeddings),
                size=X_test_scaled.shape[0],
                replace=True
            )
            random_semantics = unseen_class_embeddings[random_indices]
            X_test_aug = np.concatenate([X_test_scaled, random_semantics], axis=1)
            # Compute cosine similarities and accumulate
            similarities = 1 - spatial.distance.cdist(X_test_aug, S_projected, 'cosine')
            avg_similarities += similarities
            # Store individual run predictions for variance analysis
            preds = np.array([unseen_class_labels[idx] for idx in np.argmax(similarities, axis=1)])
            run_predictions.append(preds)
        avg_similarities /= n_runs
        self.run_predictions_ = run_predictions

        predicted_indices = np.argmax(avg_similarities, axis=1)
        y_pred = np.array([unseen_class_labels[idx] for idx in predicted_indices])
        return y_pred

    def predict_gzsl(self, X_test, all_class_embeddings, all_class_labels, seen_classes, gamma=0.4, n_runs=35, fixed_seed=True):
            """Predict labels over seen and unseen classes by averaging augmented inference similarities and applying seen-class calibration."""
            if n_runs < 1:
                raise ValueError("n_runs must be at least 1.")
            if self.scale_features:
                X_test_scaled = self.scaler.transform(X_test)
            else:
                X_test_scaled = X_test

            S_projected = all_class_embeddings @ self.W
            seen_mask = np.isin(all_class_labels, seen_classes)

            avg_similarities = np.zeros((X_test_scaled.shape[0], len(all_class_labels)))
            run_predictions = []
            for run in range(n_runs):
                rng = np.random.default_rng(seed=run) if fixed_seed else np.random.default_rng()
                random_indices = rng.choice(
                    len(all_class_embeddings),
                    size=X_test_scaled.shape[0],
                    replace=True
                )
                random_semantics = all_class_embeddings[random_indices]
                X_test_aug = np.concatenate([X_test_scaled, random_semantics], axis=1)
                similarities = 1 - spatial.distance.cdist(X_test_aug, S_projected, 'cosine')
                similarities[:, seen_mask] -= gamma
                avg_similarities += similarities
                preds = np.array([all_class_labels[idx] for idx in np.argmax(similarities, axis=1)])
                run_predictions.append(preds)
            avg_similarities /= n_runs
            self.run_predictions_gzsl_ = run_predictions
            
            predicted_indices = np.argmax(avg_similarities, axis=1)
            y_pred = np.array([all_class_labels[idx] for idx in predicted_indices])
            return y_pred