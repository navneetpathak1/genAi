from mem0 import Memory
from openai import OpenAI

OPENAI_API_KEY = "sk-xx"

QDRANT_HOST = "localhost"

config = {
    "embedder": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "text-embedding-3-small"
        }
    },

    "llm": {
        "provider": "openai",
        "config": {
            "api_key": OPENAI_API_KEY,
            "model": "gpt-4o-mini"
        }
    },

    "vector_store": {
        "provider": "qdrant",
        "config": {
            "host": QDRANT_HOST,
            "port": 6333
        }
    },

    "graph_store": {
        "provider": "neo4j",
        "config": {
            "url": "bolt://localhost:7687",
            "username": "neo4j",
            "password": "password"
        }
    }
}

memory = Memory.from_config(config)

openai_client = OpenAI(api_key=OPENAI_API_KEY)


def chat(message):

    # Retrieve related memories
    mem_result = memory.search(
        query=message,
        user_id="p123"
    )

    # Extract memory text
    memories = []

    for item in mem_result["results"]:
        memories.append(item["memory"])

    memory_context = "\n".join(memories)

    # Store current message
    memory.add(message, user_id="p123")

    # Inject memories into prompt
    messages = [
        {
            "role": "system",
            "content": f"""
You are a helpful AI assistant.

Relevant past memories:
{memory_context}
"""
        },
        {
            "role": "user",
            "content": message
        }
    ]

    result = openai_client.chat.completions.create(
        model="gpt-4.1",
        messages=messages
    )

    assistant_reply = result.choices[0].message.content

    return assistant_reply


while True:

    message = input(">> ")

    if message.lower() == "exit":
        break

    print(chat(message))