# https://aismartcode.vercel.app get promo-code with discount for advanced course

# 1. Get data from URL
# Docs: https://beautiful-soup-4.readthedocs.io/en/latest/#navigating-the-tree

# 2. Split data into chunks
# 3–4. Generate embeddings and store chunks in ChromaDB
# 5–9. RAG workflow
# 6–7. Retrieve relevant chunks using vector similarity search
# 8–9. Build prompt and invoke the LLM
# Define and compile the LangGraph workflow
# Run the RAG pipeline

# Create the chat model (the "brain" that generates answers)
llm = ChatOpenAI(
    model=os.getenv("CHAT_MODEL", "llama3.1"),                  # chat model
    base_url=os.getenv("LLM_API_BASE", "http://127.0.0.1:11434/v1"),  # local Ollama
    api_key=os.getenv("LLM_API_KEY", "ollama"),                 # dummy key (required by client)
    temperature=0,                                              # deterministic output
)