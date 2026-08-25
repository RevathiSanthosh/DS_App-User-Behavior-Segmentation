"""
Shared visual design system for the App User Behavior Segmentation app.

One cohesive look across all six pages: a navy/teal control-room palette,
Manrope + Inter + JetBrains Mono type, a numbered pipeline stepper (the
pages genuinely run in sequence — cluster assignments depend on data
loaded upstream), and a recurring "Engagement Spectrum" bar — a 4-color
strip (High -> Moderate -> Low/At-Risk -> Occasional) that echoes the
segment palette used throughout the charts.
"""

import streamlit as st

# ---------------------------------------------------------------- tokens
NAVY = "#0B2E33"
NAVY_DEEP = "#071E22"
TEAL = "#028090"
EMERALD = "#02C39A"      # High Engagement
TEAL_GREEN = "#00A896"   # Moderate Engagement
CORAL = "#E4572E"        # Low Engagement / At-Risk
SLATE = "#7E9497"        # Occasional Users
BG = "#F5F8F9"
CARD = "#FFFFFF"
INK = "#10262B"
MUTED = "#5B6B6E"

SPECTRUM = [
    ("High", EMERALD),
    ("Moderate", TEAL_GREEN),
    ("Low / At-Risk", CORAL),
    ("Occasional", SLATE),
]

PIPELINE_STEPS = ["Data Overview", "EDA", "Clustering", "Cluster Profiles", "Business Insights"]


