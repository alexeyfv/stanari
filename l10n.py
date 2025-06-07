"""Localization helpers"""

import gettext
import streamlit as st

LANG_LABELS = {
    "English": "en-US",
    "Sprski": "sr-Latn-RS",
    "Српски": "sr-Cyrl-RS",
    "Русский": "ru-RU",
}


def use_l10n(domain: str = "app"):
    """Allows to use localization"""
    if "lang" not in st.session_state:
        st.session_state["lang"] = "English"

    lang_code = LANG_LABELS[st.session_state["lang"]]
    translation = gettext.translation(
        domain, localedir="locales", languages=[lang_code]
    )
    translation.install()
    return translation.gettext
