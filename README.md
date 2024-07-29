# LLM-Based Resume Analyzer, ATS Score, and JD Match Analyzer

## Live Demo
You can try out the live demo of the application here: [Smart ATS Run Easy](https://smart-ats-run-easy.streamlit.app/)


## Objective

This project involves developing an end-to-end Applicant Tracking System (ATS) using the Google Gemini Pro Vision API. The system analyzes resumes, compares them with job descriptions, and provides actionable suggestions for enhancing resumes to better match job requirements.

## Features

- **JD PErcentage Calculation**: Automatically evaluates the CV against job descriptions.
- **Improvement Suggestions**: Provides specific areas for improvement in the CV.
- **Skill Improvement Suggestions**: Identifies and suggests skills that can be added or improved in the CV.

## Requirements

- Python 3.8+
- Streamlit
- google.generativeai
- Google Gemini Pro Vision API Key
- streamlit
- os
- PyPDF2
- streamlit_player

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Disha4346/Smart-ATS.git
    cd resume-analyzer-ats
    ```

2. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up API Key**

    Obtain a Google Gemini Pro Vision API key and set it as an environment variable.

    ```bash
    export GEMINI_PRO_API_KEY='your_api_key'
    ```

## Usage

1. **Run the Application**

    ```bash
    streamlit run app.py
    ```

2. **Upload Job Description and CV/Resume**

    - Open your browser and go to the URL displayed by Streamlit.
    - Upload your Job Description and CV in the provided interface.

3. **Get Results**

    - The application will analyze the CV against the Job Description.
    - You will receive a JD PErcentage match, suggestions for improvement, and skill improvement suggestions.

## Project Structure

- **app.py**: Main application file that runs the Streamlit frontend.
- **requirements.txt**: List of dependencies required for the project.


## Contributing

I welcome contributions to enhance this project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your branch.
4. Create a Pull Request describing your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
