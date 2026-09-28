import streamlit as st
import plotly.express as px
import pandas as pd
st.set_page_config(page_title="PocketSmart AI", page_icon="💰")
st.title("💰 PocketSmart AI")
st.subheader("Your Smart Budget Assistant")
income = st.sidebar.number_input("Monthly Income ₹", value=30000)
food = st.sidebar.number_input("Food", value=8000)
transport = st.sidebar.number_input("Transport", value=3000)
shopping = st.sidebar.number_input("Shopping", value=5000)
entertainment = st.sidebar.number_input("Entertainment", value=4000)
bills = st.sidebar.number_input("Bills & Rent", value=6000)
expenses = {"Food": food, "Transport": transport, "Shopping": shopping, "Entertainment": entertainment, "Bills": bills}
total = sum(expenses.values())
savings = income - total
st.metric("Savings Left", f"₹{savings}", f"{(savings/income*100) if income>0 else 0:.1f}%")
df = pd.DataFrame(list(expenses.items()), columns=["Category", "Amount"])
fig = px.pie(df, values="Amount", names="Category", hole=0.4)
st.plotly_chart(fig)
if savings < income*0.2:
    st.warning(f"Save only {savings/income*100:.1f}%. Cut {max(expenses, key=expenses.get)}!")
else:
    st.success("Excellent! You are saving well!"); st.balloons()
