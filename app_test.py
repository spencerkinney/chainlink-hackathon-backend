import requests
import time

def test_generate_image(server_url, prompt):
    """Sends a POST request to the Flask server to generate images based on a given prompt."""
    endpoint = f"{server_url}/generate-image"
    payload = {"prompt": prompt}
    
    try:
        start_time = time.time()

        response = requests.post(endpoint, json=payload)
        response.raise_for_status()

        end_time = time.time()
        response_time = end_time - start_time

        data = response.json()
        print("Response received")
        print(f"Response time: {response_time:.2f} seconds")

        if 'data' in data and 'images' in data['data']:
            for idx, image in enumerate(data['data']['images'], start=1):
                print(f"Image {idx}: {image[:30]}...") # Only print the first 30 bytes of the image base64 string for brevity

    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    server_url = "http://127.0.0.1:5000"
    #server_url = "https://stablediff-664a3266e9c5.herokuapp.com"
    test_prompt = "A logo design for Artour which is an art tech company. Clean and minimal design. Uber inspired."  # Example prompt
    test_generate_image(server_url, test_prompt)