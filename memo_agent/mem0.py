from dotenv import load_dotenv
from mem0 import Memory
import os
import json
from openai import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config={
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small",
            "api_key": OPENAI_API_KEY
        },
        "llm": {
            "provider": "openai",
            "config": {
                "model": "gpt-4o",
                "api_key": OPENAI_API_KEY
            }
        },
        "vector_store": {
            "provider": "qdrant",
            "config": {
                "host": "localhost",
                "port": 6333
            }
        }
    }
}
while True:
    user_query =input("> ")
    search_memory = mem_client.search(user_query)
    print(search_memory)
    memory_about_user =search_memory
    memories=[
        f"ID: {memory['id']}, Content: {memory['content']}" for memory in memory_about_user
    ]

    SYSTEM_PROMPT=f"""
    Here is the context about the user:
    {json.dumps(memories)}
    """
    response=client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )
    ai_response=response.choices[0].message.content
    print(ai_response)

    mem_client.add(
        messages=[
            {"role": "user", "content": user_query},
            {"role": "assistant", "content": ai_response}
        ]
    )
mem_client=Memory.from_config(config)