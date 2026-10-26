
import streamlit as st

st.set_page_config(
    page_title="Budget Calculator",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Monthly Budget Calculator")
st.write("Calculate your income, expenses, and remaining balance.")

currency = st.selectbox(
    "Currency",
    ["PKR", "USD", "GBP", "EUR"]
)

income = st.number_input(
    "Monthly Income",
    min_value=0.0,
    value=50000.0,
    step=1000.0
)

st.subheader("Monthly Expenses")

rent = st.number_input("Rent", min_value=0.0, value=10000.0)
food = st.number_input("Food", min_value=0.0, value=8000.0)
transport = st.number_input("Transport", min_value=0.0, value=3000.0)
utilities = st.number_input("Utilities", min_value=0.0, value=2000.0)
other = st.number_input("Other Expenses", min_value=0.0, value=1000.0)

expenses = rent + food + transport + utilities + other
balance = income - expenses

st.divider()
st.subheader("Budget Summary")

st.metric("Monthly Income", f"{currency} {income:,.2f}")
st.metric("Total Expenses", f"{currency} {expenses:,.2f}")
st.metric("Remaining Balance", f"{currency} {balance:,.2f}")

if income > 0:
    st.metric(
        "Remaining Balance (%)",
        f"{balance / income * 100:.1f}%"
    )

if balance < 0:
    st.error("Your expenses exceed your income.")
else:
    st.success("Your expenses are within your income.")
