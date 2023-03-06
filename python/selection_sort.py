import matplotlib.pyplot as plt
import numpy as np

amount = 10
x = np.arange(0, amount, 1)

def selection_sort(lst):
    for i in range(0, len(lst)):
        # i代表每轮选择最小元素要交换到的目标索引
        s = i; # s 代表最小元素的索引值

        # 比较大小，更小元素的索引值赋给s，最终 s = 最小元素的索引值
        for j in range(s+1, len(lst)):
            if(lst[s] > lst[j]):
                s = j
            plt.bar(x, lst)
            plt.pause(0.1)
            plt.clf()
        
        # 若目标元素引值 != 最小元素的索引值，交换两个值
        if (s != i):
            lst[s], lst[i] = lst[i], lst[s]
        
        print("lst: " , lst)


lst = np.random.randint(0, 100, amount)
selection_sort(lst)
plt.show()
print(lst)