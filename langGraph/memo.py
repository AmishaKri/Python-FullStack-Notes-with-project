from mem0 import Memory
import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

config = {
    "version": "v1.1",
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        },
        "llm": {
            "provider": "openai",
            "config": {
                "api_key": OPENAI_API_KEY,
                "model": "gpt-4o"
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

mem_client = Memory.from_config(config)

while True:
    user_query=input("> ")
    search_results = mem_client.search(query=user_query)
    print("Search results:", search_results)
    memory_about_user=search_results["results"]

    memories=[
        f"ID: {mem.get('id')}, Content: {mem.get('content')}" for mem in memory_about_user
    ]
    
    print("Memories:", memories)
    SYSTEM_PROMPT = f"""You are a helpful assistant. Here is the user's query: {user_query}
    Here are the user's memories:
    {json.dumps(memories)}
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_query}
        ]
    )

    ai_response=response.choices[0].message.content

    print("AI:", ai_response)

    mem_client.add(
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "assistant", "content": ai_response}
        ]
    )

    print("Memory saved!")


