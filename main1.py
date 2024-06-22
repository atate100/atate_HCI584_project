# pip install streamlit
# to run the Streamlit server open a terminal an run this:
# cd museum_wellbeing_survey
# streamlit run main.py

import streamlit as st
import plot_likert
import csv
import os
import numpy as np
import pandas as pd
import subprocess

import warnings

# Suppress FutureWarnings from plot_likert library
warnings.filterwarnings("ignore", category=FutureWarning, module="plot_likert")

if 'init_done' not in st.session_state:
# Define the questions
    questions = [
    "I felt happy.",
    "I felt engaged.",
    "I felt comfortable.",
    "I felt safe and secure.",
    "I enjoyed the company of other people.",
    "I talked to other people.",
]

# Define the header
header = ["Name"] + questions + ["Comments"]

# Define the Likert scale
scale = plot_likert.scales.agree5

# Create a dictionary to store the responses
responses = {}
print(responses)  # Debug

# check where the interpreter is "sitting", must be the root of the project
# To ensure this, you must open the project root folder(!) in VSCode and then
# start this file, not just load this file into the editor 
print("Current working directory:", os.getcwd())
print("files in data folder:", os.listdir("./data"))
file_path = "./data/wellbeing_survey.csv"

# Display a label Name with a text input
name = st.text_input("Name", "Your name")

# Display the questions and the Likert scale
for question in questions:
    responses[question] = st.radio(question, options=scale, index=2)  # start at neutral

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
    
    
    # Prepare the record for saving
    record = [name] + [responses[question] for question in questions] + [comments]
    # st.write(f"Record to be saved: {record}")  # Debug
    
    try:
        # Open the CSV file in append mode, creating it if it doesn't exist
        with open(file_path, "a", newline='', encoding='utf-8') as fo:
            writer = csv.writer(fo)
            
            # Check if the file is empty to write the header
            if os.path.getsize(file_path) == 0:
                writer.writerow(header)
            
            # Write the record
            writer.writerow(record)
        
        st.success("Your responses have been recorded successfully!")
        
    except Exception as e:
        st.error(f"An error occurred while saving your responses: {e}")

