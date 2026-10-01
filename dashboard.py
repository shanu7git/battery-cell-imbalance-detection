import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Battery Cell Imbalance Detection",
    layout="wide"
)

st.title("🔋 Battery Cell Imbalance Detection")

conn = sqlite3.connect("battery.db")

df = pd.read_sql_query(
    "SELECT * FROM battery_data ORDER BY id DESC",
    conn
)

conn.close()

if df.empty:

    st.warning("No battery data available.")

else:

    latest = df.iloc[0]

    st.subheader("Current Battery Status")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Cell 1", f"{latest['cell1']:.3f} V")
    col2.metric("Cell 2", f"{latest['cell2']:.3f} V")
    col3.metric("Cell 3", f"{latest['cell3']:.3f} V")
    col4.metric("Cell 4", f"{latest['cell4']:.3f} V")

    st.metric(
        "Voltage Difference",
        f"{latest['voltage_difference']:.3f} V"
    )

    st.metric(
        "Temperature",
        f"{latest['temperature']:.2f} °C"
    )

    st.metric(
        "SOC",
        f"{latest['soc']:.1f}%"
    )

    if latest["status"] == "IMBALANCE":

        st.error("⚠️ BATTERY CELL IMBALANCE DETECTED")

    else:

        st.success("✅ BATTERY CELLS BALANCED")

    st.subheader("Cell Voltage")

    voltage_df = df.head(50).sort_values("id")

    fig = px.line(
        voltage_df,
        x="timestamp",
        y=["cell1", "cell2", "cell3", "cell4"],
        title="Cell Voltage vs Time"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Temperature")

    fig2 = px.line(
        voltage_df,
        x="timestamp",
        y="temperature",
        title="Battery Temperature"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Voltage Difference")

    fig3 = px.line(
        voltage_df,
        x="timestamp",
        y="voltage_difference",
        title="Cell Voltage Difference"
    )

    st.plotly_chart(fig3, use_container_width=True)