# Pijja Palace is one of LA's newest and trendiest resturants offering Indian and Italian fusion. Here are their pizza customizations
# Kabir Sawlani

# These are the pizza toppings Pijja Palace currently offers
toppings = [
    "Tandori Onions", "Roasted Garlic", "Bell Peppers Jalfrezi", 
    "Stinger Chiles", "Roasted Fresnos", "Spicy Pepperoni", 
    "Homemade Goan Sausage", "Chicken Tikka", "Kadai Paneer", 
    "Baingan Tawa Fry", "Curry Leaf Ranch", "Yogurt Stilton"
]

# And here are their prices
prices = [2, 2, 3, 2, 2, 4, 5, 5, 5, 4, 2, 2]

# Let's see how many toppings are priced at $2
num_two_dollar_toppings = prices.count(2)
print("Number of $2 toppings: " + str(num_two_dollar_toppings))

# Counting the total number of toppings we have
num_toppings = len(toppings)
print("We offer " + str(num_toppings) + " different kinds of pizza toppings!")
print()  # Just adding a space for clarity

# Pairing up the toppings with their prices
pizza_and_prices = [
    [2, "Tandori Onions"], [2, "Roasted Garlic"], [3, "Bell Peppers Jalfrezi"],
    [2, "Stinger Chiles"], [2, "Roasted Fresnos"], [4, "Spicy Pepperoni"], 
    [5, "Homemade Goan Sausage"], [5, "Chicken Tikka"], [5, "Kadai Paneer"], 
    [4, "Baingan Tawa Fry"], [2, "Curry Leaf Ranch"], [2, "Yogurt Stilton"]
]

# Displaying the current list of toppings with prices
print("Toppings and Prices: " + str(pizza_and_prices))

# Organizing toppings from cheapest to priciest
pizza_and_prices.sort()

# Just checking out the cheapest and priciest toppings
cheapest_topping = pizza_and_prices[0]
priciest_topping = pizza_and_prices.pop(-1)
print("Priciest topping: " + str(priciest_topping))

# Introducing a new topping to the mix!
pizza_and_prices.append([3, "Chili Lime Pineapple"])
pizza_and_prices.sort()  # Keeping things in order

# Grabbing the three most affordable toppings
three_cheapest = pizza_and_prices[:3]
print("Three cheapest toppings: " + str(three_cheapest))
