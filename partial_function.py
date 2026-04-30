from functools import partial

# Step 1 : Define the original function
def calculate_price(base_price, tax_rate):
    return base_price * (1 + tax_rate)

# Step 2 : Create a partially applied function with GST fixed
price_with_gst = partial(calculate_price,tax_rate=0.18)

# Step 3 : Now use it without passing tax_rate again
print(price_with_gst(1000))  # 1180.0
print(price_with_gst(500))   # 590.0
