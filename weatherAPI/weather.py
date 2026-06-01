from dotenv import load_dotenv
from openai import OpenAI
import requests
from pydantic import BaseModel, Field
from typing import Optional
import os 
import json 
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

def run_command(command: str):
    result=os.system(command)
    return result
def get_weather(city: str):
    url=f"https://wttr.in/{city.lower()}?format=%C+%t"
    response = requests.get(url)
    
    if response.status_code == 200:
        return f"Current weather in {city} is {response.text}"
    return "Something went wrong"
available_tools={"get_weather": get_weather,
                 "run_command": run_command}
SYSTEM_PROMPT="""
    You're an expert AI Assistant in resolving user queries using chain of thought.
    You work on START, PLAN, and OUTPUT steps.
    You need to first PLAN what needs to be done. The PLAN can be multiple steps.
    Once you think enough PLAN has been done, finally you can give an OUTPUT.
    You can also call a tool if required from the list of avaiable tools.
    for every tool call wait for the observe step which is the output from the called tool.
    RULES:
    - Strictly follow the given JSON output format
    - Only run one step at a time.
    - The sequence of steps is START where user gives an input, PLAN that can be mulyiple times and finally OUTPUT which is going to the displayed to the user

    OUTPUT JSON FORMAT:
    {"step: "START|PLAN|OUTPUT", "content": "string", "tool": "string", "input": "string", "explanation": "string"}
    
    Available Tools:
    - get_weather{ctr:str}: Takes city name as an input string nad returns the weather info about the city. 
    - run_command{command:str}: Takes a system linux command and returns the output of the command.as an input string and returns the output of the command.
    Example 1:
    START: Hey, Can you solve 2+3/10
    PLAN: {"step": "PLAN", "content": "Seems like user is interested in math problem  2+3/10"}
    PLAN: {"step": "PLAN", "content": "I need to solve 2+3/10 Using BODMAS rule"}
    OUTPUT: {"step": "OUTPUT", "content": "The answer is 4.5"}
    
     Example 1:
    START: What is the weather of delhi?
    PLAN: {"step": "PLAN", "content": "Seems like user is interested in getting weather of Delhi in India"}
    PLAN: {"step": "PLAN", "content": "Lets see if we have any available tool from the list of available tools"}
    PLAN: {"step": "PLAN", "content": "Great, we have get_weather tool available for the query"}
    PLAN: {"step": "PLAN", "content": "I need to call get_weather tool to get the weather of Delhi as input for city"}
    PLAN: {"step": "TOOL", "tool": "get_weather", "input": "delhi"}
    PLAN: {"step": "OBSERVE", "tool": "get_weather", "output": "Current weather in delhi, India. 30°C"}
    PLAN: {"step": "PLAN", "content": "Great, we got the weather of Delhi"}
    OUTPUT: {"step": "OUTPUT", "content": "The current weather in Delhi is 20°C with some cloudy"}
    """
 
 
class MyOutputFormat(BaseModel):
    step: str = Field(..., description="The ID of the step. Example: PLAN, OUTPUT, START, TOOL, Result, etc.")
    content: Optional[str]=Field(None, description="The optional string content of the step.")
    tool: Optional[str]=Field(None, description="The ID of the tool to call. Example: weather, etc.")
    input: Optional[str]=Field(None, description="The input params for the tool.")
    explanation: str = Field(..., description="Explanation of the code")
    
message_history=[
    {"role": "system", "content": SYSTEM_PROMPT},
]

user_query=input(">")
message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=message_history,
        response_format={"type": "json_object"}
    )
    raw_response=response.choices[0].message.content
    message_history.append({"role": "assistant", "content": response.choices[0].message.content})
    print(response.choices[0].message.content)
    
    parsed_response=json.loads(raw_response)
    
    if parsed_response.get("step") == "START":
        print("START: ", parsed_response.get("content"))
        continue
    if parsed_response.get("step") == "TOOL":
        tool_to_call = parsed_response.get("tool")
        tool_input = parsed_response.get("input")

        if tool_to_call != "get_weather":
            print(f"ERROR: unsupported tool '{tool_to_call}'")
            continue

        if not tool_input:
            tool_input = "delhi"
            print("INFO: no city provided, using default city 'delhi'")

        try:
            tool_response = available_tools[tool_to_call](tool_input)
        except KeyError:
            print(f"ERROR: tool '{tool_to_call}' is not available")
            continue

        print(f"TOOL: {tool_to_call}({tool_input}) = {tool_response}")

        message_history.append({
            "role": "assistant",
            "content": json.dumps({
                "step": "OBSERVE",
                "tool": tool_to_call,
                "output": tool_response
            })
        })

        continue
    if parsed_response["step"] == "PLAN":
        print("PLAN: ", parsed_response.get("content"))
        continue

    if parsed_response["step"] == "OUTPUT":
        print("OUTPUT: ", parsed_response.get("content"))
        break
    
def main():
    user_query=input(">")
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
    
print(get_weather("delhi"))