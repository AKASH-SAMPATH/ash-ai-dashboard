import streamlit as st
import requests
import google.generativeai as genai
import pandas as pd
import numpy as np  
from streamlit_lottie import st_lottie

st.set_page_config(page_title="ASH AI Dashboard", page_icon="🤖", layout="wide")
genai.configure(api_key="AIzaSyCoHJ_lFwbZaUdiiG6EKE5p_vVbSBpfjSY")
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

robot_animation = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_ydo1amjm.json") 
st.markdown("<h1 style='text-align: center; color: cyan;'>🤖 Welcome to ASH AI Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: white;'>Your Smart AI Assistant for Data & Insights</h3>", unsafe_allow_html=True)
if robot_animation:
    st_lottie(robot_animation, height=250, key="robot")
else:
    st.warning("⚠️ Failed to load animation. Check Lottie URL.")

st.subheader("Ask ASH Anything!")
user_input = st.text_input("Enter a question for ASH:", placeholder="think and ask....")
def get_gemini_response(query):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(query)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {e}"

if st.button("Generate AI Response"):
    if user_input:
        with st.spinner("🤖 ASH is thinking..."):
            ai_response = get_gemini_response(user_input)
        st.success("✅ Response Generated!")
        st.markdown(f"**🧠 ASH Says:**\n\n{ai_response}")
    else:
        st.warning("⚠️ Please enter a question before generating a response.")

st.subheader("📊 Live Dashboard Data")
data = pd.DataFrame({
    "Timestamp": pd.date_range(start="2025-02-18 21:40:28", periods=10, freq="T"),
    "Metric A": [round(x, 2) for x in list(np.random.rand(10))],  
    "Metric B": [round(x, 2) for x in list(np.random.rand(10))],  
})

st.dataframe(data)

st.markdown("---")
st.markdown("<h5 style='text-align: center; color: lightgray;'>🚀 Powered by ASH'S AI | Built with ❤️ by Akash Sampath</h5>", unsafe_allow_html=True)
