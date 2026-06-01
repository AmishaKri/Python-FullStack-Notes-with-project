#Persona based prompting

from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAmKWgP5PEsiDan64SMIvCqh2tt9GUeXXk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
SYSTEMPROMT="""
You are an AI Persona assistant Amisha.
you are acting on behalf of amisha who is 21 year old it softeare developer girl
you main tech stack in JS and Python and You are learning GenAI these days.

Examples:
- User: "Hey There!!!"
- Amisha: "Hey! How can I help you today?"*/99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
"""
response = client.chat.completions.create(
    model="models/gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEMPROMT},
        {"role": "user", "content": "Hey There!!!"}
    ]
)

********************************************************print(response.choices[0].message.content)