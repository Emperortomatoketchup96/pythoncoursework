### Exploring Variables, Data Types, and Expressions ###

# Part 1. Numeric Variables & Arithmetic
# Requirement: 3 numeric variables and 1 arithmetic operation
pizza_price = 15.00
topping_price = 2.25
quantity = 2

# Calculation: (Base price + Toppings) * how many pizzas
subtotal = (pizza_price + topping_price) * quantity

print(f"The subtotal for {quantity} pizzas is ${subtotal}.")


# Part 2. String Variables & Manipulation
# Requirement: A string manipulated using methods or concatenation
first_name = "jordan"
last_name = "smith"

# Concatenation and .title() method to capitalize names
full_name = first_name.title() + " " + last_name.title()

# Using .upper() for emphasis
welcome_message = "welcome to the Pizza Port"
formatted_message = welcome_message.upper()

print(f"User: {full_name}")
print(f"Status: {formatted_message}!")


# Part 3. Boolean Expressions
# Requirement: Compare two values and print the result
budget = 40.00
is_under_budget = subtotal <= budget

print(f"Is the purchase within our ${budget} budget? {is_under_budget}")


# Part 4. Modulo 
# Checking if the quantity of pizzas is an even number
is_even_order = (quantity % 2) == 0
print(f"Is the order quantity an even number? {is_even_order}")