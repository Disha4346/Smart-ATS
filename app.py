import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
from streamlit_player import st_player

load_dotenv() ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

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
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy


I want the response having the structure
"JD PErcentage Match":"%"\n\n
,"MissingKeywords":"[]",\n\n
"Profile Summary":""
"""

## streamlit app setup
st.set_page_config(page_title='Resume Analyzer',
                   layout='wide',
                   page_icon="🔍")
st.sidebar.title("🎨 Smart ATS 🎨")
with st.sidebar.container(): 
    st.image('res.jpeg', use_column_width=True, caption='Resume analzer')
st.sidebar.markdown("---")

def print_praise():
    praise_quotes = """
    Disha Gupta
    """
    title = "**Created By -**\n\n"
    return title + praise_quotes

st.sidebar.success(print_praise())   
st.sidebar.write("---\n")

jd=st.text_area("⬇️ Paste the Job Description here ⬇️")
uploaded_file=st.file_uploader("⬇️ Upload Your Resume ⬇️",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")
st.write("\n\n"*4)

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response=get_gemini_repsonse(input_prompt)
        st.subheader(response)

st.info("ℹ️ℹ️  <3  Refer to this video in case you don't have a resume yet.  <3  ℹ️ℹ️\n\n")
youtube_url = "https://youtu.be/y3R9e2L8I9E?si=l0_i6AcqLSkRs7KJ"
st_player(youtube_url)
