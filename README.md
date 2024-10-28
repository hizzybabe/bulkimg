# Bulk Image Generation Prompts

A web application that generates creative prompts for AI image generation tools using Google's Gemini API.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```
5. Run the application:
   ```bash
   python app.py
   ```

# Deployment

The application is configured for Heroku deployment. 


## Usage

1. Enter a keyword in the input field
2. Click "Generate Prompts"
3. Copy the generated prompts to use with AI image generation tools