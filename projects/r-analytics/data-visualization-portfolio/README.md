[← Back to R Analytics Projects](../README.md)

# Data Visualization Portfolio

[![R](https://img.shields.io/badge/R-4.x-276DC3?style=for-the-badge&logo=r)](https://r-project.org)
[![RMarkdown](https://img.shields.io/badge/RMarkdown-Portfolio-FF6B35?style=for-the-badge&logo=r)](https://rmarkdown.rstudio.com)

R and ggplot2 across three unrelated datasets, cougar predation ecology, occupational fatality records, and the FHFA Housing Price Index. The focus throughout is category-decision rationale and visual readability over chart variety.

**Key metrics**: 3 domains • 6 visualizations across 4 figures • 146K+ fatality records

**[View Complete Portfolio (PDF)](./reports/MatthewThompson_Final_Portfolio.pdf)** | **[Source (.Rmd)](./Final-Portfolio-Assignment.Rmd)**

---

## Visualizations

### 1. Cougar Predation Ecology

**Plots**: Pie chart (prey distribution) and grouped bar chart (temporal trends).

I grouped 30+ prey species into 4 ecological categories (Wild Ungulates, Small Animals, Domestic Animals, Carnivores) to avoid overlapping classifications.

![Figure 1: cougar prey distribution by category](./images/figure-1-cougar-prey-pie.png)

![Figure 2: cougar kills by category, year over year](./images/figure-2-cougar-kills-by-year.png)

Findings:
- Wild ungulates (mule deer, bighorn sheep, pronghorn) are primary prey
- Domestic animals are the least common prey category
- Data gaps between 2012-2015
- Zero domestic animal kills recorded in 2016

### 2. Occupational Safety Analysis

**Plots**: Line graph (temporal trends) and alluvial diagram (cause-occupation flows).

I started with a proportional stream plot but switched to a line graph because stream plots hide absolute counts behind percentage shifts. The alluvial diagram (ggalluvial) shows how fatality causes map to the 5 most-dangerous occupations.

![Figure 3: top 5 most dangerous occupations: trends + cause-of-fatality flows](./images/figure-3-dangerous-jobs.png)

Findings:
- Transportation and mining are the most dangerous occupations
- Truck-related jobs (general freight, transportation & warehousing) trended up until a sharp 2023 drop
- Transportation incidents are the most common cause of fatality across the top 5 dangerous jobs; explosions and fires are the least common

### 3. Housing Price Index Trends

**Plots**: Faceted area plots (regional comparison) and a `gt` summary table.

![Figure 4: housing price index by U.S. region](./images/figure-4-hpi-by-region.png)

Findings:
- Midwest, Northeast, South show similar HPI trajectories
- West region has higher volatility
- All regions: increase to ~2005, decline through 2008-2010, recovery after 2010

---

## What I Applied

| Category | Techniques |
|---|---|
| **Plot types** | Pie, grouped bar, line, faceted area, alluvial (ggalluvial) |
| **Data wrangling** | dplyr categorical grouping, tidyr reshaping, lubridate dates |
| **Reproducibility** | RMarkdown source-to-PDF pipeline |
| **Custom tooling** | `data_dict()`, a reusable EDA helper for fast variable-level audits (types, missingness, summary stats), used during exploration of the three datasets |

**Tech stack**: R 4.x • RMarkdown • tidyverse (ggplot2, dplyr, lubridate, tidyr) • ggalluvial • viridis • patchwork • gt • readxl • reshape2

---

## Dataset Summary

| Dataset | File | Content |
|---|---|---|
| Cougar Killsites | [`data/Cougar Killsites.xlsx`](./data/Cougar%20Killsites.xlsx) | wildlife predation events, prey species + dates |
| Dangerous Jobs | [`data/Dangerous Jobs.csv`](./data/Dangerous%20Jobs.csv) | 146K+ occupational fatality records, 2003-2023 |
| Housing Price Index | [`data/Housing Price Index.xlsx - Data.csv`](./data/Housing%20Price%20Index.xlsx%20-%20Data.csv) | FHFA HPI, 4 U.S. regions, quarterly time series |

---

## Challenges Solved

### Category decisions over chart variety

Most of my course feedback was about category choices: which to group, which to drop. My tendency is to include too much in one view. For this portfolio I grouped 30+ prey species into 4 ecological categories without overlap, and dropped weight class from the grouped bar chart because reading the bars plus a weight-class overlay would be too dense.

### Stacked plots vs absolute comparison

I had started with a stacked bar chart over 10+ categories. Readers cannot accurately compare stacked values, so I switched to a grouped bar chart with fewer categories. For the most-dangerous-jobs question I used a line graph rather than a proportional stream graph, because the stream plot hides actual fatality counts behind percentage shifts.

### Alluvial diagram label readability

I built an alluvial diagram for cause-of-fatality flows. Text aesthetics were hard to read at default sizes. I considered replacing labels with a legend, but legends do not communicate where the flow starts. I kept the inline text labels and explained the diagram briefly in the caption.

### Pie-slice label placement

Course feedback suggested moving the legend labels into each pie slice. I got them only partially aligned and judged the external legend cleaner and less error-prone for this data, so I kept it. A readability call, not a blocker.

---

<details>
<summary>Repo structure</summary>

```text
data-visualization-portfolio/
├── README.md                                       # Project documentation
├── Final-Portfolio-Assignment.Rmd                  # Reproducible source (991 lines)
├── setup.R                                         # Installs the required R packages + TinyTeX
├── Data Dictionary Function.R                      # Standalone EDA helper (not sourced by the Rmd)
├── Final_MinMaxHPI_Output.pdf                      # Build artifact regenerated by the Rmd
├── scripts/
│   └── export_readme_figures.R                     # Regenerates the 4 README PNGs from the same data
├── images/                                         # PNGs embedded in this README
│   ├── figure-1-cougar-prey-pie.png
│   ├── figure-2-cougar-kills-by-year.png
│   ├── figure-3-dangerous-jobs.png
│   └── figure-4-hpi-by-region.png
├── data/                                           # cougar, occupational safety, housing data
└── reports/
    ├── MatthewThompson_Final_Portfolio.pdf         # Final rendered portfolio
    └── Final-Portfolio-Assignment.pdf              # Assignment PDF version
```

</details>

<details>
<summary>How to reproduce</summary>

Source: [`Final-Portfolio-Assignment.Rmd`](./Final-Portfolio-Assignment.Rmd). View the rendered result directly at [`reports/MatthewThompson_Final_Portfolio.pdf`](./reports/MatthewThompson_Final_Portfolio.pdf), or knit it yourself:

```r
# 1. Install packages + TinyTeX (one-time, ~2 minutes)
source("setup.R")

# 2. From RStudio: open this folder as an RStudio project, then knit Final-Portfolio-Assignment.Rmd
# Or from the R console:
rmarkdown::render("Final-Portfolio-Assignment.Rmd", output_format = "pdf_document")
```

[`setup.R`](./setup.R) installs the required packages and bootstraps TinyTeX (a minimal LaTeX distribution) if no system TeX is detected. PDF render takes ~30 seconds after setup.

The 4 PNGs in `images/` are produced by [`scripts/export_readme_figures.R`](./scripts/export_readme_figures.R), which reads the same data files the Rmd uses and rebuilds each plot with thumbnail-readable styling. The Rmd itself is unchanged.

```r
Rscript scripts/export_readme_figures.R
```

</details>

---

<sub>Course portfolio, INFO 526 (Data Visualization), University of Arizona, 2024-2025.</sub>
