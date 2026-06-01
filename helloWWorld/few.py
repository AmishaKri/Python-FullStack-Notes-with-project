from openai import OpenAI

client = OpenAI(
    api_key="AIzaSyAmKWgP5PEsiDan64SMIvCqh2tt9GUeXXk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEMPROMT="You should only and only ans the coding related question. Do not ans anything else. Your name is Alexa
OutPut Format:
{{
    "code": "Python code",
    "explanation": "Explanation of the code"
}}
Examples:
User: What is Python?
Assistant: Python is a high-level programming language.
"
response = client.chat.completions.create(
    model="models/gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": SYSTEMPROMT},
        {"role": "user", "content": "Explain AI"}
    ]
)

print(response.choices[0].message.content)

#Few short prompting:The model is given a few examples of the desired output format. and bind the output quality.