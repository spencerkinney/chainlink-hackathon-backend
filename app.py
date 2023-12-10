from flask import Flask, request, jsonify
from flask_cors import CORS
import replicate
import base64
import requests
import os
import time
from openai import OpenAI
from concurrent.futures import ThreadPoolExecutor, as_completed
from multiprocessing import Pool
from dotenv import load_dotenv
from utils import get_uploaded_jsons, process_scene_prompt


app = Flask(__name__)
CORS(app)
OUTPUT_DIRECTORY = "output"

load_dotenv()
print("FLASK_ENV:", os.environ.get('FLASK_ENV'))

def generate_image_worker(args):
    """Worker function for processing an image generation task."""
    prompt, seed = args
    return process_scene_prompt(prompt, seed)
    

@app.route('/generate-image', methods=['POST'])
def generate_image():
    """Endpoint to generate images based on prompts."""
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    seed_values = [12345, 67890]  # Example seeds
    images = []

    with Pool(processes=2) as pool:
        results = pool.map(generate_image_worker, [(prompt, seed) for seed in seed_values])

    for result in results:
        if result:
            images.append(result)
        else:
            return jsonify({"error": "Error generating image"}), 500

    return jsonify({"data": {"images": images}})

@app.route('/generate-text', methods=['POST'])
def generate_text():
  """Endpoint to generate text based on prompts."""
  data = request.json
  prompt = data.get('prompt')
  if not prompt:
    return jsonify({"error": "No prompt provided"}), 400

  client = OpenAI(api_key='')

  response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a dungeons and dragons dungeon master."},
      {"role": "user", "content": "Make a quest where the ultimate prize is a treasure chest.  The quest is presented in a choose your own adventure style adventure.  For each step, present a scenario and end with a question and 4 choices.  Only generate one question at a time and I will let you know how they answered."},
    ]
  )

  text = []
  print(response)
  text.append(response.choices[0].message.content)

  return jsonify({"data": {"text": text}})


@app.route('/latest-mints', methods=['GET'])
def latest_mints():
    """Endpoint to list the latest minted NFTs."""
    jwt_token = os.getenv('PINATA_JWT_TOKEN')
    metadata_urls = get_uploaded_jsons(jwt_token)
    return jsonify({"data": metadata_urls})

@app.route('/')
def home():
    return "If you are seeing this page, that means the shit is online. if you have further issues, don't ask spencer - he probably dont care"

if __name__ == "__main__":
    app.run(debug=True)
