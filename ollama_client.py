
from ollama import chat

response = chat(
    model='gemma3:270m',
    messages=[{'role': 'user', 'content': 'Hello!'}],
)
print(response.message.content)