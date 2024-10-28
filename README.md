# Bulk Image Generation Prompts

A web application that generates creative prompts for AI image generation tools using Google's Gemini API. This tool helps artists and creators generate detailed prompts for AI image generation platforms like Midjourney and Stable Diffusion.

## Features

- Generate 5 detailed prompts from a single keyword
- Clean and intuitive user interface
- One-click copy functionality for prompts
- Responsive design
- Error handling and loading states
- Detailed prompts with style, mood, and lighting specifications

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

## Usage

1. Enter a keyword in the input field (e.g., "cybersecurity", "fantasy landscape", "steampunk")
2. Click "Generate Prompts"
3. Wait for the AI to generate detailed prompts
4. Use the "Copy" button to copy individual prompts
5. Use the prompts with your preferred AI image generation tool

## Deployment

The application is configured for Heroku deployment with the following features:
- Python 3.11.7 runtime
- Gunicorn web server
- Environment variable support
- Ready-to-deploy configuration

## Requirements

- Python 3.11.7
- Flask
- Google Generative AI (Gemini)
- Additional dependencies listed in `requirements.txt`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
