# To explore data stored in lists, often useful to find the EXTREME VALUES: min/max
scores = [3, 6, 1, 12]

# Use max(list_name) to find the max value
scores = [3, 6, 1, 12]

print(max(scores)) # 12

# Use min(list-name) to find the min value
scores = [3, 6, 1, 12]
print(min(scores)) # 1

#Can reuse the results of min() & max() by saving them in variables
scores = [3, 6, 1, 12]
min_score = min(scores) #assigns 1 to var min_score
max_score = max(scores) #assigns 12 to var max_score

print(min_score) #1
print(max_score)#12


temperatures = [68, 60, 81]
print(max(temperatures)) #81


shares = [12, 5, 3, 7]
print(min(shares)) #3


weekly_profits = [50, 60, 70, 20]
max_profit = max(weekly_profits) #will store max value (70) inside var max_profit
print(max_profit) #70

#SORTING DATA
#Sorted lists are useful when we want to understand where individual data points, like scores, stand in relations to others

#To sort list like scores, code list_name.sort() - will change the list 
scores = [3, 6, 1, 12]
scores.sort() # will sort list in ascending order
print(scores) # 1, 3, 6, 12

#Will also sort float values and integers based on numeric values
prices = [13, 9.99, 10, 7.5]
prices.sort()
print(prices) #7.5, 9.99, 10, 13


temperatures = [-1, -3, 2]
temperatures.sort()
print(temperatures) #-3, -1, 2

#.sort() will sort strings alphabetically
names = ['Chloe', 'Ana', 'Bill']
names.sort()
print(names) #Ana, Bill, Chloe


friend_requests = [3, 1, 2]
friend_requests.sort()
print(friend_requests) #1, 2, 3


active_users = [103, 200, 140, 288]
active_users.sort()
print(active_users) #103, 140, 200, 288

sold_tickets = [7, 30, 20, 12]
print(sold_tickets) #7, 30, 20, 12
sold_tickets.sort() # sorts the list numerically
print(sold_tickets) #7, 12, 20, 30


test_points = [97, 76, 81]
test_points.sort()
print(test_points) #76, 81, 97


ingredients = [65.5, 21, 45]
ingredients.sort()
print(ingredients) #21, 45, 65.5


overview = [3, -1, 4, -2]
overview.sort()
print(overview) #-2, -1, 3, 4


destinations = ['Germany', 'Italy', 'Austria']
destinations.sort()
print(destinations) #'Austria', 'Germany', 'Italy'


#SUMMING OF DATA
#Knowing sum of #s in lists is useful when comparing diff datasets
signups_june = [30, 6, 20, 12]
signups_july = [20, 5, 100, 40]

#To calculate total of list, use sum(list_name)
signups = [30, 6, 20, 12]
print(sum(signups)) #68

#Sum also works w/ negative #s - will subtract them
quarterly_growth = [-3, 0, 0, 4]
print(sum(quarterly_growth)) #1

#To reuse the sum of a list, store the sum in variable
scores = [3, 6, 1, 12]
total = sum(scores)
print(total) #22


cart = [30, 6, 50]
print(sum(cart)) #86


points_penalties = [-3, 10]
print(sum(points_penalties)) #7


sugar = [120, 50]
total_sugar = sum(sugar)
print(total_sugar) #170