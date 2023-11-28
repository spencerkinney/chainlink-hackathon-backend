import replicate
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Define your prompts in a list
prompts = [
    "A bustling medieval town at dawn, with adventurers in detailed medieval gear at the edge, looking at a rugged path. The art style should be a classic fantasy illustration, with muted earthy tones.",
    "Adventurers meeting a cloaked stranger in a dense forest. The style should mimic early Dungeons & Dragons manuals, with a realistic, detailed forest and a mysterious, dark tone.",
    "A dynamic battle scene in a classic fantasy style, showing detailed characters fighting a large beast. The art should have a high level of detail, similar to modern fantasy RPGs, with vibrant colors.",
    "Adventurers around a treasure hoard post-battle. The art should maintain the detailed, realistic style of modern RPGs, with a mix of exhaustion and victory on the characters' faces."
]

# Iterate over each prompt and generate an image
for prompt in prompts:
    output = replicate.run(
        "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
        input={"prompt": prompt},
    )

    # Generate a unique timestamped filename for each image
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"output/{output['id']}-{timestamp}.png"

    # Download the result image URL and save it to a file
    replicate.download(output["image"], filename)