import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv() ## load all our environment variables

genai.configure(api_key="")

def get_gemini_repsonse(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader=pdf.PdfReader(uploaded_file)
    text=""
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
    return text

#Prompt Template

input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field, software engineering, full stack development,web development, AI Engineer, Machine Learning Engineer.
Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and the missing keywords with high accuracy
resume:{text}
description:{jd}

Give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""
input_prompt2 = """
 You are an experienced Technical Human Resource Manager with a deep understanding of 
 the tech field, software engineering, full stack development,web development, AI Engineer, Machine Learning Engineer,
 your task is to review the provided resume. 
Please share your professional evaluation on whether the candidate's has a strong profile considering that the job market is very competitive and you should provide 
best assistance for improving their resumes. 
 Highlight the strengths and weaknesses of the applicant.
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please upload the pdf")

submit = st.button("Percentage Match")

submit2 = st.button("Tell me about the resume")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)
    else:
        st.write("Please upload the resume")
        
elif submit2:
    if uploaded_file is not None:
        pdf_content=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt2)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please upload the resume")