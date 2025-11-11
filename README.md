 #  Solar Challenge — Week 0

### Project Overview
This project is part of the 10 Academy KAIM Program, Week 0 — *Solar Data Discovery*.  
The objective is to build a reproducible workflow using Git, explore and clean solar radiation datasets, and prepare them for comparative regional analysis.

---

##  Task 1 — Git & Environment Setup

**Goal:** Establish a robust and collaborative Python development environment.

**Key Steps:**
- Created a GitHub repository named `solar-challenge-week0`.
- Initialized the repo locally and created a virtual environment (`venv`).
- Added `.gitignore` to exclude `data/` and `.ipynb_checkpoints/`.
- Installed required dependencies via `requirements.txt`.
- Configured a GitHub Actions CI workflow (`.github/workflows/ci.yml`) to verify setup.
- Created and merged a feature branch (`setup-task`) with commits:
  - `init: add .gitignore`
  - `chore: venv setup`
  - `ci: add GitHub Actions workflow`
- Merged branch into `main` through a pull request.

✅ **Outcome:**  
Clean, version-controlled Python environment with continuous integration (CI) for reproducibility.

---

## 🧭 Task 2 — Data Profiling, Cleaning & Exploratory Data Analysis  

### 🎯 Objective  
To profile, clean, and explore the solar radiation datasets for **Benin**, **Sierra Leone**, and **Togo**, preparing them for region-level comparison and solar potential assessment.

---

### 🧰 Steps Performed  

1. **Branch Creation**  
   - Created separate EDA branches for each country (`eda-benin`, `eda-sierraleone`, `eda-togo`) to ensure clean version control and modular analysis.  

2. **Data Loading & Profiling**  
   - Loaded each CSV dataset from the `data/` folder into Jupyter Notebooks under `notebooks/`.  
   - Executed `df.info()`, `df.describe()`, and `df.isna().sum()` to inspect datatypes, distributions, and missing values.  
   - Verified that timestamps were correctly parsed and data types aligned with expectations.  

3. **Data Cleaning**  
   - Defined realistic physical ranges for variables such as `GHI`, `DNI`, `DHI`, `Tamb`, `RH`, `WS`, `BP`, etc.  
   - Removed non-physical or negative values using range-based filtering.  
   - Computed **Z-scores** for sensor columns (`|Z| > 3`) to detect and remove outliers.  
   - Dropped or imputed missing values with the median as needed.  
   - Exported cleaned DataFrames as `<country>_clean.csv` (kept in `.gitignore`).  

4. **Exploratory Data Analysis (EDA)**  
   - Visualized **time-series** patterns for irradiance and temperature.  
   - Created **correlation heatmaps** to assess relationships among solar and weather variables.  
   - Generated **scatter plots**, **histograms**, and **wind-rose** visualizations for wind direction and speed.  
   - Examined **humidity–temperature** and **irradiance–temperature** relations via bubble charts.  
   - Analyzed module performance (`ModA` & `ModB`) before and after cleaning operations.  

---

### 🌍 Country-Level Highlights  

| Country | Key Insights |
|:--|:--|
| **Benin** | Stable irradiance profile with minimal outliers; clear daily solar cycles observed. |
| **Sierra Leone** | Higher humidity levels with moderate solar potential and good data consistency. |
| **Togo** | Strong midday irradiance peaks; lower humidity correlates with higher GHI; consistent wind patterns. |

---

### 🧾 Outputs  

- Cleaned CSVs stored in `data/` (ignored by Git).  
- Jupyter Notebooks saved in `notebooks/`:  
  - `benin_eda.ipynb`  
  - `sierraleone_eda.ipynb`  
  - `togo_eda.ipynb`  

---

### 🏁 Summary  

This phase ensured reliable, clean, and well-profiled data for each country’s solar dataset.  
All three datasets are now ready for **Task 3 – Comparative Analysis and Region Ranking**, where statistical comparisons and KPIs will determine which site demonstrates the strongest solar potential.

---

### ✅ Next Step  
Proceed to **Task 3**, combining cleaned datasets to compare and rank regions using quantitative metrics and visualization-driven insights.



