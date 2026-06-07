import streamlit as st

import base64
import os

from supabase import create_client, Client

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)


def get_image_base64(image_path):
    try:
        with open(image_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        ext = os.path.splitext(image_path)[1][1:]  # gets png/jpg
        return f"data:image/{ext};base64,{data}"
    except:
        return ""