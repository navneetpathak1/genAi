from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore

file_path = "./myPDF.pdf"

# Load PDF
loader = PyPDFLoader(file_path)
docs = loader.load()

# Split text
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
split_docs = text_splitter.split_documents(docs)

# Embeddings
embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
)

# Create vector store (auto-creates collection)
# vector_store = QdrantVectorStore.from_documents(
#     documents=split_docs,
#     embedding=embeddings,
#     url="http://localhost:6333",
#     collection_name="learning"
# )


# Retrieval =>
retrieval = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="learning",
    embedding=embeddings
)

relevant_chunks = retrieval.similarity_search(
    query="what is langchain"
)


SYSTEM_PROMPT = "You are a helpful AI assistant who respond based on context." \
"Context" \
"{relevant_chunks}"






