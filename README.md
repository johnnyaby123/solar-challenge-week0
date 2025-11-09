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

##  Task 2 — Data Profiling, Cleaning & EDA

**Goal:** Profile, clean, and analyze solar radiation data for Benin to uncover trends and prepare it for regional comparison.

### **Key Steps**
1. **Data Profiling**
   - Verified dataset completeness — no missing values.
   - Reviewed column ranges for physical consistency across 19 variables.

2. **Data Cleaning**
   - Removed invalid values (e.g., negative irradiance).
   - Applied **Z-score (|Z| > 3)** to detect and remove outliers.
   - Exported cleaned data to `data/benin_clean.csv` (excluded from Git).

3. **Exploratory Data Analysis**
   - **Time Series:** Visualized GHI, DNI, DHI, and Tamb trends; identified daily and seasonal irradiance cycles.
   - **Cleaning Impact:** Observed ~10–15% improvement in irradiance readings after sensor cleaning.
   - **Correlation Analysis:** Found strong relationships between solar variables; negative correlation between humidity and temperature.
   - **Wind & Distribution:** Winds primarily from North and Southwest; moderate speed patterns (< 15 m/s).
   - **Temperature Analysis:** Higher humidity linked to lower irradiance and cooler temperatures.
   - **Bubble Chart:** Showed combined effects of humidity, temperature, and solar intensity.

✅ **Outcome:**  
A clean, validated, and well-documented dataset ready for predictive and comparative analysis.

---

##  Project Structure



