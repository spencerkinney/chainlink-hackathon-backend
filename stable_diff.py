import replicate
output = replicate.run(
    "stability-ai/sdxl:2b017d9b67edd2ee1401238df49d75da53c523f36e363881e057f5dc3ed3c5b2",
    input={"prompt": "an astronaut riding a rainbow unicorn"},
)
print(output)