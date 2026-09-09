import streamlit as st
from google import genai

import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=api_key)


st.set_page_config(
    page_title="AI Python Code Explainer",
    layout="centered"
)


st.title("AI Python Code Explainer")


st.write(
    "Paste your Python code below and get a clear "
    "beginner-friendly explanation."
)


python_code = st.text_area(
    "Enter Python Code",
    placeholder="""Example:


name = input("Enter your name: ")
print("Hello", name)
""",
    height=300
)


explanation_type = st.selectbox(
    "Select Explanation Type",
    [
        "Beginner Explanation",
        "Line-by-Line Explanation",
        "Short Summary",
        "Explain Code and Output"
    ]
)


if st.button(
    "Explain Python Code",
    type="primary",
    use_container_width=True
):


    if python_code.strip() == "":
        st.warning("Please enter Python code.")


    else:
        prompt = f"""
You are a Python teacher.


Explain the following Python code.


Python Code:
{python_code}


Explanation Type:
{explanation_type}


Instructions:
- Use clear and beginner-friendly language.
- Explain the purpose of the code.
- Explain important variables, functions and logic.
- Mention the expected output when possible.
- Do not make the explanation unnecessarily long.
- Format the explanation properly.
- Return only the explanation.
"""


        with st.spinner("Explaining Python code..."):


            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt
            )


        st.success("Python code explained successfully.")


        st.subheader("Code Explanation")


        st.markdown(response.text)

