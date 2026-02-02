import streamlit as st

st.set_page_config(page_title="Sylvesters Oyim | Research Profile", page_icon="🧬", layout="wide")

# --- HEADER ---
st.title("Sylvesters Oyim")
st.subheader("BPharm Graduate | Aspiring Bioinformatician")
st.write(
    "BPharm graduate transitioning into Bioinformatics with strong interest in computational biology, "
    "genomic data analysis, and drug discovery research. Passionate about combining pharmaceutical "
    "knowledge with data science to solve real-world health challenges."
)

st.markdown("""
**Email:** sylvestersoyim@email.com  
**GitHub:** https://github.com/yourusername  
**Location:** United States  
""")

st.divider()

# --- ABOUT ---
col1, col2 = st.columns([2, 1])

with col1:
    st.header("About Me")
    st.write("""
- Bachelor of Pharmacy (BPharm)
- Transitioning into Bioinformatics and Computational Biology
- Interested in genomics, drug discovery, and precision medicine
- Building skills in Python, data analysis, and biological data processing
- Strong foundation in pharmacology and molecular biology
""")

with col2:
    st.header("Technical Skills")
    st.write("""
- Python (Pandas, NumPy, Biopython)
- Data Visualization (Matplotlib, Seaborn)
- Basic SQL
- Molecular Biology Concepts
- Statistical Analysis
""")

st.divider()

# --- PROJECTS ---
st.header("Selected Projects")

projects = [
    {
        "title": "Gene Expression Analysis in Breast Cancer",
        "desc": "Analyzed publicly available RNA-seq datasets to identify differentially expressed genes associated with breast cancer progression. Applied statistical filtering and visualization techniques to highlight potential biomarkers.",
        "tools": "Tools: Python, Pandas, Matplotlib, Bioinformatics pipelines",
        "link": "https://github.com/yourusername/gene-expression-analysis"
    },
    {
        "title": "Drug-Target Interaction Prediction Model",
        "desc": "Built a simple machine learning model to predict potential drug-target interactions using molecular descriptors and pharmacological datasets. Explored feature selection and model evaluation techniques.",
        "tools": "Tools: Python, Scikit-learn, NumPy",
        "link": "https://github.com/yourusername/drug-target-model"
    },
    {
        "title": "Pharmacovigilance Data Dashboard",
        "desc": "Developed an interactive dashboard to explore adverse drug reaction reports and identify trends in medication safety data.",
        "tools": "Tools: Python, Streamlit, Data Visualization",
        "link": "https://github.com/yourusername/pharmacovigilance-dashboard"
    },
]

for p in projects:
    st.subheader(p["title"])
    st.write(p["desc"])
    st.caption(p["tools"])
    st.write(f"Repository: {p['link']}")
    st.divider()

# --- FUTURE GOALS ---
st.header("Research Goals")
st.write("""
My goal is to specialize in bioinformatics-driven drug discovery and precision medicine.
I aim to contribute to research that integrates genomic data with pharmacological insights
to improve therapeutic outcomes and personalized treatment strategies.
""")

# --- FOOTER ---
st.caption("Built with Streamlit Community Cloud")
