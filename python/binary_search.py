def binary_search(a, t):
    """
    Binary search function, returns the index of the target element if found, else returns -1
    """
    l = int(0) 
    r = len(a) - 1 
    m = int(0)
    while l <= r:
        m = (l + r) // 2
        if a[m] == t:
            return m
        elif a[m] > t:
            r = m - 1
        else:
            l = m + 1
    return -1

# Test the binary search function
array = [1, 5, 8, 11, 19, 22, 31, 35, 40, 45, 48, 49, 50]
target = 48
idx = binary_search(array, target)
print(idx)
