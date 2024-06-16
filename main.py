# pip install streamlit
# to run the Streamlit server open a terminal an run this:
# streamlit run /Users/amendatate/Documents/HCI584/atate_HCI584_project/main.py

import streamlit as st
import plot_likert
import csv
import os

# Print the current working directory
st.write(f"Current working directory: {os.getcwd()}") # Debug

# Define the questions
questions = [
    "I felt happy.",
    "I felt engaged.",
    "I felt comfortable.",
    "I felt safe and secure.",
    "I enjoyed the company of other people.",
    "I talked to other people.",
]

# Define the Likert scale
scale = plot_likert.scales.agree5

# Create a dictionary to store the responses
responses = {}
print(responses)  # Debug

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
    st.write(f"Record to be saved: {record}")  # Debug
    
    # Define the header
    header = ["Name"] + questions + ["Comments"]
    
    try:
        # Determine the file path
        file_path = "wellbeing_survey.csv"
        
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
