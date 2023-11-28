from dotenv import load_dotenv
from utils import process_scene_prompt

# Load environment variables
load_dotenv()

# Defining prompts in a list
prompts = [
    "Adventurers at the edge of a medieval town, facing a forked path leading into the wilderness. The scene should be in a classic fantasy style, with vibrant and colorful details, showing characters pondering their next move.", # Scene 1 - Leaving Town
    "A dense, vibrant, and colorful forest scene, with adventurers cautiously moving through. A cloaked stranger appears, sharing rumors of a monster. The art should be detailed and colorful, capturing the tension of the unknown.", # Scene 2 - Entering the Wilderness
    "Adventurers encountering a different stranger in the wilderness, who is sharing information about a nearby danger. The setting is a forest clearing, with a focus on realistic and vibrant art, emphasizing colorful interactions between the characters.", # Scene 3 - Meeting a Stranger
    "A dynamic battle scene between adventurers and a fearsome monster in a forest clearing. The art should be vivid, colorful, and action-packed, showcasing the intensity of the confrontation.", # Scene 4 - Monster Battle
    "Adventurers standing triumphant over the defeated monster, collecting their rewards. The scene should focus on the treasure and the sense of victory, with a detailed, realistic, and vibrant color style." # Scene 5 - Collecting Rewards
]

# Iterate over each prompt and generate an image
for prompt in prompts:
    process_scene_prompt(prompt)