"""
Use random module with a seed of 2020 to generate 20 integers between 100 and 120 (inclusive). Then write code to calculate the median and mode.  The median is the 10th largest number. The mode is the number that occurs the most. If two or more number have the same frequency, list them all.
"""
#Import random library
import random
#Set random seed generator
random.seed(2020)
#Set Number of Integers
integers = 20
#Create a list 20 random variables through list comprehension
list_1 = [random.randrange(100,121) for _ in range(integers)]
#sort list_1 to get median manually
list_sorted = sorted(list_1)
#Manually calculate median
median = (list_sorted[9] + list_sorted[10]) / 2.0
print(f'Manually Calculated Median is {median}')
#Manually calculate mode
number_frequency = {}
for num2 in list_sorted:
    number_frequency[num2] = number_frequency.get(num2, 0) + 1
#Sort the dictionary from their values in descending order and convert to list
sorted_list = sorted(number_frequency.items(), key=lambda x:x[1], reverse=True)
#See if there are multiple modes, returns how many times mode appears, array has to be sorted
#Right click to rename multiple variables
def mult_mode(array):
#Print out mode(s)
    print('Manually Calculated Mode(s):')
#Sorted list is spliced with mult_mode to show only highest count
mode_count = mult_mode(sorted_list)
for mode in sorted_list[:mode_count]:
    print(mode[0])
                    
