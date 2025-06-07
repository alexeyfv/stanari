"""About"""

import streamlit as st
from l10n import use_l10n

_ = use_l10n("about")

st.title(_("about_title"))

st.markdown(_("about_content"))
