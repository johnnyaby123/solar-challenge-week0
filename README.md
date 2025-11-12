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

---

## 🌍 Task 3: Cross-Country Comparison

### 🎯 Objective
To synthesize the cleaned solar datasets from **Benin**, **Sierra Leone**, and **Togo** in order to compare their relative solar potential and highlight key regional differences.

### 📂 Branch
`compare-countries`

### 📘 Notebook
`notebooks/compare_countries.ipynb`

### 🧠 Approach
1. Loaded the cleaned datasets:
   - `data/benin_clean.csv`
   - `data/sierraleone_clean.csv`
   - `data/togo_clean.csv`
2. Computed **summary statistics** (mean, median, std) for GHI, DNI, and DHI.
3. Created **boxplots** to visualize distribution of solar irradiance metrics per country.
4. Performed a **one-way ANOVA test** on GHI values to check for statistically significant differences.
5. Visualized **average GHI ranking** through a comparative bar chart.
6. Documented insights and actionable recommendations in the final markdown summary.

### 📊 Key Findings
- **Benin** has the **highest mean GHI (237 W/m²)** — indicating the strongest solar potential.
- **Togo** follows with a slightly lower but consistent GHI trend.
- **Sierra Leone** shows **lower irradiance** likely due to cloudier conditions and higher humidity.
- ANOVA confirmed **statistical significance (p < 0.05)** in GHI variation between countries.

### ✅ Outcome
The analysis successfully established a regional ranking:
1. 🥇 **Benin** — highest solar irradiance potential  
2. 🥈 **Togo** — moderate and stable performance  
3. 🥉 **Sierra Leone** — lower potential but still viable for adaptive solar systems  

## 💻 Bonus: Streamlit Interactive Dashboard  

### 🎯 Objective  
To build an interactive dashboard using **Streamlit** to visualize solar irradiance metrics (GHI, DNI, DHI) across the three countries — Benin, Sierra Leone, and Togo.

### ⚙️ Features Implemented  
- Sidebar country and metric selection  
- Interactive bar chart and boxplot visualizations  
- Dynamic summary statistics (mean, median, standard deviation)  
- Cached data loading for faster performance using `@st.cache_data`  

### 🧩 Folder Structure  

app/
├── main.py # main Streamlit app script
└── utils.py # optional helper functions (if needed)


### 🧠 Technical Notes  
- Developed using **Streamlit**, **Pandas**, and **Matplotlib**.  
- Replaced `st.bar_chart()` with Matplotlib plotting to fix `altair` compatibility error.  
- Added a version pin in `requirements.txt`:


altair<5

- Compatible with Python 3.9+ and works with cleaned local CSVs in the `data/` folder.  

### 🚀 How to Run Locally  
1. Activate your virtual environment:
 ```bash
 source venv/Scripts/activate


2. Run the dashboard:

streamlit run app/main.py


3. Open your browser at the URL shown in the terminal (usually http://localhost:8501).

🏁 Outcome

✅ A fully functional interactive dashboard that visualizes and compares solar irradiance across Benin, Sierra Leone, and Togo — providing an accessible, data-driven way to explore solar potential.

#### 🌐 Deployment
Deployed via [Streamlit Community Cloud](https://solar-challenge-week0-tzssgmt5rvggvzyw9ptnbz.streamlit.app/).

> **Live Demo:** [🔗 View Dashboard on Streamlit](https://solar-challenge-week0-tzssgmt5rvggvzyw9ptnbz.streamlit.app/)  


#### 🖼 Dashboard Preview
![Dashboard Screenshot](dashboard_screenshots/dashboard.png)

---

### 🧾 Final Report
**Title:** *Discovering Africa’s Solar Potential: Insights from Benin, Sierra Leone, and Togo*  
- Written in Medium-style format summarizing all three tasks.  
- Includes visuals, methodology, and conclusions.  

📄 **PDF Report:** [🔗 View Report on Google Drive](https://drive.google.com/file/d/1e5g4mXpOIkcpWnwlScmDna0WG4THaXUW/view?usp=sharing)  

---

### 🧩 Key Takeaways
- Learned version control best practices with Git & GitHub.  
- Built strong data cleaning and EDA foundation.  
- Explored solar data patterns and environmental correlations.  
- Created an interactive and deployable dashboard using Streamlit.

---

### 👨‍💻 Author
**Yohannes Abayneh Lemma**  
*10 Academy KAIM Cohort — Week 0 Project*