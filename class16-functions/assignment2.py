import statistics
'''Averages of a list '''

# Instructions
# Write a function that takes a list of numbers as input and returns the average of all the numbers in that list. Have fun and be sure to test test test!

random_nums = [82, 45, 68, 72, 49]

def avg_the_nums(random_nums):
    return sum(random_nums)/len(random_nums)
    
print(avg_the_nums(random_nums))
