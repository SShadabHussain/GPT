
# GPT-4 Assistant

This is a Streamlit web application that utilizes the OpenAI GPT-4 model to generate responses based on user prompts.

## Getting Started

To run this application locally, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your_username/your_repository.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:

   - Sign up for an account on the OpenAI website and obtain your API key.
   - Set the `OPENAI_API_KEY` environment variable on your system with your API key.

4. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

## Usage

Once the application is running, you can interact with it through a web browser:

- Enter your prompt in the text area provided.
- Adjust the temperature slider to control the creativity of the model's responses.
- Choose a GPT-4 model from the dropdown menu.
- Click the "Get Response" button to generate a response based on your prompt.

## Dependencies

- Python 3.x
- Streamlit
- OpenAI Python SDK
- python-dotenv
