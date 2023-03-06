import numpy as np
import matplotlib.pyplot as plt

amount = 10
x = np.arange(0, amount, 1)

def insert_sort(lst):
    # i 代表特插入元素的索引
    for i in range(1, len(lst)):
        temp = lst[i]  # temp代表待插入的元素
        j = i - 1      # j 代表已排序区域的元素索引
        while(j >= 0):
            if(temp < lst[j]):
                lst[j + 1] = lst[j]

                print(lst)
                
                plt.bar(x, lst)
                plt.pause(1)
                plt.clf()

            else:
                break # 退出循环，减少比较次数

            j = j - 1
        
        lst[j + 1] = temp
        print("lst: ", lst)

lst = np.random.randint(0, 100, amount)
insert_sort(lst)
plt.show()
print(lst)