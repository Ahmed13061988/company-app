import streamlit as st
from send_email import send_email
import pandas
st.header("Contact Us")

content = pandas.read_csv("topics.csv")

with st.form(key="my_form"):
    users_email = st.text_input("Your email")
    inquiry = st.selectbox("Select", options=(content["topic"]))
    email_body = st.text_area("Your message")
    button = st.form_submit_button("Submit")
    message = f"Topic: {inquiry}\n" \
              f"{email_body}\n" \
              f"From: {users_email}\n"
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")
