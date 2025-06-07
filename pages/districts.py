import os
import folium
import pandas as pd
import psycopg
import streamlit as st
from branca.colormap import linear
from streamlit_folium import st_folium
from l10n import use_l10n

_ = use_l10n("districts")

DB_URL = os.getenv("DATABASE_URL")


@st.cache_data
def get_geojson(url):
    """Gets the GeoJSON data for districts"""
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select d.slug, d.geojson 
                from districts d 
                """
            )

            return cur.fetchall()


@st.cache_data
def get_prices(url):
    """Gets all the prices for districts"""
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                select district_id, district_name, price 
                from districts_prices_daily
                """
            )

            return pd.DataFrame(
                cur,
                columns=["district_id", "district_name", "price"],
            )


@st.cache_data
def get_medians(url, rooms: list[int], area_min: int, area_max: int):
    with psycopg.connect(url) as conn:
        with conn.cursor() as cur:
            cur.execute(
                """
                SELECT 
                    district_id, 
                    district_name,
                    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY price) AS median_price
                FROM districts_prices_dataset
                WHERE rooms = ANY(%s) AND area BETWEEN %s AND %s
                GROUP BY district_id, district_name;
                """,
                (rooms, area_min, area_max),
            )

            return pd.DataFrame(
                cur.fetchall(),
                columns=["district_id", "district_name", "median_price"],
            )


# Page title
st.title(_("districts_title"))

# Filters
with st.sidebar:

    st.subheader(_("districts_filters_subheader"))

    rooms_titles = [
        _("studio"),
        _("1room"),
        _("2room"),
        _("3room"),
        _("4room"),
        _("5room"),
    ]

    selected_rooms = st.pills(
        _("rooms"),
        options=[0, 1, 2, 3, 4, 5],
        default=1,
        selection_mode="multi",
        format_func=lambda x: rooms_titles[x],
    )

    if not selected_rooms:
        st.warning(_("no_rooms_warnings"))
        st.stop()
    (area_min, area_max) = st.slider(
        _("area"), min_value=5, max_value=500, value=(35, 55)
    )

# Fetch data
geo_jsons = get_geojson(DB_URL)
df_medians = get_medians(DB_URL, selected_rooms, area_min, area_max)
df = get_prices(DB_URL)

# Map
# Group median by district
medians = df_medians.groupby("district_name")["median_price"].median().to_dict()

# Prepare color map
price_min = min(medians.values())
price_max = max(medians.values())
colormap = linear._colormaps["YlOrRd_09"].scale(price_min, price_max)

# Создание карты
m = folium.Map(location=[44.81777, 20.45671], zoom_start=12, attributionControl=0)

for slug, geo_json in geo_jsons:
    price = medians.get(slug)

    folium.GeoJson(
        geo_json,
        name=slug,
        tooltip=f"{slug}<br>€{price:.0f}" if price else slug,
        style_function=lambda feature, price=price: {
            "fillColor": colormap(price) if price else "#cccccc",
            "color": "black",
            "weight": 1,
            "fillOpacity": 0.6,
        },
    ).add_to(m)

colormap.add_to(m)
st_folium(m, height=500, use_container_width=True, returned_objects=[])
