#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

import os
import streamlit as st
from openai import OpenAI

# Import tab modules
from tabs import legal_consulting

def main():
    # 1. Configure page layout and title
    st.set_page_config(page_title="Ferrosa ", layout="centered")
    st.title("FAMILY SUPPORT -FERROSA")

    # 2. Load API keys from secrets or environment variables with error handling
    try:
        api_key = st.secrets.get("OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found in Streamlit secrets or environment variables.")
        client = OpenAI(api_key=api_key)
    except Exception as e:
        st.error(f"Failed to initialize OpenAI client: {e}")
        return

    try:
        groq_key = st.secrets.get("GROQ_KEY")
        if not groq_key:
            raise ValueError("Groq API key not found in Streamlit secrets.")
        os.environ["GROQ_API_KEY"] = groq_key
    except Exception as e:
        st.error(f"Failed to set Groq API key: {e}")
        return

    # 3. Initialize session state for model selection and message history
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "o4-mini-2025-04-16"
    if "messages" not in st.session_state:
        st.session_state["messages"] = {}

    # 4. Sidebar or main section radio button for selecting legal help type
    label_map = {
        "Family support ":   legal_consulting,

    }

    choice = st.radio(" Wecome to Ferrosa", list(label_map.keys()))

    # 5. Load and run the appropriate module's render() method
    module = label_map[choice]
    module.render(client)

# Run main only when this script is executed directly
if __name__ == "__main__":
    main()
