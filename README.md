# Zero-Shot Learning for Human Activity Recognition

This repository contains the full experimental pipeline developed for a Master's thesis investigating Zero-Shot Learning (ZSL) and Generalised Zero-Shot Learning (GZSL) for micro-activity recognition using wearable sensor data.

## Overview

The repository implements the broader methodological framework of the thesis, including:

- data quality control and preprocessing of raw sensor recordings
- adaptive trimming of inactive starting and end periods in UiS4ADL recordings
- segmentation of recordings into fixed windows
- time- and frequency-domain feature extraction
- generation of semantic embeddings from different types of activity descriptions
- training and inference with the projection-based **IP-SAE** model
- evaluation under fixed **ZSL** and **GZSL** settings
- cross-dataset experiments between **UiS4ADL** and **PAAL ADL**
- analysis at both **segment level** and **recording level**
- generation of figures and result files.

Supporting notebooks for preprocessing, embedding generation, feature inspection, and hyperparameter tuning are located in `Data_preparation/`, `Embeddings/`, `Feature_extraction/`, and `Model/`.

## Repository structure

The main components of the repository are:
```
ZSL_Master_2026/
├── .gitignore
├── Data
│   └── adl_dict.json
├── Data_preparation
│   ├── 0_combine_UiS4ADL_datasets.ipynb
│   ├── 1_prepare_PAAL_ADL.ipynb
│   ├── 2_initial_data_cleaning.ipynb
│   ├── 3_feature_plots_analysis.ipynb
│   ├── 4_handle_inactivity_periods.ipynb
│   ├── 5_downsample_UiS4ADL.ipynb
│   └── 6_duration_statistics.ipynb
├── Embeddings
│   ├── Models
│   │   └── embedding_generator.py
│   ├── Semantics
│   │   └── descriptions.py
│   └── generate_embeddings.ipynb
├── Experiments
│   └── Experiments.ipynb
├── Feature_extraction
│   ├── Plot_imbalance.ipynb
│   └── feature_extractor.py
├── LICENSE
├── Model
│   ├── Gamma_tuning.ipynb
│   ├── Lambda_tuning.ipynb
│   ├── Inference_stability.ipynb
│   └── model.py
├── README.md
├── Results
│   ├── Figures
│   └── Others
│       ├── Split_Protocol
│       └── Trimming
├── Utils
│   └── split_strategies.py
└── requirements.txt
```

## Data availability

The datasets and cached semantic embeddings are not stored directly in the repository. They must be downloaded separately from Google Drive and placed into the repository before running the experiments.

Three downloads are required:

1. Pre-generated embeddings: [Download here](https://drive.google.com/file/d/1kayJGw0sBcrccNWqqJ6-TzDh6Zha-oh0/view?usp=sharing)
2. PAAL ADL dataset (raw and preprocessed versions): [Download here](https://drive.google.com/file/d/1CCyKBcgTjjI2-9aIfZK273ZOY0BoxrGs/view?usp=sharing)
3. UiS4ADL dataset (raw and preprocessed versions): [Download here](https://drive.google.com/file/d/1q7-q-O5oXi8A7iL4IEE9jo83CkdEKyiV/view?usp=sharing)

These archives should be downloaded from the provided links and extracted into the repository so that the required files appear under the `Data/` directory. The expected structure is:

```
ZSL_Master_2026/
├── Data
│   ├── Embeddings
│   │   └── ...
│   ├── PAAL_ADL
│   │   ├── Processed
│   │   │   └── PAAL_ADL_32hz.csv
│   │   └── Raw
│   │       ├── ADLs.csv
│   │       ├── data.zip
│   │       ├── dataset
│   │       │   └── ...
│   │       └── users.csv
│   ├── UiS4ADL
│   │   ├── Processed
│   │   │   ├── UiS4ADL_100hz.csv
│   │   │   ├── UiS4ADL_100hz_inactivity_removed.csv
│   │   │   ├── UiS4ADL_100hz_initially_cleaned.csv
│   │   │   ├── UiS4ADL_32hz.csv
│   │   │   └── UiS4ADL_acc_32hz.csv
│   │   └── Raw
│   │       ├── New
│   │       │   └── all_data.csv
│   │       ├── Old
│   │       │   └── UiS4ADL-100hz.csv
│   │       └── UiS4ADL_100hz_raw.csv
│   └── adl_dict.json
```

## Setup and execution

The implementation used in the thesis was developed in **Python 3.11.9**.  
The required dependencies are listed in `requirements.txt`.

A typical setup is:

```
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

No additional installation steps beyond Python and the listed dependencies are required.

The main experimental workflow is contained in `Experiments/Experiments.ipynb`.
The notebook is designed to be run sequentially from top to bottom. Later sections depend on variables, intermediate results, and outputs created in earlier sections. Running cells out of order may therefore lead to errors or incorrect results.

Before running the notebook:

1. download and extract the required archives into `Data/`
2. create and activate a Python environment
3. install the dependencies listed in `requirements.txt`
4. open `Experiments/Experiments.ipynb` and run all cells in order

## Reproducibility

The experiments were designed to support reproducible evaluation as closely as possible.
- Fixed random seeds are used where applicable.
- Pre-generated embeddings can be downloaded directly to match the thesis setup.
- Controlled comparisons reuse fixed splits and shared configurations where appropriate, so that observed differences reflect the experimental factor under investigation.
- Because inference includes repeated stochastic sampling, small numerical differences may still occur across runs. In the reported experiments, these differences were minor and did not affect the overall performance patterns or conclusions.

## License

This repository is licensed under the MIT License.