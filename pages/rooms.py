"""Rooms page"""

import os
import pandas as pd
import psycopg
import streamlit as st
import altair as alt
from l10n import use_l10n

_ = use_l10n("rooms")

DB_URL = os.getenv("DATABASE_URL")

st.header(_("rooms_title"))
st.markdown(_("rooms_description"))


def box_plot(
    df: pd.DataFrame,
    xAxisTitle: str,
    dimension_name: str,
    dimensions: list[str],
    width: int,
    height: int,
):
    """Creates a box plot"""

    epsilon = 5

    df["p05_label"] = df["p05"].apply(lambda x: f"{x:.0f} €")
    df["p50_label"] = df["p50"].apply(lambda x: f"{x:.0f} €")
    df["p95_label"] = df["p95"].apply(lambda x: f"{x:.0f} €")

    df["p50_left"] = df["p50"] - epsilon
    df["p50_right"] = df["p50"] + epsilon

    range = (
        alt.Chart(df)
        .mark_bar(height=25, cornerRadius=5)
        .encode(
            x=alt.X("p05:Q").title(xAxisTitle),
            x2="p95:Q",
            y=alt.Y(f"{dimension_name}:N").title(None).sort(dimensions),
            tooltip=[],
        )
        .properties(height=height, width=width)
    )

    median = (
        alt.Chart(df)
        .mark_bar(height=20, cornerRadius=5, color="#ffffff")
        .encode(
            x=alt.X("p50_left:Q"),
            x2="p50_right",
            y=alt.Y(f"{dimension_name}:N").sort(dimensions),
            tooltip=[],
        )
        .properties(height=height, width=width)
    )

    p05_text = (
        alt.Chart(df)
        .mark_text(align="right", dx=-5)
        .encode(
            x="p05:Q",
            y=alt.Y(f"{dimension_name}:N").sort(dimensions),
            text="p05_label:N",
            tooltip=[],
        )
    )

    p90_text = (
        alt.Chart(df)
        .mark_text(align="left", dx=5)
        .encode(
            x="p95:Q",
            y=alt.Y(f"{dimension_name}:N").sort(dimensions),
            text="p95_label:N",
            tooltip=[],
        )
    )

    p50_text = (
        alt.Chart(df)
        .mark_text(align="center", dy=-20)
        .encode(
            x="p50:Q",
            y=alt.Y(f"{dimension_name}:N").sort(dimensions),
            text="p50_label:N",
            tooltip=[],
        )
    )

    plot = range + median + p05_text + p90_text + p50_text

    return plot


# Create tabs for all visualizations
tab_labels = [
    _("overview"),
    _("studio"),
    _("1room"),
    _("2room"),
    _("3room"),
    _("4room"),
    _("5room"),
]
tabs = st.tabs(tab_labels)


@st.cache_data
def get_overview_df():
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select rooms, p05, p50, p95
                from rooms_median_prices
                """
            )

            df = pd.DataFrame(
                cur,
                columns=["rooms", "p05", "p50", "p95"],
            )

            return df


@st.cache_data
def get_per_room_df():

    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select rooms, area, price
                from rooms_area_prices
                """
            )

            df = pd.DataFrame(cur, columns=["rooms", "area", "price"])

            return df


# First tab - Box plot
with tabs[0]:
    overview_df = get_overview_df()
    overview_df["title"] = overview_df["rooms"].map(
        {
            0: _("studio"),
            1: _("1room"),
            2: _("2room"),
            3: _("3room"),
            4: _("4room"),
            5: _("5room"),
        }
    )

    sort_order = [
        _("overview"),
        _("studio"),
        _("1room"),
        _("2room"),
        _("3room"),
        _("4room"),
        _("5room"),
    ]

    boxplot = box_plot(
        overview_df,
        _("price"),
        "title",
        sort_order,
        height=400,
        width=600,
    )

    st.altair_chart(boxplot, on_select="ignore", use_container_width=True)

# Heatmap tabs

per_room_df = get_per_room_df()

# Create and display heatmaps in tabs (skip first tab as it's for boxplot)
for i, tab in enumerate(tabs[1:], 0):  # start from 0 for room numbers
    with tab:
        df_filtered = per_room_df[per_room_df["rooms"] == i]
        chart = (
            alt.Chart(df_filtered)
            .mark_rect()
            .encode(
                alt.X("area:Q", title=_("area"), bin=alt.Bin(maxbins=20)),
                alt.Y("price:Q", title=_("price"), bin=alt.Bin(maxbins=20)),
                alt.Color(
                    "count():Q",
                    title=_("number_of_apartments"),
                    scale=alt.Scale(scheme="greenblue"),
                ),
            )
            .properties(height=400)
        )
        st.altair_chart(chart, use_container_width=True)
