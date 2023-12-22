import requests
import json


API_KEY = "YOUR_API_KEY"  # Replace with your actual API key

# Read the Api_key
API_KEY = open("OpenAI_API_Key.txt", "r").read().strip()


def main():
    response=requests.get('https://api.exchangeratesapi.io/latest')
    if response.status_code !=200:
        print("Status Code :",response.status_code)
        raise Exception("There was error!")
    
    print("Header:",response.headers['Content-Type'])
    data=response.json()
    print("JSON data",data)
    
    
    
if __name__ == "__main__":
    main()
    
