import requests
import json

# Read the Api_key
API_KEY = open("API_Key.txt", "r").read().strip()

def get_currency_value(currency_symbol):
    url = f"http://api.exchangeratesapi.io/latest?access_key={API_KEY}"
    response = requests.get(url, verify=False)
    if response.status_code != 200:
        print("Status Code:", response.status_code)
        raise Exception("There was an error!")

    data = response.json()

    # Check if the currency symbol exists in the rates dictionary
    if currency_symbol in data['rates']:
        currency_value = data['rates'][currency_symbol]
        return currency_value
    else:
        raise ValueError("Invalid currency symbol")

# Example usage
currency_symbol = 'INR'
currency_value = get_currency_value(currency_symbol)
print(f"The value of {currency_symbol} is: {currency_value}")



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

    # Select the value of 'INR'
    inr_value = data['rates']['INR']
    print("INR value:", inr_value)


if __name__ == "__main__":
    main()
