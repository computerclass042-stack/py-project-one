import streamlit as st

# Page Configuration
st.set_page_config(page_title="Interest Calculator", page_icon="💰")

st.title("💰 Smart Interest Calculator")
st.write("Apne savings ya loan ka interest turant calculate karein.")

# Sidebar for User Info
st.sidebar.header("Developer Details")
st.sidebar.info("Anuj\nProfessional Intern at NGO") #

# Input Fields
col1, col2 = st.columns(2)
with col1:
    principal = st.number_input("Principal Amount (Rs.)", min_value=0.0, step=100.0, value=1000.0)
    rate = st.number_input("Interest Rate (% per year)", min_value=0.0, step=0.1, value=5.0)
with col2:
    time = st.number_input("Time Period (Years)", min_value=0.0, step=0.5, value=1.0)
    interest_type = st.selectbox("Interest Type", ["Simple Interest", "Compound Interest"])

# Calculation Logic
if st.button("Calculate Karein"):
    if interest_type == "Simple Interest":
        interest = (principal * rate * time) / 100
        total = principal + interest
    else:
        total = principal * (pow((1 + rate / 100), time))
        interest = total - principal

    # Result Display
    st.divider()
    st.subheader("Results:")
    st.success(f"Interest Amount: ₹{interest:,.2f}")
    st.info(f"Total Maturity Amount: ₹{total:,.2f}")

# Educational Note for Students
st.divider()
st.caption("Note: Ye calculator 6th aur 7th grade ke math concepts par based hai.") #


