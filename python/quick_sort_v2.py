import matplotlib.pyplot as plt
import numpy as np

amount = 10
x = np.arange(0, amount, 1)

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    print("swap: ", lst, "i = ", i, "j = ", j)

def partition(lst, low, high):
    pv = lst[low]
    i = low
    j = high
    while(i < j):
        while(i < j and lst[j] > pv): j = j - 1
        while(i < j and lst[i] <= pv): i = i + 1
        swap(lst, i, j)
    swap(lst, low, j)
    print("lst", lst)
    return j

def quick_sort_v2(lst, low, high):
    if(low >= high):
        return
    p = partition(lst, low, high)
    quick_sort_v2(lst, low, p-1)
    quick_sort_v2(lst, p+1, high)

def animation(x, lst):
    plt.bar(x, lst)
    plt.pause(0.5)
    plt.clf()

# lst = [5, 3, 7, 2, 9, 8, 1, 4]
lst = np.random.randint(0, 100, amount)
print("origin: ", lst)
quick_sort_v2(lst, 0, len(lst) - 1)
plt.show()
print("result: ", lst)