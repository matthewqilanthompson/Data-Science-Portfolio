[← Back to Data Science Projects](../README.md)

# Trait-Based Prediction of Animal Taxa

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![SHAP](https://img.shields.io/badge/SHAP-Explainability-FF6B6B?style=flat-square)
![Quarto](https://img.shields.io/badge/Quarto-Website-75AADB?style=flat-square&logo=quarto&logoColor=white)

Compared two ways of encoding animal trait data, binary presence/absence vs. evolutionary origin rates, to see which one better predicts an animal's higher-level taxonomic group from sexually selected traits, using 1,087 families (binary data) and 84 phylum-level rate estimates.

**[View Live Website](https://info-523-su25.github.io/final-project-thompson/)** | **[Analysis Notebook](./index.ipynb)**

---

## Research Question

**Can sexually selected traits predict higher-level taxonomic groups (superphyla), and which traits matter most?**

**Evolutionary-rate features scored higher than binary presence/absence on macro F1 (0.31 vs 0.13), though on a much smaller test set (28 rows); a random-forest 5-fold cross-validation on the rate data scored 0.19, near the ~0.20 chance baseline for 5 classes, so the signal is limited.** Best model: Logistic Regression on rate data (macro F1 0.31, balanced accuracy 0.32).

This is where biology and data science meet: the features aren't generic columns, they're domain-informed trait categories (sexually selected, visual, competition, auditory, female choice), and that domain framing is what guided how the SHAP results were interpreted.

---

## What Surfaced

<p align="center">
  <img src="./images/Plots/phylum_distribution.png" alt="Distribution of families across phyla" width="600">
</p>

_Dataset has 1,087 animal families across 5 superphyla. Class imbalance (Arthropoda ~84%) required balanced metrics._

|                Evolutionary Rates (Better)                |                Binary Presence/Absence                 |
| :---------------------------------------------------------: | :--------------------------------------------------------: |
| <img src="./images/Plots/SHAP_evolution.png" width="350"> | <img src="./images/Plots/SHAP_family.png" width="350"> |
|    Visual (V), Competition (C), Auditory (A) strongest    |               Sparse data, weak signal                |

On the binary data, SHAP showed the model leaned almost entirely on one feature (the "sexually selected" flag). On evolutionary-rate data, the signal spread across Visual, Competition, Auditory, and Female-choice traits: a more honest and generalizable signal.

---

## Skills Applied

| Category | Techniques |
|---|---|
| **Preprocessing** | Missing value handling, log-transform + standardization of evolutionary rates, label encoding |
| **Cross-validation** | Stratified K-fold to preserve class proportions across folds |
| **Models** | Logistic Regression, Decision Tree, Random Forest |
| **Explainability** | SHAP values for feature importance ranking |
| **Evaluation** | Balanced accuracy, macro F1 (instead of accuracy / ROC-AUC, given the class imbalance) |
| **Feature engineering** | Domain-driven grouping of phyla into 5 superphyla |
| **Reproducibility** | Quarto website (Jupyter notebook + .qmd source, rendered to an HTML site) |

---

## Findings

| Finding | Detail |
|---|---|
| **Evolutionary rates > Binary data** | Continuous origin rates gave a stronger signal than sparse binary presence/absence data |
| **Best model: macro F1 0.31, balanced accuracy 0.32** | Logistic Regression on evolutionary-rate data, vs. macro F1 0.13 on binary data (different, larger test set). Raw accuracy was 0.50, inflated by the ~84% Arthropoda imbalance, which is why balanced metrics are reported instead. |
| **Key predictors** | Visual, Competition, and Auditory traits (identified via SHAP) |
| **Class imbalance matters** | Balanced accuracy and macro F1 used instead of raw accuracy throughout |

### Models Tested

| Model | Data Type | Result |
|---|---|---|
| **Logistic Regression** | Evolutionary rates | **macro F1 0.31, balanced acc 0.32 (best)** |
| Random Forest | Evolutionary rates | macro F1 0.23, balanced acc 0.32 |
| Decision Tree | Evolutionary rates | macro F1 0.09, balanced acc 0.23 |
| All models | Binary data | macro F1 0.09-0.13, balanced acc 0.28-0.30 |

---

## Dataset

| File | Records | Description |
|---|---|---|
| [`family_related_data.csv`](./data/family_related_data.csv) | 1,087 families | Binary trait presence/absence |
| [`animals_rateof_evolution.csv`](./data/animals_rateof_evolution.csv) | 84 estimates | Evolutionary origin rates |

_Why the size gap: the binary file records trait presence/absence per **family** (1,087 rows); the evolutionary-rate file holds maximum-likelihood origin-rate estimates aggregated at the **phylum** level, one row per phylogenetic-tree replicate (84 rows). They're model-derived summaries, not per-family observations._

**Traits analyzed**: Auditory (A), Gustatory (G), Olfactory (O), Tactile (T), Visual (V), Male competition (C), Female competition (K), Intersexual conflict (S), Female choice (F), Male choice (M)

**Classification target**: 5 superphyla (Ecdysozoa, Lophotrochozoa, Deuterostomia, Basal Metazoa, Basal Bilateria)

Full codebook: [`data/README.md`](./data/README.md)

---

## Challenges Solved

The two datasets behaved very differently. The binary data was sparse and dominated by Arthropoda (~84% of samples), and SHAP showed the model leaned almost entirely on the "sexually selected" flag. The evolutionary-rate data was more balanced, and its signal spread across Visual, Competition, Auditory, and Female-choice traits, which is why rate-based features predicted taxonomy better than binary presence.

Next time: drop the SS trait from the family-level model, since it was masking every other signal, and prioritize collecting less sparse, less imbalanced trait data before pushing model complexity further.

---

<details>
<summary>Repo structure</summary>

```text
data-mining-final-project/
├── README.md                          # This file
├── index.ipynb                        # Main analysis notebook (99 cells, 1.2MB)
├── _quarto.yml                        # Quarto website configuration
├── requirements.txt                   # Python dependencies (jupyter, scikit-learn, shap, etc.)
├── proposal.qmd                       # Research proposal
├── presentation.qmd                   # Results presentation
├── data.qmd                           # Dataset description page
├── about.qmd                          # About page
├── citations.qmd                      # Bibliography
├── data/
│   ├── family_related_data.csv        # Binary traits (1,087 families, 50KB)
│   ├── animals_rateof_evolution.csv   # Evolutionary rates (84 estimates, 12KB)
│   └── README.md                      # Data codebook
├── images/
│   ├── Plots/                         # SHAP and EDA plots
│   └── tree_scenery.jpg               # Header image for the site
└── docs/                              # Generated Quarto website (regenerated by `quarto render`)
```

**Other resources**: [Proposal](./proposal.qmd) (original research questions and methodology), [Presentation](./presentation.qmd) (key findings and visualizations), [Data Codebook](./data/README.md) (complete variable descriptions).

</details>

<details>
<summary>Reproduce it</summary>

Requires Python 3.10+ and [Quarto 1.5+](https://quarto.org/docs/get-started/).

```bash
# 1. Install Python deps
pip install -r requirements.txt

# 2. Render the full website (notebook + .qmd pages -> docs/)
quarto render

# Or render just the main analysis notebook
quarto render index.ipynb
```

`quarto render` produces the static site in [`docs/`](./docs/), the same site published at [info-523-su25.github.io/final-project-thompson/](https://info-523-su25.github.io/final-project-thompson/). Full render takes ~30 seconds; single-notebook render is ~3 seconds.

</details>

---

<sub>Course project, INFO 523 (Data Mining & Machine Learning), University of Arizona, Summer 2025. Project template inspired by Mine Çetinkaya-Rundel @ Duke University.</sub>
