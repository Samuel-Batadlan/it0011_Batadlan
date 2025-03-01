exchange_rates = {
    "Euro": 0.931936166,
    "U.K. Pound Sterling": 0.827816452,
    "Japanese Yen": 131.1994943,
    "Australian Dollar": 1.439773864,
    "Swiss Franc": 0.920289009,
    "Canadian Dollar": 1.342307659,
    "New Zealand Dollar": 1.583390808,
    "Turkish Lira": 18.83402666,
    "Nigerian Naira": 460.386436,
    "Indian Rupee": 82.61621692,
    "Mexican Peso": 18.93036821,
    "South Korean Won": 1260.46907,
    "Chinese Yuan": 6.787890099,
    "Brazilian Real": 5.197907606,
    "South African Rand": 17.71922356,
    "Russian Rouble": 73.13025012,
    "Philippine Peso": 54.81472581
}

usd_amount = float(input("Enter the amount in US Dollars: "))

desired_currency = input("Enter the currency you want to convert to: ")

if desired_currency in exchange_rates:
    converted_amount = usd_amount * exchange_rates[desired_currency]
    
    print("\nConversion Summary:")
    print(f"USD: {usd_amount} → {desired_currency}: {converted_amount:.2f}")
else:
    print("Sorry, we couldn't find that currency.")

