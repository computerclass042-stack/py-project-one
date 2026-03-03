import streamlit as st

st.title("📏 Simple Unit Converter")
st.write("NGO Students ke liye asaan tool") #

# Sidebar for credit
st.sidebar.markdown("### Developer")
st.sidebar.info("Anuj\nNGO Intern") #

# Selection
option = st.selectbox("Kya convert karna hai?", ["Kilometers to Miles", "Celsius to Fahrenheit"])

# Logic
if option == "Kilometers to Miles":
    km = st.number_input("Enter Kilometers", value=1.0)
    miles = km * 0.621371
    st.success(f"{km} KM = {miles:.2f} Miles")

elif option == "Celsius to Fahrenheit":
    c = st.number_input("Enter Celsius", value=0.0)
    f = (c * 9/5) + 32
    st.success(f"{c}°C = {f:.2f}°F")
