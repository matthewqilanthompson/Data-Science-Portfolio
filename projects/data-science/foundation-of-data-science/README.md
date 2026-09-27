<!-- lint-ok: leaderboard-rank | leaderboard screenshot at ./images/leaderboard-readmission-test.png; the 5th->13th move is the evidence for the calibration argument -->
[← Back to Data Science Projects](../README.md)

# Healthcare Readmission Risk Prediction

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

Built a Random Forest model to predict 30-day hospital readmission risk from synthetic EHR data (587,801 training rows) for a class competition against dozens of other submissions. An early version of the model scored a suspicious perfect 1.0 ROC AUC, no train/test gap at all. Tracing that down to leaked target data, fixing it, and re-validating turned out to be the most useful part of the project (full story below).

**Leaderboard**: [CodaBench Competition 6813](https://www.codabench.org/competitions/6813/) (login-gated; CodaBench requires an account to view any competition page). Final rankings and scoring are documented below.

---

## Competition Results

**ROC AUC 0.858 on the final held-out test**, down only slightly from 0.901 in development.

| Phase           | Ranking    | ROC AUC | Participants |
| --------------- | ---------- | ------- | ------------ |
| **Development** | 5th place  | 0.9011  | 40           |
| **Testing**     | 13th place | 0.8581  | 35           |

![CodaBench test-phase leaderboard, competition 6813](./images/leaderboard-readmission-test.png)

_CodaBench test-phase leaderboard for competition 6813. Username `matthewqthomp` at rank 13 with ROC AUC 0.8581. Top 12 visible; full leaderboard had 35 participants._

My cross-validated AUC (~0.86) predicted the final test AUC (0.858) almost exactly. The model held up on unseen data. The development-phase leaderboard score (0.90) was the optimistic one; the rank moved from 5th to 13th as the field's scores settled on the held-out test.

---

## The Data Leakage Catch

While checking an early version of the model for overfitting, it returned a perfect 1.0 ROC AUC, with no gap between train and test. A perfect score isn't a result, it's a warning sign.

I traced it to a feature that aggregated `readmitted_within_30_days` by patient, but only counted rows where the value was already 1, so the target was leaking directly into the features. I removed that aggregation, rebuilt the feature set, and re-ran cross-validation. The corrected score came back with a small, expected gap (~0.04) between train and test, and it's the version that went on to predict the final held-out test AUC (0.858) almost exactly.

Catching that before it reached a leaderboard, rather than after, is the calibration check that mattered most in this project.

---

## Skills Applied

| Category            | Techniques                                                                                          |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| **Feature engineering** | Frequency encoding (`patient_id` -> encounter count), mean imputation at scale, dropping uninformative and leaky features |
| **Model selection**  | Compared 9 algorithms: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, HistGradientBoosting, AdaBoost, ExtraTrees, Bagging, KNeighbors |
| **Validation**       | Cross-validation, leakage detection via an implausibly perfect score, train/test gap analysis      |
| **Class imbalance**  | `class_weight='balanced'` to reduce bias from the unbalanced target                                 |

---

## Project Overview

Final project for INFO 511 (Foundation of Data Science): a CodaBench class competition to predict 30-day hospital readmissions on a Synthea-generated EHR dataset. Submitted model: Random Forest (`n_estimators=200`, `class_weight='balanced'`), chosen for a close ROC AUC score to HistGradientBoosting with a slightly lower standard deviation.

**Key Metrics**: 587,801 train rows • 125,958 dev rows • 9 algorithms compared • Final test ROC AUC 0.858 (13th/35)

---

## Feature Engineering & Data Quality

| Decision                       | Reasoning                                                                |
| ------------------------------- | ------------------------------------------------------------------------- |
| **Patient frequency encoding** | Transformed `patient_id` into encounter count per patient (key predictor); an earlier attempt that grouped on `patient_id` directly scored only ~0.69 |
| **Dropped zip code**           | Not meaningful without a distance calculation, and didn't correlate with readmission |
| **Dropped symptom columns**    | `has_chronic_pain`, `has_hypertension`, `has_diabetes`, `has_asthma`, `has_depression` all had a single identical value, so uninformative |
| **Mean imputation**            | Handled missing medication counts, procedure costs, pain scores, and patient height; appropriate given the large sample size |

---

## Dataset

Synthetic Arizona patient encounter records (Synthea-generated EHR) provided for the INFO 511 class competition. Full data documentation in [`data/README.md`](./data/README.md).

| File | Size | Records | Contents |
|---|---|---|---|
| [`data/train.csv`](./data/train.csv) | 88MB | 587,801 | Training set with features + target |
| [`data/dev.csv`](./data/dev.csv) | 19MB | 125,958 | Development/validation set with target |
| [`data/dev(renamed).csv`](./data/dev%28renamed%29.csv) | 19MB | 125,958 | Second dev split snapshot |
| [`data/test.csv`](./data/test.csv) | 19MB | features only | Held-out test set |
| [`data/submission.csv`](./data/submission.csv) | 7MB | predictions | Final submission scored on the leaderboard |

Target variable: `readmitted_within_30_days` (binary).

---

<details>
<summary>Project structure</summary>

```text
foundation-of-data-science/
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies (pandas, scikit-learn, joblib, numpy, datasets)
├── final_project_process.ipynb         # Main analysis notebook (1,272 lines)
├── final_project_process.md            # Markdown export of the notebook (browser-friendly)
├── ds.py                               # Core data science utilities (4.8KB)
├── train_predict.py                    # Model training + prediction CLI (6.7KB)
├── data/
│   ├── train.csv                       # Training dataset (587,801 records)
│   ├── dev.csv                         # Development/validation set (125,958 records)
│   ├── dev(renamed).csv                # Second dev split snapshot
│   ├── test.csv                        # Test dataset (features only)
│   ├── submission.csv                  # Final predictions
│   └── README.md                       # Data documentation
└── scripts/
    ├── scoring/                        # Competition evaluation scripts (CodaBench scoring)
    └── scoring_dev/                    # Development scoring tools
```

</details>

<details>
<summary>How to reproduce</summary>

Requires Python 3.9+.

```bash
# 1. Install deps
pip install -r requirements.txt

# 2. Train on train.csv, evaluate on dev.csv, save the trained model
python train_predict.py train \
  --train_path data/train.csv \
  --dev_path data/dev.csv \
  --model_path model.joblib

# 3. Predict on the held-out test set
python train_predict.py predict \
  --model_path model.joblib \
  --input_path data/test.csv \
  --output_path data/submission.csv
```

Full step-by-step EDA, feature engineering, and model selection is in [`final_project_process.ipynb`](./final_project_process.ipynb). A browser-readable markdown export is at [`final_project_process.md`](./final_project_process.md).

</details>

---

<sub>Class project, INFO 511 (Foundation of Data Science), University of Arizona, 2024-2025. Competition: CodaBench Healthcare Equity Explorer.</sub>
