import streamlit as st
import plotly.express as px
from ai_agent import AIDashboardAgent

st.set_page_config(layout="wide")

# Instantiate AI Agent
agent = AIDashboardAgent("sample_data.csv")
df, insights = agent.run()

# Streamlit UI
st.title("AI-Powered Dashboard 📊")

# Display AI insights
st.subheader("AI-Generated Insights 🧠")
st.write(insights)

# Check if data is available
if df is not None:
    # Plot data trends
    fig = px.line(df, x="Date", y="Sales", title="Sales Over Time")
    st.plotly_chart(fig, use_container_width=True)
    
    # Show data table
    st.subheader("Raw Data 📑")
    st.dataframe(df)
else:
    st.error("Failed to fetch data!")
