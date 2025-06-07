"""Help page"""

import streamlit as st
from l10n import use_l10n

_ = use_l10n("help")

st.header(_("help_title"))  # "How to read the visualizations"

tab1, tab2 = st.tabs([_("boxplot_title"), _("heatmap_title")])  # Box Plot, Heatmap

with tab1:
    st.markdown(_("boxplot_description"))
    # """

    # """

with tab2:
    st.markdown(_("heatmap_description"))
"""
"""
