from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
client=OpenAI()
response=client.completions.create(
    model="text-davinci-003", 
    message=[
        {"role": "user", "content": "Hello world"}
    ]
    max_tokens=100)
print(response)