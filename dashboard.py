import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="🎓 Student Performance Dashboard")

df = pd.read_csv("marks.csv")

df["Total"] = df[['Math', 'Science', 'English', 'History']].sum(axis=1)
df["Average"] = df["Total"] / 4
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

student_filter = st.sidebar.multiselect(
    "Select Students",
    options=df["Name"].unique(),
    default=df["Name"].unique()
)

filtered_df = df[df["Name"].isin(student_filter)]

st.title("🎓 Student Performance Dashboard")
st.write("An interactive dashboard built with Streamlit and Pandas.")


st.subheader("📋 Student Details")
st.dataframe(filtered_df[['Name', 'Math', 'Science', 'English', 'History', 'Total', 'Average', 'Result']])

st.subheader("📊 Summary Metrics")
col1, col2 = st.columns(2)
col1.metric("Total Students", len(filtered_df))
col2.metric("Pass Rate", f"{(filtered_df['Result'] == 'Pass').mean() * 100:.2f}%")

st.subheader("📈 Average Marks Bar Chart")
fig, ax = plt.subplots()
ax.bar(filtered_df["Name"], filtered_df["Average"], color='skyblue')
ax.set_ylabel("Average Score")
ax.set_xlabel("Student")
st.pyplot(fig)
