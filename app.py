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
from utils import get_uploaded_jsons
import logging


app = Flask(__name__)
CORS(app)
OUTPUT_DIRECTORY = "output"




load_dotenv()
print("FLASK_ENV:", os.environ.get('FLASK_ENV'))


def is_development_mode():
    """Check if the application is running in development mode."""
    return os.environ.get('FLASK_ENV') == 'development'


def download_image(image_url):
    """Downloads an image from a given URL and returns its content."""
    try:
        response = requests.get(image_url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        app.logger.error(f"Error downloading image from {image_url}: {e}")
        return None


def save_image_locally(image_content, seed):
    """Saves the image locally in development mode."""
    ensure_output_directory_exists()
    filename = f"{OUTPUT_DIRECTORY}/image-seed-{seed}-{time.strftime('%Y%m%d-%H%M%S')}.png"
    with open(filename, 'wb') as file:
        file.write(image_content)
    app.logger.info(f"Image saved locally: {filename}")


def process_scene_prompt(prompt, seed):
    """Processes a scene prompt with a given seed to generate an image."""
    try:
        output = replicate.run(
            "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
            input={"prompt": prompt, "seed": seed},
        )

        if isinstance(output, list) and len(output) > 0:
            image_url = output[0]
            image_content = download_image(image_url)
            if image_content:
                if is_development_mode():
                    save_image_locally(image_content, seed)
                encoded_image = base64.b64encode(image_content).decode('utf-8')
                return encoded_image
            else:
                return None
        else:
            app.logger.error("Unexpected output format: {}".format(output))
            return None
    except Exception as e:
        app.logger.error(f"Error in processing scene prompt: {e}")
        return None


def ensure_output_directory_exists():
    """Ensures that the output directory exists."""
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

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

    seed_values = [-1, -1]  # Example seeds
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
