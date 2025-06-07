"""Main page"""

import os
import psycopg
import streamlit as st
import pandas as pd
import altair as alt
from l10n import use_l10n

_ = use_l10n("main")

st.title(_("main_title"))  # 🏠 Stanari

st.subheader(_("main_subheader"))  # Serbian rental market analytics

# Database connection
DB_URL = os.getenv("DATABASE_URL")


@st.cache_data
def get_dashboard_stats():
    """Overview stats"""

    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select date, total_listings, p05, p50, p95
                from selected_date, dashboard_stats_daily
                """
            )

            result = cur.fetchone()

            return pd.DataFrame(
                [
                    {
                        "date": result[0],
                        "total_listings": result[1],
                        "p05": result[2],
                        "p50": result[3],
                        "p95": result[4],
                    }
                ]
            )


@st.cache_data
def get_room_prices():
    """Get median prices per room type"""
    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select rooms, median_price
                from dashboard_median_prices
                """
            )

            result = cur.fetchall()

            df = pd.DataFrame(result, columns=["rooms", "median_price"])
            df["title"] = df["rooms"].map(
                {
                    0: "Studio",
                    1: "1 Room",
                    2: "2 Rooms",
                    3: "3 Rooms",
                    4: "4 Rooms",
                    5: "5+ Rooms",
                }
            )

            return df


# Get all stats in one query
df_stats = get_dashboard_stats()

date = df_stats["date"][0]
total_listings = int(df_stats["total_listings"][0])
min_price = int(df_stats["p05"][0])
median = int(df_stats["p50"][0])
max_price = int(df_stats["p95"][0])

# Key metrics
col1, col2, col3, col4 = st.columns([1, 1, 2, 2])
with col1:
    st.metric(_("active_listings"), f"{total_listings}")
with col2:
    st.metric(_("median_price"), f"€{median}")
with col3:
    st.metric(_("price_range"), f"€{min_price} - €{max_price}")
with col4:
    st.metric(_("last_updated"), date.strftime("%d %b %Y"))

# Main sections
left_col, right_col = st.columns([1, 1])

with left_col:
    st.markdown(_("description"))

with right_col:
    # Room prices chart
    st.markdown(_("medians_by_size"))  #
    df_stats = get_room_prices()
    chart = (
        alt.Chart(df_stats)
        .mark_bar()
        .encode(
            x=alt.X("median_price").title(_("x_median_price")),
            y=alt.Y("title").title("").sort("-x"),
            text="median_price",
        )
    )
    chart = chart + chart.mark_text(align="left", dx=3)
    st.altair_chart(chart, use_container_width=True)
