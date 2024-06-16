# pip install streamlit
# to run the Streamlit server open a terminal an run this:
# streamlit run Likert_streamlit.py


import streamlit as st
import plot_likert

# Define the questions
questions = [
    "I find the interface of this app easy to use.",
    "The content provided by this app is useful.",
    "I would recommend this app to others."
]

# Define the Likert scale
scale = plot_likert.scales.agree5

# Create a dictionary to store the responses
responses = {}

# Display the questions and the Likert scale
for question in questions:
    responses[question] = st.selectbox(question, options=scale)

# Display the text field for comments
comments = st.text_area("Any additional comments?")

# When the submit button is pressed, print the responses and the comments
if st.button('Submit'):
    st.write("Responses:")
    for question, response in responses.items():
        st.write(f"{question}: {response}")
    st.write("Comments:")
    st.write(comments)

