import streamlit as st
from google.cloud import aiplatform

def configure_api():
    aiplatform.init(project="your-project-id")

def generate_review(prompt):
    try:
        # Create a client
        client = aiplatform.PredictionServiceClient()

        # Create a request for text generation
        response = client.predict(
            endpoint="your-endpoint-id",
            instances=[{"content": prompt}]
        )

        # Get the generated text
        generated_text = response.predictions[0]['content']

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

    configure_api()

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
