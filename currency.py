from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    result = c.convert(from_currency, to_currency, amount)
    return result

amount = float(input("Enter the amount: "))
from_currency = input("From Currency: ").upper()
to_currency = input("To Currency: ").upper()

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
