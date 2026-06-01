from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAmKWgP5PEsiDan64SMIvCqh2tt9GUeXXk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="models/gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that only give answer to math question and if the question not related to math please say sorry I can only answer math question"},
        {"role": "user", "content": "Explain AI"}
    ]
)

print(response.choices[0].message.content)