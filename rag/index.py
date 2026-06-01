from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
pdf_path = Path(__file__).parent / "node.pdf"

#Load this file in python program
loader = PyPDFLoader(pdf_path)
docs = loader.load()


#Split the docs nto small chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=400)  
chunks=text_splitter.split_documents(documents=docs)

#vector embedding  
print(docs[12])


#vector embedding
embedding_model=OpenAIEmbeddings(
    model="text-embedding-3-large",
)

vector_store=QdrantVectorStore.from_documents(
    document=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning rag"
)
print("Indexing of document done..")
