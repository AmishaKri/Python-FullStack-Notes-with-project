from openai import OpenAI
import json 
client = OpenAI(
    api_key="AIzaSyAmKWgP5PEsiDan64SMIvCqh2tt9GUeXXk",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEMPROMT="""
 You're an expert AI Assistant in resolving user queries using chain of thought.
 You work on START, PLAN, and OUTPUT steps.
 You need to first PLAN what needs to be done. The PLAN can be multiple steps.
 Once you think enough PLAN has been done, finally you can give an OUTPUT.

 RULES:
 - Strictly follow the given JSON output format
 - Only run one step at a time.
 - The sequence of steps is START where user gives an input, PLAN that can be mulyiple times and finally OUTPUT which is going to the displayed to the user

 OUTPUT JSON FORMAT:
 {
    "step": "START|PLAN|OUTPUT",
    "content": "The content of the step"
 }

 Example:
 START: Hey, Can you solve 2+3/10
 PLAN: {"step": "PLAN", "content": "Seems like user is interested in math problem  2+3/10"}
 PLAN: {"step": "PLAN", "content": "I need to solve 2+3/10 Using BODMAS rule"}

"""
messageHistory=[
    {"role": "system", "content": SYSTEMPROMT}
]
userQuery=input("User: ")
messageHistory.append({"role": "user", "content": userQuery})

while True:
    client.chat.completions.create(
        model="models/gemini-3-flash-preview",
        response_format={"type": "json_object"},
        messages=messageHistory
    )

rawResult=(response.choices[0].message.content)
parsedResult=json.loads(rawResult)

if parsedResult["step"] == "START":
    print("START: ", parsedResult.get("content"))
    continue

if parsedResult["step"] == "PLAN":
    print("PLAN: ", parsedResult.get("content"))
    continue

if parsedResult["step"] == "OUTPUT":
    print("OUTPUT: ", parsedResult.get("content"))
    break
   
print(parsedResult)



print(response.choices[0].message.content)

#Few short prompting:The model is given a few examples of the desired output format. and bind the output quality.