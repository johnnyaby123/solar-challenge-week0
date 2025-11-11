import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# --- Page Configuration ---
st.set_page_config(page_title="Solar Potential Dashboard", layout="wide")

st.title("☀️ Solar Energy Comparison Dashboard")
st.write("Interactive visualization of solar irradiance metrics across Benin, Sierra Leone, and Togo.")

# --- Load Data ---
@st.cache_data
def load_data():
    benin = pd.read_csv("../data/benin_clean.csv")
    sierra = pd.read_csv("../data/sierraleone-bumbuna_clean.csv")
    togo = pd.read_csv("../data/togo-dapaong_qc_clean.csv")
    benin["Country"] = "Benin"
    sierra["Country"] = "Sierra Leone"
    togo["Country"] = "Togo"
    return pd.concat([benin, sierra, togo], ignore_index=True)

df = load_data()

# --- Sidebar ---
st.sidebar.header("Filter Options")
countries = st.sidebar.multiselect(
    "Select Country",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)
metrics = st.sidebar.multiselect(
    "Select Metric(s)",
    options=["GHI", "DNI", "DHI"],
    default=["GHI"]
)
filtered_df = df[df["Country"].isin(countries)]

# --- Main Content ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Average Irradiance by Country")
    avg_values = filtered_df.groupby("Country")[metrics].mean()
    st.bar_chart(avg_values)

with col2:
    st.subheader("📈 Distribution by Metric")
    for metric in metrics:
        fig, ax = plt.subplots()
        filtered_df.boxplot(column=metric, by="Country", ax=ax)
        plt.title(f"{metric} by Country")
        plt.suptitle("")
        st.pyplot(fig)

# --- Summary Section ---
st.markdown("### 🧠 Key Insights")
st.markdown("""
- **Benin** shows the highest mean irradiance and stable performance.
- **Togo** maintains moderate but consistent solar metrics.
- **Sierra Leone** records lower values due to higher cloud cover.
""")

st.success("✅ Dashboard Loaded Successfully!")

