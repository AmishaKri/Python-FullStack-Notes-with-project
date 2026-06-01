from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()

openai_client = OpenAI()


_vector_store = None


def get_vector_store() -> QdrantVectorStore:
    global _vector_store
    if _vector_store is None:
        embedding_model = OpenAIEmbeddings(
            model="text-embedding-3-large",
        )
        _vector_store = QdrantVectorStore.from_existing_collection(
            embedding=embedding_model,
            url="http://localhost:6333",
            collection_name="learning rag"
        )
    return _vector_store


def process_query(user_query: str) -> str:
    vector_store = get_vector_store()
    search_result = vector_store.similarity_search(query=user_query)
    context = "\n\n\n".join(
        [
            f"Page Content: {result.page_content}\nPage number: {result.metadata.get('page label')}\nFile location: {result.metadata.get('file location')}"
            for result in search_result
        ]
    )

    system_prompt = f"""
You are a helpful assistant that only give answer to user query based on the available context retrieved from a PDF file along with page contents and page number. You should only answer the user based on the following context and navigate the user to open the right page number to know more.

Context:
{context}
"""

    response = openai_client.create_chat_completion(
        model="gpt-3.5-turbo-16k",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query},
        ],
    )

    return response.choices[0].message.content
