import openai
from dotenv import load dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY.txt")

messages = [
    {"role": "system", "content": "You are a developer."},
    {"role": "user", "content": "Hello, I need help with my code."},
    {"role": "assistant", "content": "Sure, I'd be happy to help. What's the problem?"},
]
response = openai.ChatCompletion.create(
    model = 'gpt3.5-turbo',
    messages



