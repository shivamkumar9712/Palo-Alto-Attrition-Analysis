import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Workforce Attrition Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Workforce Attrition Patterns and Risk Hotspot Analysis")

df = pd.read_csv("C:/Users/Shivam Kumar/Desktop/English/jbooks/.venv/New folder/Palo Alto Networks.csv")

st.subheader("Dataset Preview")

st.dataframe(df.head())

st.write("Number of employees:", len(df))
st.write("Number of columns:", len(df.columns))

# Add first KPI

total_employees = len(df)

total_exited = int(df["Attrition"].sum())

total_retained = total_employees - total_exited

attrition_rate = (
    total_exited / total_employees * 100
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Employees",
    total_employees
)

col2.metric(
    "Employees Exited",
    total_exited
)

col3.metric(
    "Employees Retained",
    total_retained
)

col4.metric(
    "Attrition Rate",
    f"{attrition_rate:.2f}%"
)

# Add a chart

import plotly.express as px

department_attrition = (
    df.groupby("Department")["Attrition"]
    .mean()
    .mul(100)
    .reset_index(name="AttritionRate")
)

fig = px.bar(
    department_attrition,
    x="Department",
    y="AttritionRate",
    title="Attrition Rate by Department",
    text_auto=".1f"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# Add sidebar filters

st.sidebar.title("🔎 Filters")

departments = st.sidebar.multiselect(
    "Department",
    df["Department"].unique(),
    default=df["Department"].unique()
)

overtime = st.sidebar.multiselect(
    "Overtime",
    df["OverTime"].unique(),
    default=df["OverTime"].unique()
)

filtered_df = df[
    (df["Department"].isin(departments)) &
    (df["OverTime"].isin(overtime))
]

st.write("Filtered Employees:", len(filtered_df))