#sort a list of integers in ascending order
def sort_list(list_of_ints):
    for i in range(len(list_of_ints)):
        for j in range(len(list_of_ints)):
            if list_of_ints[i] < list_of_ints[j]:
                list_of_ints[i], list_of_ints[j] = list_of_ints[j], list_of_ints[i]
    return list_of_ints
#find the maximum value in a list of integers
def find_max(list_of_ints):
    max_value = list_of_ints[0]
    for i in range(len(list_of_ints)):
        if list_of_ints[i] > max_value:
            max_value = list_of_ints[i]
    return max_value
#find the minimum value in a list of integers
def find_min(list_of_ints):
    min_value = list_of_ints[0]
    for i in range(len(list_of_ints)):
        if list_of_ints[i] < min_value:
            min_value = list_of_ints[i]
    return min_value
print("sort a list of integers in ascending order")
print(sort_list([1,7,2,4,8,6,9,3,10]))
print("find the maximum value in a list of integers")
print(find_max([1,7,2,4,8,6,9,3,10]))
print("find the minimum value in a list of integers")
print(find_min([1,7,2,4,8,6,9,3,10]))

import datetime

#find number of days between two dates
def days_between_dates(year1, month1, day1, year2, month2, day2):
    date1 = datetime.date(year1, month1, day1)
    date2 = datetime.date(year2, month2, day2)
    return abs(date2 - date1).days
print("find number of days between two dates")
print(days_between_dates(2016, 1, 1, 2016, 12, 31))

#plot a graph using matplotlib
import matplotlib.pyplot as plt
import numpy as np

def plot_graph(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.show()

x = [1,5,3,2]
y = [1,7,4,3]
plot_graph(x, y)






