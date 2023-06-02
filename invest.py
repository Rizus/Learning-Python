

# Мой вариант
def invest(amount, rate, years):
    for i in range(1, years + 1):
        x = (amount * rate / 100)
        amount = x + amount
        print(f"year {i}: ${amount:.2f}")
    return


# Решение из книги
# def invest(amount, rate, years):
#     """Display year on year growth of an initial investment"""
#     for year in range(1, years + 1):
#         amount = amount * (1 + rate)
#         print(f"year {year}: ${amount:,.2f}")


# invest(100, .05, 4)


amount = float(input("Enter the amount: "))
rate = float(input("Enter the rate: "))
years = int(input("Enter the years: "))

invest(amount, rate, years)
