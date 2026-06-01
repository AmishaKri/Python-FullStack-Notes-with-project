from dotenv import load_dotenv
from pathlib import Path


from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI


load_dotenv()

openai_client=OpenAI

#vector embedding
embedding_model=OpenAIEmbeddings(
    model="text-embedding-3-large",
)

vector_store=QdrantVectorStore.from_existing_collection(
    
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning rag"
)
print("Indexing of document done..")

#Take user input
user_query=input("Ask something")

search_result=vector_db.similarity_search(query=user_query)

context="\n\n\n".join([f"Page Content:{result.page_content}" \n Page number: {result.metadata['page label']} \n File location:{result.metadata['file location']}" for result in search_result])

SYSTEM PROMPT="""
You are a helpful assistant that only give answer to user query based on the available context retrieved from a PDF file along ith page contens and page number. You should only ans the user based on the following context and navigate the user to open the right page number to know more.

Context:
    {context}
"""

openai_client.create_chat_completion(
    model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query},
    ],
)

print(response.choices[0].message.content)