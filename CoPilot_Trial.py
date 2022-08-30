import datetime

#plot a graph using matplotlib
import matplotlib.pyplot as plt
import numpy as np

#plot a graph using matplotlib
def plot_graph(x, y):
    plt.plot(x, y)
    plt.show()

x= [1,2,3,4,5]
y= [1,2,3,4,5]
plot_graph(x, y)



def calculate_days_between_dates(begin, end):
    begin = datetime.datetime.strptime(begin, "%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    return abs((begin - end).days)

print(calculate_days_between_dates("2019-01-01", "2019-10-02"))

def sort_list(list):
    return sorted(list)

print(sort_list([9, 5, 3, 7, 6, 8, 2, 1, 4, 10]))




