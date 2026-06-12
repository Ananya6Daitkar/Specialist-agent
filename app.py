import streamlit as st
from Specialist_agent import SpecialistAgent

st.title("Specialist Pricing Agent")

product = st.text_input("Enter Product Name")

if st.button("Get Price"):

    agent = SpecialistAgent()

    price = agent.price(product)

    st.write(f"Estimated Price: ₹{price}")