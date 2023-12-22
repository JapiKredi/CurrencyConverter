import requests
import json

# Read the Api_key
API_KEY = open("API_Key.txt", "r").read().strip()

def main():
    url = f"http://api.exchangeratesapi.io/latest?access_key={API_KEY}"
    response = requests.get(url, verify=False)
    if response.status_code != 200:
        print("Status Code:", response.status_code)
        raise Exception("There was an error!")

    print("Header:", response.headers['Content-Type'])
    data = response.json()
    print("JSON data:", data)


if __name__ == "__main__":
    main()

    
