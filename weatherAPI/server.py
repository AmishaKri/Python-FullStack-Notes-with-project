from openai import OpenAI
from dotenv import load_dotenv
import requests
import os
import json

# Load env
load_dotenv()

# Initialize Groq
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# ==========================================
# TOOL
# ==========================================

def get_weather(city):

    url = f"https://wttr.in/{city}?format=%C+%t"

    response = requests.get(url)

    if response.status_code == 200:
        return response.text

    return "Weather unavailable"


# ==========================================
# TOOL DEFINITIONS
# ==========================================

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City name"
                    }
                },
                "required": ["city"]
            }
        }
    }
]

# ==========================================
# USER INPUT
# ==========================================

user_query = input("Ask something: ")

# ==========================================
# SIMPLE PROMPT
# ==========================================

messages = [
    {
        "role": "system",
        "content": """
You are a weather assistant.

If user asks about weather,
temperature, climate, forecast,
or rain, use the get_weather tool.
"""
    },
    {
        "role": "user",
        "content": user_query
    }
]

# ==========================================
# FIRST CALL
# ==========================================

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    tools=tools,
    tool_choice="auto"
)

message = response.choices[0].message

# ==========================================
# TOOL EXECUTION
# ==========================================

if message.tool_calls:

    tool_call = message.tool_calls[0]

    function_name = tool_call.function.name

    arguments = json.loads(tool_call.function.arguments)

    if function_name == "get_weather":

        tool_result = get_weather(arguments["city"])

        print("\n===== TOOL RESULT =====\n")
        print(tool_result)

        # Add assistant message
        messages.append(message)

        # Add tool output
        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": tool_result
        })

        # ======================================
        # FINAL RESPONSE
        # ======================================

        second_response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )

        print("\n===== FINAL ANSWER =====\n")
        print(second_response.choices[0].message.content)

else:
    print(message.content)