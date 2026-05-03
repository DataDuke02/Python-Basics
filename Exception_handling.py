#try throw except finally
print("Welcome to Zomoto!")
try:
    numer_of_items = int(input("How many items?: "))
    total_price = 200 * numer_of_items
    average_price = total_price / numer_of_items
    print("Average Price :",average_price)
except ZeroDivisionError:
    print("You can't order 0 items.")
finally:
    print("Alaways exceute")

print("next code block")
