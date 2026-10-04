# GitHub Copilot Instructions for Portfolio Repository

## ⚠️ CRITICAL: Command Logging Protocol

**When using the `run_in_terminal` tool, you MUST log every command immediately after execution:**

```bash
source ~/Documents/DEVELOPMENT/error-log/ai-integration/copilot-conversation-logger-v2.zsh && \
log_copilot_command "your-command-here" $exit_code "output-preview" "copilot_chat"
```

**Why**: `run_in_terminal` bypasses shell hooks - manual logging is the ONLY way to capture Copilot Chat commands for error learning and history tracking. This is NOT optional.

---

## Repository Overview

This is a **Master's Data Science portfolio** demonstrating academic projects across R analytics, Python data science, database systems, and system automation. The structure is organized by project type rather than technology, with each major project containing its own dependencies and documentation.

## Critical Architecture Patterns

### Multi-Language Project Organization

- **Projects are technology-isolated**: Each project folder (`projects/automation/`, `projects/data-science/`, `projects/r-analytics/`) contains independent environments with separate `requirements.txt` or R dependencies
- **No root-level dependencies**: Install dependencies within specific project directories, not at repository root
- **Path context matters**: Many Python scripts use absolute paths (e.g., `train_predict.py` has hardcoded venv paths) - be aware of environment-specific paths when debugging

### Key Technology Combinations

- **R Projects**: Use RMarkdown (`.Rmd`) or Quarto (`.qmd`) for documentation, ggplot2 for visualization, Shiny for dashboards
- **Python Data Science**: Jupyter notebooks (`.ipynb`) with Quarto for publishing to HTML/websites
- **Automation**: Shell scripts use `#!/usr/bin/env bash` or `#!/usr/bin/env zsh` - maintain this convention

## Essential Development Workflows

### Running Quarto Projects

```bash
cd projects/data-science/data-mining-final-project
quarto render              # Build entire site
quarto preview             # Live preview with hot reload
quarto publish gh-pages    # Deploy to GitHub Pages
```

**Key files**: `_quarto.yml` defines website structure, navigation, and rendering options. The `index.ipynb` is the main analysis notebook.

### Running R Shiny Dashboards

```bash
R -e "shiny::runApp('projects/r-analytics/sales-dashboard')"
```

**Pattern**: Self-contained `app.R` files with UI and server in single file. Uses `shinydashboard`, `plotly`, `DT`, and `dplyr`.

### Python Environment Setup

```bash
cd projects/data-science/data-mining-final-project
pip install -r requirements.txt
jupyter lab index.ipynb
```

**Note**: Python 3.11+ required. Projects use scikit-learn, pandas, SHAP for ML interpretability.

### Shell Script Conventions

- Error management system in `projects/automation/error-management/` uses structured logging with unique IDs
- Scripts include comprehensive headers with author/course info for academic context
- Use `chmod +x` on new shell scripts before running

### Database Systems Setup

- **Docker containerization**: Database systems projects use Docker for MySQL setup
- **SQL backups**: Check `database-backup/` directories for schema, sample data, and analytics SQL files
- **Healthcare data**: Projects use ~65MB Synthea synthetic EHR datasets across 6 normalized entities
- **Schema pattern**: Three-file backup structure: `*_schema.sql`, `*_sample_data.sql`, `*_analytics_reports.sql`

## Project-Specific Conventions

### Data Science Projects

- **Superphyla grouping pattern**: In `data-mining-final-project`, phyla are grouped into 5 superphyla to reduce sparsity - maintain this preprocessing pattern if modifying analysis
- **SHAP analysis standard**: Use SHAP library for model explainability in ML projects (see `index.ipynb` for implementation examples)
- **Balanced metrics**: Use balanced accuracy and macro F1 for imbalanced classification (not standard accuracy)

### R Visualization Projects

- **ggplot2 + plotly combo**: R projects use ggplot2 for static visualizations, plotly for interactivity
- **RMarkdown output**: PDF output with `knitr::opts_chunk$set(echo = TRUE, warning=FALSE, message=FALSE, results='hide')`
- **Data dictionary functions**: Custom functions for data exploration (see `Data Dictionary Function.R`)

### Automation Projects

- **smart-file-organizer**: Uses `pyproject.toml` (modern Python packaging), not `setup.py`
- **OpenAI integration**: AI classifier requires `OPENAI_API_KEY` environment variable
- **SQLite audit trails**: Organizer uses SQLite for undo functionality - database operations in `src/utils/database.py`

## Critical Integration Points

### Quarto + Jupyter + GitHub Pages

The `data-mining-final-project` uses a specific workflow:

1. Analysis done in `index.ipynb` (Jupyter with Python 3.12+)
2. `_quarto.yml` configures website structure with freeze: auto for caching
3. Renders to `docs/` directory for GitHub Pages
4. Theme toggles between `flatly` (light) and `darkly` (dark)

### R + Python Integration

Some projects mix R and Python (e.g., statistical functions in R called from Python) - respect language boundaries and use appropriate documentation formats for each.

## Common Pitfalls to Avoid

1. **Don't install packages globally**: Each project has isolated environments
2. **Respect absolute paths**: Some Python scripts use hardcoded paths for local development - these need adjustment for different environments
3. **Academic context**: Projects include course information and academic framing - maintain this context in modifications
4. **Binary vs evolutionary data**: In data-mining project, binary data performed poorly vs evolutionary rates - don't assume both datasets are equivalent
5. **Shell script permissions**: New scripts need `chmod +x` to be executable

## Documentation Standards

- **README structure**: Each project has comprehensive README with badges, quick start, technical stack, and project components
- **Code folding in Quarto**: Use `code-fold: true` and `code-summary: "Code"` in YAML frontmatter for cleaner HTML output
- **Academic citations**: Data science projects include `citations.qmd` files - maintain bibliography references

## Testing and Validation

- **Python tests**: Use pytest in `tests/` directories (e.g., `smart-file-organizer/tests/`)
- **R validation**: RMarkdown rendering serves as validation - if it renders, code works
- **Demo scripts**: `demo.sh` files provide interactive demonstrations - use these to understand project workflows

## GitHub Actions & CI/CD

- **Update stats workflow**: `.github/workflows/update-stats.yml` runs every 6 hours to update GitHub activity stats
- **Manual triggers**: Workflows support `workflow_dispatch` for manual execution
- **Portfolio context**: Actions are lightweight (stats updates only) - don't add heavy CI/CD without discussion

## Key Files for Understanding Architecture

- `WARP.md`: Terminal-specific guidance, technology stack, and development commands
- `projects/automation/README.md`: Automation project overview and architecture diagrams
- `projects/data-science/data-mining-final-project/_quarto.yml`: Quarto configuration patterns
- `projects/automation/smart-file-organizer/pyproject.toml`: Modern Python project structure

## Portfolio-Specific Context

This repository is actively used for:

- **Job applications**: Focus on demonstrating competency and professional presentation
- **Academic coursework**: Projects include final projects for INFO 523, INFO 526, INFO 579
- **Skill demonstration**: Healthcare analytics (EHR/Synthea data), ecological analysis, ML pipelines, system automation
- Keep all modifications aligned with portfolio presentation standards and reproducible research principles