def inject_css():
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500;700;800&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600&display=swap');

        html, body, .stApp {{
            background-color: {BG};
            font-family: 'Inter', sans-serif;
            color: {INK};
        }}
        h1, h2, h3, h4, .app-h {{
            font-family: 'Manrope', sans-serif !important;
            letter-spacing: -0.01em;
            color: {NAVY} !important;
        }}
        [data-testid="stAppViewBlockContainer"] {{
            padding-top: 1.4rem;
            max-width: 1180px;
        }}

        /* ---------- sidebar ---------- */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {NAVY} 0%, {NAVY_DEEP} 100%);
        }}
        [data-testid="stSidebar"] * {{
            color: #E7F3F2 !important;
        }}
        [data-testid="stSidebarNav"] a {{
            border-radius: 8px;
            margin: 1px 6px;
        }}
        [data-testid="stSidebarNav"] a:hover {{
            background-color: rgba(2, 195, 154, 0.18);
        }}
        [data-testid="stSidebarNav"] a[aria-current="page"] {{
            background-color: rgba(2, 195, 154, 0.28);
            border-left: 3px solid {EMERALD};
        }}
        [data-testid="stSidebar"] hr {{ border-color: rgba(255,255,255,0.14); }}
        [data-testid="stSidebar"] .stSlider [data-baseweb="slider"] div div div {{ background: {EMERALD} !important; }}

        /* ---------- header banner ---------- */
        .app-banner {{
            background: linear-gradient(120deg, {NAVY} 0%, {TEAL} 130%);
            border-radius: 16px;
            padding: 22px 28px 18px 28px;
            margin-bottom: 22px;
            box-shadow: 0 6px 22px rgba(11,46,51,0.18);
        }}
        .app-banner .eyebrow {{
            color: #9FE8DC;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.72rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            margin-bottom: 2px;
        }}
        .app-banner h1 {{
            color: #FFFFFF !important;
            font-size: 1.7rem;
            margin: 0 0 4px 0;
        }}
        .app-banner p {{
            color: #D8ECE9;
            margin: 0;
            font-size: 0.94rem;
        }}

        /* ---------- spectrum motif ---------- */
        .spectrum-strip {{
            height: 6px;
            border-radius: 4px;
            margin-top: 14px;
            background: linear-gradient(90deg, {EMERALD} 0% 25%, {TEAL_GREEN} 25% 50%, {CORAL} 50% 75%, {SLATE} 75% 100%);
        }}
        .spectrum-legend {{ display: flex; gap: 18px; flex-wrap: wrap; margin: 6px 0 4px 0; }}
        .spectrum-legend .dot-label {{ display: flex; align-items: center; gap: 6px; font-size: 0.84rem; color: {MUTED}; }}
        .spectrum-legend .dot {{ width: 10px; height: 10px; border-radius: 50%; display: inline-block; }}

        /* ---------- pipeline stepper ---------- */
        .stepper {{ display: flex; align-items: center; margin-top: 16px; }}
        .step {{ display: flex; align-items: center; gap: 8px; }}
        .step .num {{
            width: 24px; height: 24px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 600;
            border: 1.5px solid rgba(255,255,255,0.55); color: #DDEFEC; flex-shrink: 0;
        }}
        .step.done .num {{ background: {EMERALD}; border-color: {EMERALD}; color: {NAVY_DEEP}; }}
        .step.current .num {{ background: #FFFFFF; border-color: #FFFFFF; color: {NAVY}; }}
        .step .label {{ font-size: 0.78rem; color: #C9E6E1; white-space: nowrap; }}
        .step.current .label {{ color: #FFFFFF; font-weight: 600; }}
        .step-line {{ flex: 1; height: 1.5px; background: rgba(255,255,255,0.3); margin: 0 8px; min-width: 10px; }}

        /* ---------- metrics as cards ---------- */
        [data-testid="stMetric"] {{
            background: {CARD};
            border-radius: 12px;
            padding: 14px 16px 10px 16px;
            border: 1px solid #E4ECEB;
            border-top: 3px solid {TEAL};
            box-shadow: 0 2px 10px rgba(11,46,51,0.05);
        }}
        [data-testid="stMetricValue"] {{
            font-family: 'JetBrains Mono', monospace;
            color: {NAVY};
        }}
        [data-testid="stMetricLabel"] {{ color: {MUTED}; }}

        /* ---------- bordered containers as cards ---------- */
        [data-testid="stVerticalBlockBorderWrapper"] {{
            border-radius: 14px !important;
            box-shadow: 0 2px 12px rgba(11,46,51,0.06);
        }}

        /* ---------- buttons ---------- */
        .stButton button, .stDownloadButton button {{
            background: linear-gradient(120deg, {TEAL}, {EMERALD});
            color: white;
            border: none;
            border-radius: 9px;
            font-weight: 600;
            transition: filter 0.15s ease;
        }}
        .stButton button:hover, .stDownloadButton button:hover {{
            filter: brightness(1.08);
            color: white;
        }}

        /* ---------- alerts ---------- */
        [data-testid="stAlert"] {{ border-radius: 10px; }}

        /* ---------- tabs ---------- */
        .stTabs [data-baseweb="tab"] {{
            font-family: 'Manrope', sans-serif;
            font-weight: 600;
        }}
        .stTabs [aria-selected="true"] {{ color: {TEAL} !important; }}

        /* ---------- dataframe ---------- */
        [data-testid="stDataFrame"] {{ border-radius: 10px; overflow: hidden; }}

        /* ---------- use-case / segment cards ---------- */
        .uc-card {{
            background: {CARD}; border-radius: 12px; padding: 16px;
            border: 1px solid #E4ECEB; height: 100%;
        }}
        .uc-card .uc-icon {{
            width: 34px; height: 34px; border-radius: 9px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.05rem; margin-bottom: 8px;
        }}
        .uc-card h4 {{ margin: 0 0 6px 0; font-size: 0.98rem; color: {NAVY} !important; }}
        .uc-card p {{ margin: 0; font-size: 0.86rem; color: {MUTED}; }}

        .seg-pill {{
            border-radius: 10px; padding: 12px 14px; color: white; margin-bottom: 6px;
        }}
        .seg-pill b {{ font-size: 0.95rem; }}
        .seg-pill span {{ font-size: 0.8rem; opacity: 0.92; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def page_header(icon: str, title: str, subtitle: str, step: int | None = None, eyebrow: str = "GUVI x HCL MINI-PROJECT"):
    """Gradient banner with the spectrum motif, and an optional pipeline stepper (1-indexed)."""
    stepper_html = ""
    if step is not None:
        parts = []
        for i, name in enumerate(PIPELINE_STEPS, start=1):
            cls = "done" if i < step else ("current" if i == step else "")
            mark = "&#10003;" if i < step else str(i)
            parts.append(f'<div class="step {cls}"><div class="num">{mark}</div><div class="label">{name}</div></div>')
            if i != len(PIPELINE_STEPS):
                parts.append('<div class="step-line"></div>')
        stepper_html = f'<div class="stepper">{"".join(parts)}</div>'

    st.markdown(
        f"""
        <div class="app-banner">
            <div class="eyebrow">{eyebrow}</div>
            <h1>{icon} {title}</h1>
            <p>{subtitle}</p>
            {stepper_html}
            <div class="spectrum-strip"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def spectrum_legend():
    dots = "".join(
        f'<div class="dot-label"><span class="dot" style="background:{color}"></span>{label} Engagement</div>'
        if label not in ("Low / At-Risk", "Occasional")
        else f'<div class="dot-label"><span class="dot" style="background:{color}"></span>{label}</div>'
        for label, color in SPECTRUM
    )
    st.markdown(f'<div class="spectrum-legend">{dots}</div>', unsafe_allow_html=True)
