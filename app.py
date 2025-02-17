import streamlit as st
from google.cloud import aiplatform

# Configure API key
api_key = "AIzaSyD8_LN6yHSQNPzU5Aeu6NLEDiVt-isDBds"
aiplatform.init(project="649270149201", api_key=api_key)

# Streamlit UI
st.title("Python AI Code Reviewer")
st.write("Enter your Python code below and get a detailed review!")

user_code = st.text_area("Enter Python code here ...", height=250)

if st.button("Generate Review"):
    if user_code.strip():
        st.write("Analyzing your code... Please wait ")
        # Creating the prompt for AI
        prompt = f"Review the following Python code. Identify potential bugs, inefficiencies, and suggest improvements:\n\n{user_code}"
        # Call Google Generative AI API
        try:
            client = aiplatform.services.generative_ai.GenerativeAiClient()
            request = aiplatform.services.generative_ai.GenerateRequest(
                prompt=prompt,
                max_length=512,
                top_p=0.9,
                temperature=1.0
            )
            response = client.generate(request)
            review_result = response.generated_text
            st.subheader("")
            st.markdown(review_result)
        except Exception as e:
            st.error(f"Error while analyzing code: {e}")
    else:
        st.warning("")


