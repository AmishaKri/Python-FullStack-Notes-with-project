from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def get_weather(city: str):
    url=f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"Current weather in {city} is {response.text}"
    return "Something went wrong"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": f"current degree in {location}",
            }
        ]
    )

    return response.choices[0].message.content
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "current degree in delhi",
        }
    ]
)

print(response.choices[0].message.content)