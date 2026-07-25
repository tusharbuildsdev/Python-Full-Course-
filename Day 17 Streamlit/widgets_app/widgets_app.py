import streamlit as st

st.title("Widgets: Input you can read")
st.header("Tell me about yourself")
name = st.text_input("What is your name?", "")
age = st.slider("How old are you?", 0, 100, 20)
city = st.selectbox("Which city?", ["Delhi", "Mumbai", "Pune", "Chennai", "Other"])
st.write(f"Hi **{name or 'friend'}**,age:{age},city:{city}")


st.divider()
st.header("Live Tip Calculator")
bill = st.number_input("Bill Amount (Rs)", min_value=0.0, value=500.0, step=10.0)
tip_percentage = st.slider("Tip Percentage", 0, 30, 10)
tip = bill * tip_percentage / 100
total = bill + tip
st.metric("Total to pay", f"Rs {total:.2f}")
st.divider()
