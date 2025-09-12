def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price

price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))


total = calculate_discount(price, discount_percent)

print("Final price:", total)
