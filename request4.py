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

    # Check if the currency symbols exist in the rates dictionary
    if 'INR' in data['rates'] and currency_symbol in data['rates']:
        inr_value = data['rates']['INR']
        currency_value = data['rates'][currency_symbol]
        return inr_value, currency_value
    else:
        raise ValueError("Invalid currency symbol")

# Example usage
def main():
    currency_symbol = 'USD'
    inr_value, currency_value = get_currency_value(currency_symbol)
    print(f"The value of INR is: {inr_value}")
    print(f"The value of {currency_symbol} is: {currency_value}")

# Call the main function
main()