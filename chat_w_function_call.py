import openai
import os

# Read the OpenAI Api_key
openai.api_key = open("OPENAI_API_KEY.txt", "r").read().strip()


def start_chat_completion(prompt):
    # Define the parameters for the chat completion API call
    parameters = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': prompt}],
        'max_tokens': 100,
        'temperature': 0.7,
        'n': 1,
        'stop': None
    }

    # Call the OpenAI API to get the chat completion response
    response = openai.Completion.create(**parameters)

    # Extract the generated message from the API response
    message = response.choices[0].message

    # Return the generated message content
    return message['content']

# Example usage
def main():
    prompt = "What is the weather like today?"
    completion = start_chat_completion(prompt)
    print(completion)

# Call the main function
main()