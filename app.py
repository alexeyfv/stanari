"""Stanari"""

from dotenv import load_dotenv
import streamlit as st
from l10n import use_l10n, LANG_LABELS

load_dotenv()

_ = use_l10n("app")

pages = {
    _("overview"): [
        st.Page("pages/main.py", title=_("dashboard")),
    ],
    _("analysis"): [
        st.Page("pages/districts.py", icon="📊", title=_("by_districts")),
        st.Page("pages/rooms.py", icon="📐", title=_("by_apartment_size")),
        st.Page("pages/trends.py", icon="📈", title=_("trends")),
    ],
    _("help"): [
        st.Page("pages/help.py", icon="ℹ️", title=_("help")),
    ],
    _("about"): [
        st.Page("pages/about.py", icon="⭐️", title=_("about")),
    ],
}

st.set_page_config(
    page_title="Stanari",
    page_icon="🏠",
    layout="wide",
)

with st.sidebar:

    st.selectbox(
        label=":material/translate:",
        key="lang",
        options=LANG_LABELS.keys(),
        accept_new_options=False,
    )

    st.selectbox(
        label=_("data_source"),
        key="data_source",
        options=("nekretnine.rs"),
        accept_new_options=False,
    )

pg = st.navigation(pages, expanded=False)
pg.run()
