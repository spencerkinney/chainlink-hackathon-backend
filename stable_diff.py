from dotenv import load_dotenv
from utils import process_scene_prompt

# Load environment variables
load_dotenv()

# Defining prompts in a list
# prompts = [
#     "Adventurers at the edge of a medieval town, facing a forked path leading into the wilderness. The scene should be in a classic fantasy style, with vibrant and colorful details, showing characters pondering their next move.", # Scene 1 - Leaving Town
#     "A dense, vibrant, and colorful forest scene, with adventurers cautiously moving through. A cloaked stranger appears, sharing rumors of a monster. The art should be detailed and colorful, capturing the tension of the unknown.", # Scene 2 - Entering the Wilderness
#     "Adventurers encountering a different stranger in the wilderness, who is sharing information about a nearby danger. The setting is a forest clearing, with a focus on realistic and vibrant art, emphasizing colorful interactions between the characters.", # Scene 3 - Meeting a Stranger
#     "A dynamic battle scene between adventurers and a fearsome monster in a forest clearing. The art should be vivid, colorful, and action-packed, showcasing the intensity of the confrontation.", # Scene 4 - Monster Battle
#     "Adventurers standing triumphant over the defeated monster, collecting their rewards. The scene should focus on the treasure and the sense of victory, with a detailed, realistic, and vibrant color style." # Scene 5 - Collecting Rewards
# ]


# prompts = [
#     "perfect masterpiece, fantasy art by artist Roger Brown, 4 dark humanoid silhouettes in front of a Medieval town with a castle at sunset, detailed and intricate, high details, 8k, HD, high quality, low contrast, depth of field, technicolor",
#     "perfect masterpiece, fantasy art by artist Roger Brown, wilderness landscape, detailed and intricate, high details, 8k, HD, high quality, low contrast, depth of field, technicolor",
#     "perfect masterpiece, fantasy art by artist Roger Brown, closeup of a strange Medieval character in a wilderness landscape, detailed and intricate, high details, 8k, HD, high quality, low contrast, depth of field, technicolor",
#     "perfect masterpiece, closeup of Wyvern monster, fantasy art by artist Roger Brown, detailed and intricate, high details, 8k, HD, high quality, low contrast, depth of field, technicolor",
#     "perfect masterpiece, fantasy art by artist Roger Brown, treasure chest open full of gold coins, wilderness landscape, detailed and intricate, high details, 8k, HD, high quality, low contrast, depth of field, technicolor",
# ]

prompt = """Visualize Alarmin The Outcast, a Drow Sorcerer from the Dungeons & Dragons universe, \
poised in a dimly lit cavern. Alarmin's skin is a deep ash-gray, with stark white hair \
that cascades down their shoulders. Their eyes are piercing violet, showing their aberrant \
psychic lineage. They stand 5 feet tall with a lean, agile physique. Their attire blends \
dark leather with fine cloth, adorned with silver threadwork of arcane symbols. No armor is \
worn, allowing freedom for spellcasting and movement. \
Alarmin wields a blackened wood quarterstaff with glowing blue runes and a bone-handled dagger. \
Motes of light float around, indicating their Drow magic, Faerie Fire spell. An aura of psychic \
energy emanates from them, distorting the air subtly. Their expression is wary yet confident, \
reflecting a life in the shadows. The cavern backdrop includes a makeshift bedroll and ancient \
Drow iconography on the walls. Alarmin's demeanor combines their criminal past with undeniable \
charisma, with light and shadow playing across their features to create an enigmatic presence."""


prompts = [
    prompt,
]

# Iterate over each prompt and generate an image
for prompt in prompts:
    process_scene_prompt(prompt)
