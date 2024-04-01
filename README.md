# Invoice AI Assistant

Invoice AI Assistant is a Streamlit web application that utilizes AI to analyze invoices. It allows users to input prompts and upload images of invoices, and then provides analysis results based on AI processing.

## Features

- **AI-Powered Analysis**: Utilizes Google Generative AI to provide insights on uploaded invoices.
- **Easy-to-Use Interface**: Simple and intuitive user interface for inputting prompts and uploading images.
- **Custom Styling**: Enhanced UI with custom styling for better user experience.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your_username/invoice-ai-assistant.git
    cd invoice-ai-assistant
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables:

    ```bash
    # Create a .env file
    touch .env
    ```

    Add your Google API key to the `.env` file:

    ```
    GOOGLE_API_KEY=your_api_key_here
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Customization

You can customize the styling and functionality of the app by modifying the `app.py` file and the CSS styles within it.

