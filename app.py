import streamlit as st
import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from pdf_utils import extract_text_from_pdf

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

st.set_page_config(
    page_title="AI MCQ Generator",
    page_icon="📝"
)

st.title("AI MCQ Generator")
st.write("Generate MCQs from your study material using AI.")

if not HF_TOKEN:
    st.error("HF_TOKEN not found in .env file.")
    st.stop()

client = InferenceClient(
    api_key=HF_TOKEN,
    provider="groq"
)

# Sidebar
st.sidebar.header("MCQ Settings")

num_questions = st.sidebar.slider(
    "Number of Questions",
    1, 50, 10
)

# Input
input_type = st.radio(
    "Choose input method",
    ["Paste Text", "Upload PDF"]
)

study_material = ""

if input_type == "Paste Text":

    study_material = st.text_area(
        "Enter study material",
        height=250
    )

else:

    file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if file:
        study_material = extract_text_from_pdf(file)
        st.success("PDF uploaded successfully.")

        with st.expander("Preview"):
            st.write(study_material[:3000])

# Generate
if st.button("Generate MCQs", type="primary"):

    if not study_material.strip():
        st.warning("Please enter text or upload a PDF.")

    else:

        prompt = f"""
Generate exactly {num_questions} MCQs from the study material.

Each question must have 4 options: A, B, C, D.
Only one answer should be correct.
Give the answer key at the end.

Format:

Question 1:
Question here

A. Option
B. Option
C. Option
D. Option

Continue until Question {num_questions}.

Answer Key:
1. A
2. B

Study Material:
{study_material}
"""

        try:

            with st.spinner("Generating MCQs..."):

                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an MCQ generator."
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    max_tokens=6000,
                    temperature=0.5
                )

                result = response.choices[0].message.content

            st.subheader("Generated MCQs")
            st.write(result)

        except Exception as e:

            st.error(f"Error: {e}")