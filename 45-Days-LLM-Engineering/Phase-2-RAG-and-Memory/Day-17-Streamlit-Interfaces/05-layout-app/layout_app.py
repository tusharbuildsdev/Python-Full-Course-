import streamlit as st

st.title("Layout a page")

st.sidebar.header("Settings")

model = st.sidebar.selectbox("Model", ["llama", "OpenAi", "Gemini"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.5)
st.write(f"You picked **{model}** at temp : {temperature}")
st.header("Welcome to new page")


st.header("colls puts thing side by side")
coll, coll2, coll3 = st.columns(3)

with coll:
    st.write("Col 1 Content")
    st.metric("User", 1290, "+120")

with coll2:
    st.write("Col 2 Content")
    st.metric("Active Today", 120, "-8")

with coll3:
    st.write("Col 3 Content")
    st.metric("Signups", 57, "+15")


st.divider()
st.header("Tabs Act like mini page")
(
    tab_summary,
    tab_details,
) = st.tabs(["Summary", "Details"])

with tab_summary:
    st.write("This is summary tab")
with tab_details:
    st.write("This is details tab")


st.header("Expander hide long or optional content")
with st.expander("Click to see content"):
    st.code("You  are a helpful assistant", language="text")

show_debug = st.sidebar.checkbox(
    "Show Debug Info",
)
if show_debug:
    st.warning("Debug Mode is ON")
    st.json({"mode": model, "temperature": temperature})
