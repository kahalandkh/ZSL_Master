# Zero-Shot Learning for Wrist-Worn Micro-Activity Recognition: Evaluation, Pipeline Analysis, and Cross-Dataset Generalisation

This repository contains the experimental pipeline accompanying a study investigating Zero-Shot Learning (ZSL) and Generalised Zero-Shot Learning
(GZSL) for wrist-worn micro-activity recognition, including controlled semantic-factor experiments, cross-dataset evaluation, and subject-independent evaluation.


## Overview

The repository implements the experimental framework used in the study, including:

- data quality control and preprocessing of raw sensor recordings
- adaptive trimming of inactive periods at the beginning and end of UiS4ADL recordings
- segmentation of recordings into fixed windows
- time and frequency domain feature extraction
- generation of semantic embeddings from different types of activity descriptions
- training and inference with the projection-based **IP-SAE** model
- evaluation under fixed **ZSL** and **GZSL** settings
- subject-independent ZSL evaluation
- cross-dataset experiments between **UiS4ADL** and **PAAL ADL**
- analysis at both **segment level** and **recording level**
- generation of figures and result files.

Supporting code and notebooks for preprocessing, embedding generation, feature analysis, and hyperparameter tuning are organised in `Data_preparation/`, `Embeddings/`, `Feature_extraction/`, and `Model/`.

## Repository structure

The main components of the repository are:
```
repository/
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
│   ├── Experiments.ipynb
│   └── Experiments_subject_independent.ipynb
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

The experiments use the PAAL ADL and UiS4ADL datasets.

#### PAAL ADL

The raw PAAL ADL dataset is publicly available from [Zenodo](https://zenodo.org/records/5785955):

Climent-Pérez, P., Muñoz-Antón, Á. M., Poli, A., Spinsante, S., & Florez-Revuelta, F. *PAAL ADL Accelerometry Dataset v2.0* (Version 2.0). Zenodo. DOI: 10.5281/zenodo.5785955.

After downloading the dataset, place the original files under: `Data/PAAL_ADL/Raw/`. The preprocessing used in this study is implemented in `Data_preparation/1_prepare_PAAL_ADL.ipynb`.

#### UiS4ADL

The UiS4ADL dataset used in this study is available through **FLAIR: Free-Living Activities for Independent-living Recognition**:

Demrozi, F. *FLAIR: Free-Living Activities for Independent-living Recognition*. Zenodo, 2026. Project repository: https://github.com/FlorencDemrozi/flair

After obtaining the full dataset, place the original files under: `Data/UiS4ADL/Raw/`. The preprocessing steps used in this study are provided in `Data_preparation/`. The relevant preprocessing notebooks should be run in numerical order.

## Semantic embeddings

Semantic embeddings are not included in the repository. They can be regenerated from the provided activity descriptions by running `Embeddings/generate_embeddings.ipynb`. The notebook generates the embeddings required by the experiments for all supported embedding models and activity-description variants.


## Expected data structure

After obtaining the required data and running the preprocessing notebooks, the `Data/` directory should have the following structure:

```
repository/
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

The implementation used in the experiments was developed in **Python 3.11.9**.  
The required dependencies are listed in `requirements.txt`.

A typical setup is:

```
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

No additional software installation beyond Python and the listed dependencies is required. Regenerating semantic embeddings requires downloading the pretrained embedding models used in the experiments.

The main experimental workflow is contained in `Experiments/Experiments.ipynb`, with the subject-independent evaluation provided separately in `Experiments/Experiments_subject_independent.ipynb`.
The notebooks are designed to be run sequentially from top to bottom. Later sections depend on variables, intermediate results, and outputs created in earlier sections. Running cells out of order may therefore lead to errors or incorrect results.

Before running the main experiment notebooks:

1. obtain the required datasets and place the raw files under `Data/` using the structure described above
2. create and activate a Python environment
3. install the dependencies listed in `requirements.txt`
4. run the relevant preprocessing notebooks in `Data_preparation/`
5. generate the semantic embeddings using `Embeddings/generate_embeddings.ipynb`
6. open `Experiments/Experiments.ipynb` and run all cells in order
7. to reproduce the subject-independent experiments, open `Experiments/Experiments_subject_independent.ipynb` and run all cells in order

## Reproducibility

The experiments were designed to support reproducible evaluation as closely as possible.
- Fixed random seeds are used where applicable.
- Semantic embeddings can be regenerated from the provided activity descriptions using `Embeddings/generate_embeddings.ipynb`.
- Controlled comparisons reuse fixed activity splits and shared configurations where appropriate to reduce variation between experimental conditions.
- Subject-independent evaluation uses 50 repeated random participant partitions, reused across the corresponding experimental comparisons.
- Because inference includes repeated stochastic sampling, small numerical differences may still occur across runs. In the reported experiments, these differences were minor and did not affect the overall performance patterns or conclusions. `Model/Inference_stability.ipynb` separately evaluates the variability introduced when inference is run without fixed seeds.

## License

The code in this repository is licensed under the MIT License. The datasets used in the experiments are subject to their respective access conditions and licences.