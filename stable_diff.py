import replicate
from dotenv import load_dotenv
import time
from utils import download_image, ensure_output_directory

# Load environment variables
load_dotenv()

# Define the output directory
output_directory = "output"
ensure_output_directory(output_directory)

# Defining prompts in a list
prompts = [
    "Adventurers at the edge of a medieval town, facing a forked path leading into the wilderness. The scene should have a classic fantasy style, with detailed characters pondering their next move.", # Scene 1 - Leaving Town
    "A dense forest scene, with adventurers cautiously moving through. A cloaked stranger appears, sharing rumors of a monster. The art should be detailed and mysterious, capturing the tension of the unknown.", # Scene 2 - Entering the Wilderness
    "Adventurers encountering a different stranger in the wilderness, who is sharing information about a nearby danger. The setting is a forest clearing, and the art should be realistic, with a focus on the interaction between the characters.", # Scene 3 - Meeting a Stranger
    "A dynamic battle scene between adventurers and a fearsome monster in a forest clearing. The art should be vivid and action-packed, showcasing the intensity of the confrontation.", # Scene 4 - Monster Battle
    "Adventurers standing triumphant over the defeated monster, collecting their rewards. The scene should focus on the treasure and the sense of victory, with a detailed, realistic style." # Scene 5 - Collecting Rewards
]

# Function to process each prompt
def process_prompt(prompt):
    output = replicate.run(
        "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
        input={"prompt": prompt},
    )

    # Check if output is a list with at least one element
    if isinstance(output, list) and len(output) > 0:
        image_url = output[0]
        # Generate a unique timestamped filename for each image
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filename = f"{output_directory}/image-{timestamp}.png"

        # Download the image
        download_image(image_url, filename)
    else:
        print("Unexpected output format:", output)

# Iterate over each prompt and generate an image
for prompt in prompts:
    process_prompt(prompt)