
# AI MCQ Generator

An AI-powered Multiple Choice Question (MCQ) Generator that automatically creates questions, options, correct answers, and explanations from study material.

The application is built using Python and Streamlit, with Hugging Face providing the AI inference capabilities. It supports both pasted text and PDF-based study material.

---

## Project Overview

Creating MCQs manually from study material can be time-consuming. This project automates the process by using an AI language model to analyze educational content and generate relevant multiple-choice questions.

Users can provide study material by:

- Pasting text directly into the application
- Uploading a PDF document
- Selecting the required number of questions
- Generating MCQs using AI

Each generated question contains four answer choices, the correct answer, and an explanation.

---

## Features

### Text-Based MCQ Generation
Users can paste study material directly into the application and generate MCQs from the provided content.

### PDF Support
The application can extract text from uploaded PDF documents and use the extracted content to generate questions.

### Custom Number of Questions
Users can select the number of MCQs they want to generate.

### AI-Powered Question Generation
Hugging Face inference is used to generate questions based on the provided study material.

### Multiple Choice Options
Each generated question contains four options:

- A
- B
- C
- D

### Answer and Explanation
The application provides the correct answer along with an explanation to help users understand the concept.

### Streamlit Interface
The project provides a simple and interactive web interface using Streamlit.

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Application development |
| Streamlit | Web application interface |
| Hugging Face | AI model inference |
| Hugging Face Hub | API integration |
| PyPDF | PDF text extraction |
| python-dotenv | Environment variable management |

---

## Project Structure

```text
MCQ-GENERATOR/
│
├── app.py
├── mcqgenerator.py
├── pdf_utils.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
````

### File Description

**app.py**

Contains the main Streamlit application interface and handles user interaction.

**mcqgenerator.py**

Contains the AI-based MCQ generation logic and Hugging Face API integration.

**pdf_utils.py**

Extracts text from uploaded PDF files using PyPDF.

**requirements.txt**

Contains the Python packages required to run the project.

**.env**

Stores the Hugging Face API token securely. This file should not be uploaded to GitHub.

**.gitignore**

Prevents sensitive files and unnecessary Python files from being uploaded to the repository.

---

## System Requirements

Before running the project, make sure the following are installed:

* Python 3.10 or later
* Git
* Visual Studio Code
* Hugging Face account
* Hugging Face API token

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/MCQ-Generator.git
```

Move into the project directory:

```bash
cd MCQ-Generator
```

---

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

---

### 3. Activate the Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
venv\Scripts\activate
```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Hugging Face API Configuration

Create a Hugging Face API token from your Hugging Face account.

Create a file named:

```text
.env
```

Add your token:

```env
HF_TOKEN=your_huggingface_token
```

Do not upload your `.env` file to GitHub.

The project uses the environment variable to authenticate with Hugging Face.

---

## Running the Application

After activating the virtual environment, run:

```bash
python -m streamlit run app.py
```

The Streamlit application will open in your browser.

If it does not open automatically, use the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

---

## How to Use

### Step 1: Open the Application

Launch the Streamlit application using:

```bash
python -m streamlit run app.py
```

### Step 2: Select the Input Method

Choose one of the available input methods:

* Paste Text
* Upload PDF

### Step 3: Provide Study Material

Paste your study material or upload a PDF containing the topic you want to study.

Example:

```text
Artificial Intelligence is a branch of computer science that focuses
on creating systems capable of performing tasks that normally require
human intelligence. These tasks include learning, reasoning,
problem-solving, and decision-making.
```

### Step 4: Select the Number of Questions

Choose the number of MCQs you want to generate.

### Step 5: Generate MCQs

Click the:

```text
Generate MCQs
```

button.

The application processes the study material and generates multiple-choice questions.

### Step 6: Review the Questions

Each generated MCQ includes:

```text
Question
A. Option
B. Option
C. Option
D. Option

Correct Answer
Explanation
```

---

## Example

### Input

```text
Machine Learning is a subset of Artificial Intelligence that enables
computers to learn from data without being explicitly programmed.
```

### Generated MCQ

```text
Question:
What is Machine Learning?

A. A type of computer hardware
B. A subset of Artificial Intelligence
C. A programming language
D. A database system

Correct Answer:
B

Explanation:
Machine Learning is a subset of Artificial Intelligence that allows
systems to learn patterns from data without explicit programming.
```

---

## Application Workflow

```text
User
  |
  v
Enter Study Material
  |
  +-------------------+
  |                   |
  v                   v
Paste Text         Upload PDF
  |                   |
  |                   v
  |              Extract PDF Text
  |                   |
  +---------+---------+
            |
            v
      Process Content
            |
            v
    Hugging Face Model
            |
            v
      Generate MCQs
            |
            v
 Question + Options
 + Answer + Explanation
```

---

## Security

Sensitive credentials should never be committed to the GitHub repository.

The `.gitignore` file should contain:

```gitignore
venv/
.env
__pycache__/
*.pyc
```

The Hugging Face API token should only be stored in the `.env` file during local development.

---

## Future Enhancements

The project can be extended with additional features such as:

* Difficulty-level selection
* Subject/topic selection
* MCQ quiz mode
* Automatic score calculation
* Timer-based quizzes
* Download generated MCQs as PDF
* Download questions as a text or Word document
* Question regeneration
* Improved question validation
* User authentication
* Question history
* Database integration
* Deployment using Streamlit Cloud

---

## Learning Outcomes

This project demonstrates practical implementation of:

* Large Language Model integration
* Hugging Face API usage
* Prompt-based question generation
* Natural Language Processing
* PDF text extraction
* Python application development
* Streamlit web application development
* Environment variable management
* Virtual environment management
* Git and GitHub project management

---

## Project Status

The project is currently under development. The core functionality for generating MCQs from text and PDF study material is implemented.

---

## License

This project is intended for educational and academic purposes.

---

## Author

**Varalakshmi Kumar**

AI / Machine Learning Project

---

## Acknowledgements

* Hugging Face for providing AI model inference services
* Streamlit for the application framework
* PyPDF for PDF text extraction

