from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAmKWgP5PEsiDan64SMIvCqh2tt9GUeXXk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEMPROMT="You should only and only ans the coding related question. Do not ans anything else. Your name is Alexa"
response = client.chat.completions.create(
    model="models/gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEMPROMT},
        {"role": "user", "content": "Explain AI"}
    ]
)

print(response.choices[0].message.content)

#Zero short prompting:The model is given a direct question or task without prior examples.