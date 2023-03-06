import matplotlib.pyplot as plt
import numpy as np

amount = 10
x = np.arange(0, amount, 1)

def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]
    print("swap: ", lst, "i = ", i, "j = ", j)

def partition(lst, low, high):
    pv = lst[high]
    i = low
    for j in range(low, high, 1):
        if(lst[j] < pv):
            if(i != j):
                swap(lst, i, j)
            i = i + 1
        # animation(x, lst)

    if(i != high):
        swap(lst, high, i)
    print("i=", i, "lst", lst)
    # animation(x, lst)

    return i


def quick_sort_v1(lst, low, high):
    if(low >= high):
        return
    p = partition(lst, low, high)
    quick_sort_v1(lst, low, p-1)
    quick_sort_v1(lst, p+1, high)

def animation(x, lst):
    plt.bar(x, lst)
    plt.pause(0.5)
    plt.clf()

# lst = [5, 3, 7, 2, 9, 8, 1, 4]
lst = np.random.randint(0, 100, amount)
print("origin: ", lst)
quick_sort_v1(lst, 0, len(lst) - 1)
plt.show()
print("result: ", lst)