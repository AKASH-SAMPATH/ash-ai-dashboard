import streamlit as st
import plotly.express as px
from ai_agent import AIDashboardAgent

st.set_page_config(layout="wide")
agent = AIDashboardAgent("sample_data.csv")
df, insights = agent.run()
st.title("AI-Powered Dashboard ")
st.subheader("AI-Generated Insights ")
st.write(insights)
if df is not None:
    
    fig = px.line(df, x="Date", y="Sales", title="Sales Over Time")
    st.plotly_chart(fig, use_container_width=True)
    st.subheader("Raw Data 📑")
    st.dataframe(df)
else:
    st.error("Failed to fetch data!")
