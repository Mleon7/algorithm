import random
import matplotlib.pyplot as plt

amount = 50
PAUSE_TIME = 0.01

random.seed("ABC")
numbers = [random.randint(0, 1000) for _ in range(amount)]

def merge_sort(numbers_list, left, right):
    # base case
    if left >= right:
        return
    
    # find the middle
    mid = (left + right) // 2

    plt.bar(list(range(amount)), numbers_list)
    plt.pause(PAUSE_TIME)
    plt.clf()

    # split recursive into left and right halves
    merge_sort(numbers_list, left, mid)
    merge_sort(numbers_list, mid + 1, right)

    # merge the two results
    merge(numbers_list, left, right, mid)

    plt.bar(list(range(amount)), numbers_list)
    plt.pause(PAUSE_TIME)
    plt.clf()



def merge(numbers_list, left, right, mid):
    # copy left and right halves into new lists
    left_cpy = numbers_list[left:mid + 1]
    right_cpy = numbers_list[mid + 1:right + 1]

    # counters indicating the progress
    l_counter, r_counter = 0, 0
    sorted_counter = left

    # while we reach the end of one half
    while l_counter < len(left_cpy) and r_counter < len(right_cpy):

        # pick the smaller element and put it into the next position
        # and progress the counters
        if left_cpy[l_counter] <= right_cpy[r_counter]:
            numbers_list[sorted_counter] = left_cpy[l_counter]
            l_counter += 1
        else:
            numbers_list[sorted_counter] = right_cpy[r_counter]
            r_counter += 1

        sorted_counter += 1

    while l_counter < len(left_cpy):
        numbers_list[sorted_counter] = left_cpy[l_counter]
        l_counter += 1
        sorted_counter += 1
    
    while r_counter < len(right_cpy):
        numbers_list[sorted_counter] = right_cpy[r_counter]
        r_counter += 1
        sorted_counter += 1

print(numbers)
merge_sort(numbers, 0, len(numbers)-1)
print(numbers)
plt.bar(list(range(amount)), numbers)
plt.show()