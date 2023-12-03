import replicate
import requests
import os
import time

# Define the output directory
OUTPUT_DIRECTORY = "output"


# Function to download image from URL
def download_image(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
    else:
        print(f"Failed to download image from {image_url}")

# Ensure the output directory exists
def ensure_output_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


# Function to process each prompt
def process_scene_prompt(prompt, seed=12345):
    ensure_output_directory(OUTPUT_DIRECTORY)

    output = replicate.run(
        "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
        input={"prompt": prompt, "seed": seed},
    )

    # Check if output is a list with at least one element
    if isinstance(output, list) and len(output) > 0:
        image_url = output[0]
        # Generate a unique timestamped filename for each image
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{OUTPUT_DIRECTORY}/image-{timestamp}.png"

        # Download the image
        download_image(image_url, filename)
    else:
        print("Unexpected output format:", output)