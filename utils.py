import requests
import os

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