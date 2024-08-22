import os
from dotenv import load_dotenv
from openai import AzureOpenAI
import json

load_dotenv()

api_key = os.getenv("API_KEY")
azure_endpoint = os.getenv("AZURE_ENDPOINT")

client = AzureOpenAI(
    api_version="2024-05-01-preview",
    azure_endpoint=azure_endpoint,
    api_key=api_key,
)

# Generate the image using DALL-E 3
result = client.images.generate(
    model="Dalle3",  # the name of your DALL-E 3 deployment
    prompt="3D render of a cute orange monster on a dark blue background, digital art",
    n=1
)

# Parse and print the image URL
image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(f"Generated image URL: {image_url}")
