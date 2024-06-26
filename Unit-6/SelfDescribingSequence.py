import sys

lim = 673368
f = [1, 1, 2, 2]
sz = 4

# Precompute values for f array
i = 3
while sz < lim:
    for j in range(f[i]):
        f.append(i)
        sz += 1
    i += 1

while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    
    if n < lim:
        print(f[n])
        continue
    
    x = 3
    cur = 4
    bound = 6
    while bound + x * f[x] < n:
        bound += x * f[x]
        cur += f[x]
        x += 1
    
    print(cur + (n - bound) // x)

