import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
from streamlit_player import st_player

load_dotenv()  # Load environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Corrected function name
def get_gemini_response(resume_text, job_desc):
    model = genai.GenerativeModel('gemini-1.5-pro')
    input_prompt = f"""
    Hey, act like a skilled ATS (Applicant Tracking System) specializing in software engineering, data science, and big data engineering.
    Your task is to analyze the given resume against the provided job description and suggest improvements.

    ### Job Description:
    {job_desc}

    ### Resume:
    {resume_text}

    Assign a JD Match Percentage and list missing keywords.

    Response Format:
    {{
        "JD Percentage Match": "%",  
        "Missing Keywords": [],  
        "Profile Summary": ""
    }}
    """
    
    response = model.generate_content(input_prompt)
    return response.text

def extract_text_from_pdf(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""  # Ensure empty pages don’t break the code
    return text.strip()

# Streamlit UI setup
st.set_page_config(page_title='Resume Analyzer', layout='wide', page_icon="🔍")
st.sidebar.title("🎨 Smart ATS 🎨")
with st.sidebar.container(): 
    st.image('res.jpeg', use_container_width=True, caption='Resume Analyzer')
st.sidebar.markdown("---")

def print_praise():
    return "**Created By -**\n\nDisha Gupta"

st.sidebar.success(print_praise())   
st.sidebar.write("---\n")

# User input fields
jd = st.text_area("⬇️ Paste the Job Description here ⬇️")
uploaded_file = st.file_uploader("⬇️ Upload Your Resume ⬇️", type="pdf", help="Please upload the PDF")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None and jd.strip() != "":
        resume_text = extract_text_from_pdf(uploaded_file)
        response = get_gemini_response(resume_text, jd)  # Now passing both resume and JD
        st.subheader("📊 ATS Analysis Result")
        st.write(response)  # Display output properly
    else:
        st.error("⚠️ Please upload a resume and paste a job description!")

st.info("ℹ️ Need help? Watch this resume tutorial:")
youtube_url = "https://youtu.be/y3R9e2L8I9E?si=l0_i6AcqLSkRs7KJ"
st_player(youtube_url)
