# App User Behavior Segmentation — Interactive Streamlit App

GUVI × HCL mini-project: an interactive, multi-page Streamlit app that segments
app users into behavioral groups using K-Means clustering, with EDA and
cluster visualizations built on Matplotlib and Seaborn.

## Design

Every page shares one visual system (`style.py`):

- **Palette** — navy/teal control-room base (`#0B2E33`, `#028090`) with the
  four segment colors (emerald, teal-green, coral, slate) reused everywhere,
  from the sidebar to the charts.
- **Type** — Manrope for headings, Inter for body text, JetBrains Mono for
  metrics and data.
- **Pipeline stepper** — the gradient header banner on pages 1–5 shows a
  numbered 1→5 stepper, since the pages are a real, order-dependent pipeline
  (clustering needs data loaded first, profiles need clustering run first).
- **Engagement Spectrum** — a recurring 4-color strip/legend (High → Moderate
  → Low/At-Risk → Occasional) that ties Home, Cluster Profiles, and Business
  Insights back to the same segment model.

Metrics, section headers, and charts are grouped into bordered "cards"
(`st.container(border=True)`) for a cleaner, dashboard-like layout.

## Pages

1. **Home** — project overview and quick stats.
2. **Data Overview** — generate a synthetic dataset (adjustable size / seed /
   missing-value rate) or upload your own CSV; inspect schema, summary
   stats, and missing-value cleaning.
3. **EDA** — feature distribution histograms, a correlation heatmap, and a
   two-feature scatter plot colored by engagement score.
4. **Clustering** — pick features, run the Elbow Method to choose *k*,
   fit K-Means, and view the PCA-projected cluster scatter plot with a
   live silhouette score.
5. **Cluster Profiles** — per-segment averages, a distribution pie chart,
   and side-by-side bar comparisons across chosen metrics.
6. **Business Insights** — segment → recommended-action mapping, plus CSV
   downloads (full dataset or a single segment).

## Run locally

```bash
pip install -r requirements.txt
streamlit run Home.py
```

Then open the URL Streamlit prints (typically http://localhost:8501).

## Using your own data

On the **Data Overview** page, switch the data source to "Upload CSV". Your
file should contain (at minimum) these numeric columns, used directly by the
clustering pipeline:

```
session_frequency, session_duration_minutes, engagement_score,
days_since_last_login, app_opens_per_day, notification_click_rate,
purchases_made, churn_risk_score
```

Everything downstream (EDA, clustering, profiling, exports) works unchanged
once these columns are present.

## Project structure

```
Home.py                        # landing page
style.py                       # shared design system (CSS, header, spectrum motif)
utils.py                       # synthetic data generator + shared helpers
.streamlit/config.toml         # theme colors
pages/
  1_Data_Overview.py
  2_EDA.py
  3_Clustering.py
  4_Cluster_Profiles.py
  5_Business_Insights.py
requirements.txt
```
