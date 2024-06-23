from flask import Flask, request, jsonify, render_template
import requests


# Load environment variables from .env file

app = Flask(__name__)

api_key= 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMDliYTM5ZDItNTE4OS00MmU0LTgzYTAtYjRjZDdlNjE4MmUyIiwidHlwZSI6ImFwaV90b2tlbiJ9.gD72jhfV_AMJUhsIljxHZXl-cDNGsDOTqSM4UKiMDkk'

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
     data = request.get_json()
     prompt = data.get('prompt', '')
     max_length = data.get('max_length', 500)
    
     full_prompt = f"Write an essay about {prompt}"
    
     # Make a request to API
     headers = {
         'Authorization': f'Bearer {api_key}',
         'Content-Type': 'application/json',
     }
     payload = {
         'prompt': full_prompt,
         'max_tokens': max_length,
         'temperature': 0.7,
     }
     response = requests.post('https://api.edenai.run/v2/text/generation', headers=headers, json=payload)
    
     if response.status_code == 200:
         result = response.json()
         essay = result['choices'][0]['text'].strip()
     else:
         essay = f"Error: {response.status_code}, {response.text}"
    
     return jsonify({'essay': essay})

if __name__ == '__main__':
  app.run(debug=True)
