from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configure Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_prompts(keyword):
    prompt = f"""Generate 5 detailed image generation prompts related to {keyword}. 
    Each prompt should be creative and detailed, perfect for AI image generation tools like Midjourney or Stable Diffusion.
    Format each prompt on a new line and number them 1-5.
    Make each prompt descriptive with style, mood, lighting, and other relevant details."""

    response = model.generate_content(prompt)
    prompts = response.text.strip().split('\n')
    return [p.strip() for p in prompts if p.strip()]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    keyword = request.json.get('keyword', '')
    if not keyword:
        return jsonify({'error': 'Keyword is required'}), 400
    
    try:
        prompts = generate_prompts(keyword)
        return jsonify({'prompts': prompts})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
