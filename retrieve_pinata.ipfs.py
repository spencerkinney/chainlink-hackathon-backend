import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_uploaded_jsons(jwt_token):
    url = "https://api.pinata.cloud/data/pinList"
    headers = {'Authorization': f'Bearer {jwt_token}'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print("Success, authenticated and received response!")
        pin_data = response.json()
        json_files_urls = [
            f"https://ipfs.io/ipfs/{pin['ipfs_pin_hash']}" 
            for pin in pin_data['rows'] 
            if pin.get('metadata') and pin['metadata'].get('name') 
            and isinstance(pin['metadata']['name'], str) 
            and pin['metadata']['name'].endswith('.json')
        ]
        return json_files_urls
    else:
        print("Error:", response.status_code, response.text)
        return []

# Retrieve the JWT token from the .env file
jwt_token = os.getenv('PINATA_JWT_TOKEN')

# Get the list of URLs for uploaded JSON files
uploaded_json_urls = get_uploaded_jsons(jwt_token)
print(uploaded_json_urls)