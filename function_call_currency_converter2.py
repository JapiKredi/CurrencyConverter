{
        "name": "get_exchange_rate",
        "description": "Convert currency from one type to another and get the exchange rate",
        "parameters": {
            "type": "object",
            "properties": {
                "fromCurrency": {
                    "type": "string",
                    "description": "The currency you want to convert from (ISO 4217 code)"
                },
                "toCurrency": {
                    "type": "string",
                    "description": "The currency you want to convert to (ISO 4217 code)"
                },
                "amount": {
                    "type": "number",
                    "description": "The amount you want to convert (optional)"
                }
            },
            "required": ["fromCurrency", "toCurrency"]
        },
        "extraInfo": {
            "method": "post",
            "functionUrl": "https://openfunctions.consolex.ai/api/get_exchange_rate"
        }
    }

