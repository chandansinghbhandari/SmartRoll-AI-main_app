import streamlit as st
# import pathlib

# BASE_DIR = pathlib.Path(__file__).parent.parent
# logo_url = str(BASE_DIR/ "static"/ "img"/"app_logo.png")

def header_home():

    from src.database.config import get_image_base64
    logo_url = get_image_base64("static/img/app_logo.png")
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>SmartRoll<br/>AI</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    from src.database.config import get_image_base64
    logo_url = get_image_base64("static/img/app_logo.png")

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>SmartRoll<br/>AI</h2>
        </div>   
                
                """, unsafe_allow_html=True)
