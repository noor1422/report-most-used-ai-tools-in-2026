import streamlit as st
import pandas as pd
import plotly.express as px

# عنوان الصفحة
st.set_page_config(page_title="AI Tools Report", layout="wide")

st.title(" 🤖  Statistical Report: Most Used AI Tools in 2026")
st.markdown("This report presents the most popular Artificial Intelligence tools currently used worldwide.")

# البيانات
data = {
    "AI Tool": [
        " ChatGPT",
        "Google Gemini",
        "Microsoft Copilot",
        "Claude",
        "Perplexity",
        "Midjourney",
        "GitHub Copilot"
    ],
    "Estimated Usage (%)": [38, 18, 15, 10, 8, 6, 5]
}

df = pd.DataFrame(data)

# عرض الجدول
st.subheader("AI Tools Usage Table")
st.dataframe(df, use_container_width=True)

# مؤشرات
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Most Used Tool", "ChatGPT")

with col2:
    st.metric("Number of Tools", len(df))

with col3:
    st.metric("Top Usage", "38%")

# رسم بياني عمودي
st.subheader("Usage Distribution")

fig = px.bar(
    df,
    x="AI Tool",
    y="Estimated Usage (%)",
    text="Estimated Usage (%)",
    color="Estimated Usage (%)"
)

st.plotly_chart(fig, use_container_width=True)

# رسم دائري
st.subheader("Market Share")

pie = px.pie(
    df,
    names="AI Tool",
    values="Estimated Usage (%)"
)

st.plotly_chart(pie, use_container_width=True)

# استنتاج
st.subheader("Key Findings")

st.success("""
• ChatGPT is the most widely used AI tool.
• Gemini and Copilot are strong competitors.
• AI-powered coding assistants are becoming increasingly popular.
• Generative AI tools dominate the current market.
""")

# معلومات إضافية
with st.expander("About the Report"):
    st.write("""
    This report provides an educational overview of the most popular AI tools
    based on current market trends and public adoption.
    """)
