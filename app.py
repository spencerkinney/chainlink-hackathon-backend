from flask import Flask, request, jsonify
import replicate
import base64
import requests
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dotenv import load_dotenv


app = Flask(__name__)
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


def ensure_output_directory_exists():
    """Ensures that the output directory exists."""
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)


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


@app.route('/generate-image', methods=['POST'])
def generate_image():
    """Endpoint to generate images based on prompts."""
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    seed_values = [12345, 67890]  # Example seeds
    images = []

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(process_scene_prompt, prompt, seed)
                   for seed in seed_values]
        for future in as_completed(futures):
            result = future.result()
            if result:
                images.append(result)
            else:
                return jsonify({"error": "Error generating image"}), 500

    return jsonify({"data": {"images": images}})


if __name__ == "__main__":
    app.run(debug=True)
