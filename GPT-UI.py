import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Securely get the API key from the environment variables
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    st.error("API key not found. Please set OPENAI_API_KEY in your environment variables.")
    st.stop()

# Initialize the OpenAI client with the API key
openai.api_key = api_key

def get_completion(prompt, model="gpt-4-0125-preview", temperature=0):
    try:
        client = openai.OpenAI(api_key = openai.api_key)
        messages = [{"role": "user", "content": prompt}]
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    
    st.set_page_config(
            # page_title="GPT-4 Assistant",
            page_icon="🤖",
            # layout="wide"
        )
    st.title("GPT-4 Assistant")
    col_A, col_B, col_C = st.columns([5, 5, 5])
    
    with st.container():
        # Increase the width of the input prompt using columns. The first column will be used for the prompt.
        col1, col2 = st.columns([10, 1])  # Adjust the ratio as needed for your layout
        with col1:
            prompt = st.text_area("Enter your prompt", "")
            temperature = st.slider("Set temperature (0-1)", min_value=0.0, max_value=1.0, value=0.0, step=0.01)

        with st.columns(3)[0]:
            model_choice = st.selectbox("Choose model", ["gpt-4-turbo-preview", "gpt-4-0125-preview"], index=0)

    if st.button("Get Response"):
        # Fetch and display the response
        response = get_completion(prompt, model=model_choice, temperature=temperature)
        if response:
            st.write("GPT response:")
            st.markdown(f"```{response}```")

if __name__ == "__main__":
    main()