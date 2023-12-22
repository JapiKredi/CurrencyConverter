tools = [
    {
        "type": "function",
        "function": {
            "name": "get_currency_symbol",
            "description": "Get the current currency symbol",
            "parameters": {
                "type": "object",
                "properties": {
                    "currency_symbol": {
                        "type": "string",
                        "description": "The currency symbol, e.g. USD for US Dollar"
                    }
                },
                "required": ["currency_symbol"]
            }
        }
    }
]
