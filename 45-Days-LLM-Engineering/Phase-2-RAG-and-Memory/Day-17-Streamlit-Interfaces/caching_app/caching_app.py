import time
import streamlit as st

st.title("Caching:run slow work once , not every rerun")


def slow_uncached(n):
    time.sleep(2)
    return n * n


@st.cache_data
def slow_cached(n):
    time.sleep(2)
    return n * n


st.header("Uncached: slow every single time")
number1 = st.slider("Pick a number (uncached)", 1, 10, 3)
if st.button("Square it (uncached)"):
    result = slow_uncached(number1)
    st.success(f"{number1} squared is {result}")

st.divider()

st.header("Cached: slow once per value, then instant")
number2 = st.slider("Pick a number (cached)", 1, 10, 3)

if st.button("Square it (cached)"):
    result = slow_cached(number2)
    st.success(f"{number2} squared is {result}")

st.caption(
    "Try clicking 'cached' with the same number twice: the second click is instant. "
    "Then change the number and click again: slow once more (a new cache entry)."
)

st.divider()
