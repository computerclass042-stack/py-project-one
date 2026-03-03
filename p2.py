import streamlit as st

st.title("My Python Quiz & Calculator")

# Input lene ke liye Streamlit ke buttons ya text_input use karo
name = st.text_input("Aapka Naam kya hai?")
if name:
    st.write(f"Hello {name}, welcome to my project!")

# Example Calculator logic
num1 = st.number_input("Pehla Number daalein", value=0)
num2 = st.number_input("Doosra Number daalein", value=0)

if st.button("Add Karo"):
    result = num1 + num2
    st.success(f"Answer hai: {result}")
