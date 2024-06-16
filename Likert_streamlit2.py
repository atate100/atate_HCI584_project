# pip install streamlit
# to run the Streamlit server open a terminal an run this:
# streamlit run Likert_streamlit2.py

import streamlit as st
import plot_likert
import pandas as pd
import matplotlib.pyplot as plt

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

# Display a label Name with a text input
name = st.text_input("Name", "Your name")

# Display the questions and the Likert scale
for question in questions:
    responses[question] = st.radio(question, options=scale, index=2) # start at neutral

# Display the text field for comments
comments = st.text_area("Any additional comments?")

# When the submit button is pressed, print the responses and the comments
if st.button('Submit'):
    st.write(f"Name: {name}")
    st.write("Responses:")
    for question, response in responses.items():
        st.write(f"{question}: {response}")
    st.write("Comments:")
    st.write(comments)

# Saving the results

# open csv file in append mode ("a")
#with open("survey.csv", "a") as fo:

    # make a comma separate string with name, question1, etc: (no spaces!)
    # ex: record = "Chris,All of the time,Not very often, ...,Liked the room a lot!"
    # print() string into fo
    #print(record, file = fo)