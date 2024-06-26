import sys

for line in sys.stdin:
    n = int(line.strip())
    tmp = 1
    i = 1
    while True:
        if tmp % n == 0:
            break
        tmp = tmp * 10 + 1
        tmp %= n
        i += 1
    print(i)
