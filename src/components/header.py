import streamlit as st
import base64

def header_home():

    with open("snap27.jpeg", "rb") as f:
        img_data = base64.b64encode(f.read()).decode()
    
    st.markdown(f"""
    <div style='diplay:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px;'>
        <img src='data:image/png;base64,{img_data}' style='height:100px; padding-left:280px; ' />
        <h1 style='text-align:center; color: #E0E3FF' >SNAP </br> CLASS</h1>
    </div>
    """, unsafe_allow_html=True)



def header_dashboard():
    with open("snap27.jpeg", "rb") as f:
        img_data = base64.b64encode(f.read()).decode()

    st.markdown(f"""\
<div style='display:flex; align-items:center; gap:10px;'>
    <img src='data:image/png;base64,{img_data}' style='height:95px;' />
    <h2 style='color: #5865F2; margin:0; white-space: nowrap;'>SNAP<br>CLASS</h2>
</div>
""", unsafe_allow_html=True)
