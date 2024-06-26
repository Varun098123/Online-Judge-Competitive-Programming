"""
Program Name = 3n + 1 Problem

Name  = Varun Kotgire
class = TYCSE-A
Roll  = 79
Batch = 4
"""

import numpy as np

# Read input and convert to int32 using numpy
i, j = input().split()
i = np.int32(i)
j = np.int32(j)

all_count = []

for num in range(i, j+1):
    count = np.int32(1)
    while num > 1:
        if num % 2 == 0: # if num is even then do num = num / 2
            num = num / 2
            count += 1
        else: # if num is odd then do num = (num * 3) + 1
            num = (num * 3) + 1
            count += 1
    all_count.append(count)

output = max(all_count)

print(i, j, output)

"""
Output

0 10
0 10 20

date=7-3-24
"""
