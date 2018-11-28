import numpy as np

a = np.random.randint(1000, size=100)

k = 15
k %= len(a)

print(a)

def reverse(start, end):
    while start < end:
        global a
        s = a[end]
        a[end] = a[start]
        a[start] = s
        start += 1
        end -= 1

reverse(0, len(a) - k - 1) # 时间复杂度 （len(a) - k）/2
reverse(len(a) - k , len(a) - 1) # 时间复杂度 （k）/2
reverse(0, len(a) - 1) # 时间复杂度 （len(a)）/2
print(a)

# 总体时间复杂度 O（len(a)）=O（N）