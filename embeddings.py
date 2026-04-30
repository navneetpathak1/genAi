from openai import OpenAI
from dotenv import load_dotenv
import tiktoken

load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Sample text for encoding
text = """
Artificial Intelligence is transforming the world by enabling machines
to learn from data, make decisions, and improve over time.
"""
 
# Choose encoding
encoding = tiktoken.encoding_for_model("gpt-4o")

# Encode the text
tokens = encoding.encode(text)

# Decode back (optional)
decoded_text = encoding.decode(tokens)

# Print results
print("Original Text:\n", text)
print("\nEncoded Tokens:\n", tokens)
print("\nNumber of Tokens:", len(tokens))
print("\nDecoded Text:\n", decoded_text)