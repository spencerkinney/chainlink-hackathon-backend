import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Function to upload a file to Pinata using JWT from .env
def upload_to_pinata(filepath, jwt_token):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    
    with open(filepath, 'rb') as file:
        files = {'file': file}
        headers = {'Authorization': f'Bearer {jwt_token}'}
        response = requests.post(url, files=files, headers=headers)

        return response.json()

# Function to create a JSON file for NFT metadata
def create_metadata_file(image_url, filename):
    metadata = {
        "name": "Legendary Dagger NFT",
        "description": "A unique NFT representing a Legendary Dagger.",
        "image": image_url,
        "attributes": [
            {"trait_type": "Category", "value": "weapon"},
            {"trait_type": "Loot", "value": "legendary dagger"}
        ]
    }
    with open(filename, 'w') as file:
        json.dump(metadata, file)

# Retrieve the JWT token from the .env file
jwt_token = os.getenv('PINATA_JWT_TOKEN')

# Path to your NFT image file
image_file_path = 'ipfs/files/img/legendary-dagger.png'  # Update this with your actual image file path

# Upload the NFT image
image_response = upload_to_pinata(image_file_path, jwt_token)
image_url = f"https://ipfs.io/ipfs/{image_response['IpfsHash']}"

# Path for the metadata JSON file
metadata_file_path = 'legendary-dagger-metadata.json'  # You can choose any filename or path

# Create and save the metadata JSON file
create_metadata_file(image_url, metadata_file_path)

# Upload the metadata JSON file
metadata_response = upload_to_pinata(metadata_file_path, jwt_token)

print(metadata_response)