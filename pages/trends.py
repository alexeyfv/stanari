"""Trends page"""

import os
import pandas as pd
import psycopg
import streamlit as st
import altair as alt
from l10n import use_l10n

_ = use_l10n("trends")

DB_URL = os.getenv("DATABASE_URL")

st.title(_("trends"))


@st.cache_data
def by_date():

    with psycopg.connect(DB_URL) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select rooms, date, count, median_price
                from trends_stats_by_day
                """
            )

            result = cur.fetchall()

            df = pd.DataFrame(result, columns=["rooms", "date", "count", "price"])

            return df


df_by_date = by_date()

df_by_date["title"] = df_by_date["rooms"].map(
    {
        0: _("studio"),
        1: _("1room"),
        2: _("2room"),
        3: _("3room"),
        4: _("4room"),
        5: _("5room"),
    }
)

col1, col2 = st.columns(2)

with col1:

    st.subheader(_("price_trends"))  # Price trends
    prices = (
        alt.Chart(df_by_date)
        .mark_line(
            interpolate="monotone",
            strokeWidth=3,
            point=alt.OverlayMarkDef(filled=False, fill="white"),
        )
        .encode(
            x=alt.X("date:T").title(_("date")),  # Date
            y=alt.Y("price:Q").title(_("price")),  # Price (€)
            color=alt.Color(
                "title:N",
                title=_("rooms"),  # Rooms
                legend=alt.Legend(orient="bottom"),
            ),
        )
        .properties(height=400)
    )

    st.altair_chart(prices, use_container_width=True)

with col2:

    st.subheader(_("listings_count_trends"))  # Listingcs count trends
    counts = (
        alt.Chart(df_by_date)
        .mark_line(
            interpolate="monotone",
            strokeWidth=3,
            point=alt.OverlayMarkDef(filled=False, fill="white"),
        )
        .encode(
            x=alt.X("date:T").title(_("date")),
            y=alt.Y("count:Q").title(_("price")),
            color=alt.Color(
                "title:N",
                title=_("rooms"),
                legend=alt.Legend(orient="bottom"),
            ),
        )
        .properties(height=400)
    )

    st.altair_chart(counts, use_container_width=True)
