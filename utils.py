"""
Shared utilities for the App User Behavior Segmentation Streamlit app.

Generates a synthetic app-user-behavior dataset (matching the schema described
in the GUVI x HCL project brief), plus small helpers used across pages.
"""

import numpy as np
import pandas as pd

FEATURE_COLS = [
    "session_frequency",
    "session_duration_minutes",
    "engagement_score",
    "days_since_last_login",
    "app_opens_per_day",
    "notification_click_rate",
    "purchases_made",
    "churn_risk_score",
]

FEATURE_LABELS = {
    "session_frequency": "Session Frequency",
    "session_duration_minutes": "Session Duration (min)",
    "engagement_score": "Engagement Score",
    "days_since_last_login": "Days Since Last Login",
    "app_opens_per_day": "App Opens / Day",
    "notification_click_rate": "Notification Click Rate",
    "purchases_made": "Purchases Made",
    "churn_risk_score": "Churn Risk Score",
}

SEGMENT_ACTIONS = {
    "High Engagement Users": "Loyalty programs, premium/upsell offers, referral incentives.",
    "Moderate Engagement Users": "Personalized nudges and feature recommendations to increase engagement.",
    "Low Engagement / At-Risk Users": "Proactive retention: win-back offers, reminders, improved onboarding.",
    "Occasional Users": "Re-engagement pushes tied to relevant triggers to bring sporadic users back.",
}

SEGMENT_COLORS = {
    "High Engagement Users": "#02C39A",
    "Moderate Engagement Users": "#00A896",
    "Low Engagement / At-Risk Users": "#E4572E",
    "Occasional Users": "#7E9497",
}


def _make_segment(n, rng, session_freq, session_dur, engagement, days_inactive,
                   opens_per_day, notif_ctr, purchases, churn):
    if n <= 0:
        return pd.DataFrame(columns=FEATURE_COLS)
    return pd.DataFrame({
        "session_frequency": rng.normal(session_freq, session_freq * 0.18, n).clip(0.2, None),
        "session_duration_minutes": rng.normal(session_dur, session_dur * 0.2, n).clip(0.5, None),
        "engagement_score": rng.normal(engagement, 6, n).clip(0, 100),
        "days_since_last_login": rng.normal(days_inactive, max(days_inactive * 0.3, 0.5), n).clip(0, None),
        "app_opens_per_day": rng.normal(opens_per_day, opens_per_day * 0.2, n).clip(0, None),
        "notification_click_rate": rng.normal(notif_ctr, 0.05, n).clip(0, 1),
        "purchases_made": rng.poisson(purchases, n),
        "churn_risk_score": rng.normal(churn, 8, n).clip(0, 100),
    })


def generate_synthetic_data(n_users: int = 50000, seed: int = 42, missing_frac: float = 0.02) -> pd.DataFrame:
    """Generate a synthetic app-user-behavior dataset with four latent
    behavioral archetypes, matching the project's expected schema."""
    rng = np.random.default_rng(seed)

    n_high = int(n_users * 0.22)
    n_mod = int(n_users * 0.33)
    n_low = int(n_users * 0.25)
    n_occ = n_users - n_high - n_mod - n_low

    high = _make_segment(n_high, rng, 18, 32, 88, 0.5, 9, 0.55, 4.0, 8)
    moderate = _make_segment(n_mod, rng, 9, 15, 60, 2.5, 4, 0.30, 1.5, 28)
    low = _make_segment(n_low, rng, 3, 6, 28, 12, 1.2, 0.10, 0.3, 68)
    occasional = _make_segment(n_occ, rng, 1.2, 4, 15, 25, 0.4, 0.05, 0.05, 55)

    df = pd.concat([high, moderate, low, occasional], ignore_index=True)
    df = df.sample(frac=1, random_state=seed).reset_index(drop=True)

    df.insert(0, "user_id", [f"U{100000 + i}" for i in range(len(df))])
    df["age"] = rng.integers(16, 65, len(df))
    df["gender"] = rng.choice(["Male", "Female", "Other"], len(df), p=[0.48, 0.48, 0.04])
    df["device_type"] = rng.choice(["Android", "iOS"], len(df), p=[0.68, 0.32])
    df["subscription_type"] = rng.choice(["Free", "Premium"], len(df), p=[0.78, 0.22])

    if missing_frac > 0:
        for col in ["session_duration_minutes", "engagement_score", "notification_click_rate"]:
            mask = rng.random(len(df)) < missing_frac
            df.loc[mask, col] = np.nan

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Impute missing numeric values with the column median."""
    df = df.copy()
    for col in ["session_duration_minutes", "engagement_score", "notification_click_rate"]:
        if col in df.columns and df[col].isnull().any():
            df[col] = df[col].fillna(df[col].median())
    return df


def label_clusters(profile: pd.DataFrame) -> dict:
    """Rank clusters by engagement_score and map to human-readable segment names."""
    ranked = profile.sort_values("engagement_score", ascending=False).index.tolist()
    names = ["High Engagement Users", "Moderate Engagement Users",
             "Low Engagement / At-Risk Users", "Occasional Users"]
    return {ranked[i]: names[i] for i in range(len(ranked))}
