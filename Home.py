import streamlit as st

from style import inject_css, page_header, spectrum_legend
from utils import generate_synthetic_data, clean_data

st.set_page_config(
    page_title="App User Behavior Segmentation",
    page_icon="📊",
    layout="wide",
)
inject_css()

# ---------------------------------------------------------------- session init
if "df_raw" not in st.session_state:
    st.session_state["df_raw"] = generate_synthetic_data()
if "df_clean" not in st.session_state:
    st.session_state["df_clean"] = clean_data(st.session_state["df_raw"])

page_header(
    "📊", "App User Behavior Segmentation",
    "An unsupervised machine learning pipeline that turns raw app-activity logs "
    "into four behavioral segments — and each segment into a concrete business action.",
)

df = st.session_state["df_clean"]
col1, col2, col3, col4 = st.columns(4)
col1.metric("Users loaded", f"{len(df):,}")
col2.metric("Features tracked", "8 behavioral")
col3.metric("Segments (K-Means)", "4")
col4.metric("Missing values", int(df.isnull().sum().sum()))

st.write("")

left, right = st.columns([1.3, 1], gap="large")

with left:
    with st.container(border=True):
        st.subheader("How to use this app")
        st.markdown(
            """
Use the sidebar to move through the pipeline, in order:

1. **Data Overview** — generate or upload a dataset, inspect schema and quality.
2. **EDA** — distribution plots and a correlation heatmap (Matplotlib/Seaborn).
3. **Clustering** — pick *k* interactively, view the Elbow plot, fit K-Means, and see the PCA scatter.
4. **Cluster Profiles** — compare segments on engagement, churn risk, and activity.
5. **Business Insights** — segment → action mapping, with CSV exports.

Data, cluster assignments, and settings carry over between pages via the
session state, so you can move back and forth freely.
"""
        )

with right:
    with st.container(border=True):
        st.subheader("The engagement spectrum")
        st.caption("Every user lands somewhere on this scale — it's the throughline for the whole app.")
        spectrum_legend()
        st.markdown(
            "<p style='font-size:0.86rem;color:#5B6B6E;margin-top:10px;'>"
            "Segments are ranked by average engagement score once K-Means runs on the "
            "<b>Clustering</b> page, then reused everywhere downstream.</p>",
            unsafe_allow_html=True,
        )

st.write("")
st.subheader("Business use cases")
uc1, uc2, uc3 = st.columns(3)
use_cases = [
    ("🎯", "#02C39A", "Targeted Marketing", "Personalize campaigns by engagement level instead of one-size-fits-all blasts."),
    ("⚠️", "#E4572E", "Churn Risk & Retention", "Catch at-risk users early with proactive win-back offers."),
    ("🧩", "#028090", "Personalized Experience", "Tailor in-app features and notifications per segment."),
]
for col, (icon, color, title, body) in zip((uc1, uc2, uc3), use_cases):
    with col:
        st.markdown(
            f"""
            <div class="uc-card">
                <div class="uc-icon" style="background:{color}22;">{icon}</div>
                <h4>{title}</h4>
                <p>{body}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
st.info(
    "This app ships with a synthetic 50,000-user dataset that mirrors the "
    "project's schema and four expected behavior patterns. Upload your own "
    "CSV on the **Data Overview** page to run the same pipeline on real data.",
    icon="ℹ️",
)
