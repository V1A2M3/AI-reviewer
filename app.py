import streamlit as st
from google.cloud import aiplatform

# Create a Streamlit app
st.title("Python Code Reviewer App")

# Get the code from the user
code = st.text_area("Enter your code here:", height=200)

# Create a button to submit the code
if st.button("Submit"):
    # Perform code review
    review = perform_code_review(code)
    
    # Display the code review
    st.subheader("Code Review:")
    st.write(review)

def perform_code_review(code):
    # This function performs the code review
    # For simplicity, let's just use a text generation model
    try:
        client = aiplatform.TextGeneration(
            display_name="text-generation",
            location="us-central1",
            project="649270149201"
        )
        request = aiplatform.TextGenerationRequest(
            prompt=code,
            max_length=512,
            top_p=0.9,
            temperature=1.0
        )
        response = client.generate_text(request)
        review = response.generated_text
        return review
    except Exception as e:
        return f"Error while analyzing code: {e}"


