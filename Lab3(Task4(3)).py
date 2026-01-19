# Currency rates to KZT
currency_rates = {
    "USD": 450,
    "EUR": 490,
    "RUB": 5,
    "CNY": 65
}

# Ask user for currency
currency = input("Валютаны енгізіңіз (мысалы: USD, EUR): ").upper()

# Show rate
if currency in currency_rates:
    print(f"1 {currency} = {currency_rates[currency]} теңге")
else:
    print("Бұл валюта тіркелмеген.")

