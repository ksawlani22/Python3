#DTLA Cuts x Loops
#Kabir Sawlani

# List of offered haircuts and their prices
haircuts = [
    "Haircut", 
    "Haircut with Beard Trim", 
    "College Student Haircut", 
    "College Student Haircut and Beard Trim", 
    "Scissor Cut", 
    "Haircut and Hot Towel Shave", 
    "Buzz Cut", 
    "Buzz Cut with Beard Trim"
]

prices = [45, 65, 39, 59, 51, 75, 41, 61]

# Sales data from last week
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculating the average price
total_price = sum(prices)
average_price = total_price / len(prices)
print("Average Price")
print(average_price)

# Applying a discount of $5 to all haircut prices
new_prices = [price - 5 for price in prices]
print("New Prices")
print(new_prices)

# Calculating the total revenue from last week
total_revenue = sum(prices[i] * last_week[i] for i in range(len(haircuts)))
print("Total Revenue: " + str(total_revenue))

# Calculating the average daily revenue
average_daily_revenue = total_revenue / 7 
print("Average Daily Revenue " + str(average_daily_revenue))

# Listing haircuts under $50 after the discount
cuts_under_50 = [haircuts[i] for i in range(len(haircuts)) if new_prices[i] < 50]
print("Cuts Under $50: " + str(cuts_under_50))
