class CurrencyConverter:
    SICKLE_TO_KNUT = 29
    GALLEON_TO_SICKLE = 17
    VALID_COINS = ["galleon", "sickle", "knut"]

    @staticmethod
    def convert_to_knuts(galleons=0, sickles=0, knuts=0):
        return galleons * CurrencyConverter.GALLEON_TO_SICKLE * CurrencyConverter.SICKLE_TO_KNUT + sickles * CurrencyConverter.SICKLE_TO_KNUT + knuts

    @staticmethod
    def convert_to_sickles(knuts):
        return round(knuts / CurrencyConverter.SICKLE_TO_KNUT, 2)

    @staticmethod
    def convert_to_galleons(knuts):
        return round(knuts / (CurrencyConverter.SICKLE_TO_KNUT * CurrencyConverter.GALLEON_TO_SICKLE), 2)

def main():
    print("Welcome to the Harry Potter Currency Converter!")
    print("This program converts a bag of coins into your desired currency.")

    coin_types_input = input("Which types of coins do you have? (Galleon, Sickle, Knut) Enter all that apply, separated by commas: ")
    coin_types = [coin.strip().lower() for coin in coin_types_input.split(',')]

    while not all(coin in CurrencyConverter.VALID_COINS for coin in coin_types):
        print("Invalid coin type entered. Please enter only Galleon, Sickle, or Knut.")
        coin_types_input = input("Which types of coins do you have? (Galleon, Sickle, Knut) Enter all that apply, separated by commas: ")
        coin_types = [coin.strip().lower() for coin in coin_types_input.split(',')]

    amounts = {}
    for coin_type in coin_types:
        amount = -1
        while amount < 0:
            try:
                amount = int(input(f"Enter the number of {coin_type.capitalize()}s: "))
                if amount < 0:
                    print("Please enter a non-negative number.")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        amounts[coin_type] = amount

    while True:
        target_currency = input("What currency do you want to convert to? (Galleons, Sickles, Knuts): ").lower().rstrip('s')
        if target_currency in CurrencyConverter.VALID_COINS:
            break
        print("Invalid target currency. Please enter Galleons, Sickles, or Knuts.")

    total_knuts = CurrencyConverter.convert_to_knuts(
        amounts.get("galleon", 0),
        amounts.get("sickle", 0),
        amounts.get("knut", 0)
    )

    conversion_functions = {
        "galleon": CurrencyConverter.convert_to_galleons,
        "sickle": CurrencyConverter.convert_to_sickles,
        "knut": lambda knuts: knuts
    }

    result = conversion_functions[target_currency](total_knuts)
    print(f"The total amount in {target_currency.capitalize()}s is: {result}")

if __name__ == "__main__":
    main()