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
        "name": "Rare Necklace NFT",
        "description": "A unique NFT representing a Rare Necklace.",
        "image": image_url,
        "attributes": [
            {"trait_type": "Category", "value": "wealth"},
            {"trait_type": "Loot", "value": "rare necklace"}
        ]
    }
    with open(filename, 'w') as file:
        json.dump(metadata, file)

# Retrieve the JWT token from the .env file
jwt_token = os.getenv('PINATA_JWT_TOKEN')

# Path to your NFT image file
image_file_path = 'ipfs/files/img/rare-necklace.jpeg'  # Update this with your actual image file path

# Upload the NFT image
image_response = upload_to_pinata(image_file_path, jwt_token)
image_url = f"https://ipfs.io/ipfs/{image_response['IpfsHash']}"

# Path for the metadata JSON file
metadata_file_path = 'rare-necklace-metadata.json'  # You can choose any filename or path

# Create and save the metadata JSON file
create_metadata_file(image_url, metadata_file_path)

# Upload the metadata JSON file
metadata_response = upload_to_pinata(metadata_file_path, jwt_token)

print(metadata_response)