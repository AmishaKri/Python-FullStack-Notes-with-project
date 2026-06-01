from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client=OpenAI()

response = client.chat.completions.create(
    model="image-alpha-001",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "image", "url": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Good_Food_Display.jpg"},
                {"type": "text", "text": "Generate a caption for this image in about 40 words."}
            ]
        }
    ]
)