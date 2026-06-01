from typing_extensions import TypedDict
from typing import Annotated
from  langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()

llm = init_chat_model(
    model="gpt-4o",
    model_provider="openai"
)
class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    print("Inside chatbot")
    response = llm.invoke(state.get("messages"))
    return {"messages":[response]}


graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

updated_state = graph.invoke({"messages": ["Hey there"]})
print(updated_state)

# START -> chatbot -> END 

# state = { messages: ["Hey there"]}
# node runs: chatbot(state: ["Hey There"]) -> ["Hi, This is a message from ChatBot Node"]
# state = { "messages": ["Hey there", "Hi, This is a message from ChatBot Node"]}

