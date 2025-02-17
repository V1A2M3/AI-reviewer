import streamlit as st
from google.cloud import aiplatform

def configure_api(api_key):
    aiplatform.init(project="649270149201", api_key="AIzaSyD8_LN6yHSQNPzU5Aeu6NLEDiVt-isDBds")

def generate_review(prompt):
    try:
        # Create a client
        client = aiplatform.TextClient()

        # Send the request
        response = client.generate_text(prompt=prompt)

        # Get the generated text
        generated_text = response.text

        return generated_text
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def display_review(review_result):
    st.subheader("🔍 Code Review Report")
    st.markdown(review_result)

def main():
    st.title("Python AI Code Reviewer")
    st.write("Enter your Python code below and get a detailed review!")

    api_key = "AIzaSyD8_LN6yHSQNPzU5Aeu6NLEDiVt-isDBds"
    configure_api(api_key)

    user_code = st.text_area("Enter Python code here ...", height=250)

    if st.button("Generate Review"):
        if user_code.strip():
            st.write("Analyzing your code... Please wait ⏳")
            prompt = f"Review the following Python code. Identify potential bugs, inefficiencies, and suggest improvements:\n\n{user_code}"
            review_result = generate_review(prompt)
            if review_result:
                display_review(review_result)
        else:
            st.warning("⚠ Please enter some Python code first.")

if __name__ == "__main__":
    main()

