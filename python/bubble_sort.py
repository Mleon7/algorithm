import matplotlib.pyplot as plt
import numpy as np

amount = 10

def bubble_sort(lst): 
    n = len(lst)
    for i in range(n):
        is_swapped = False # 判断是否发生了交换
        print(i, "轮：")

        for j in range(0, n-i-1):
            print("比较次数" , j)

            plt.bar(x, lst)
            plt.pause(0.1)
            plt.clf()

            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                is_swapped = True

        if (not is_swapped): break

def bubble_sort_v2(lst):
    n = len(lst) - 1
    while(True):
        print("n=", n, ", lst=", lst)
        last = 0  # 表示最后一次交换索引位置
        for i in range(0, n):
            print("比较次数", i)
            # plt.bar(x, lst)
            # plt.pause(0.1)
            # plt.clf()
            if(lst[i] > lst[i+1]):
                lst[i], lst[i+1] = lst[i+1], lst[i]
                last = i # 只要发生了交换，就更改last
        
        n = last
        if(n == 0): break


lst = np.random.randint(0, 100, amount)
# lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = np.arange(0, amount, 1)
bubble_sort_v2(lst)

plt.show()
plt.clf()
print("lst", lst)