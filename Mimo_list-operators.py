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