import sys

for line in sys.stdin:
    A = list(map(int, line.strip().split()))
    n = len(A)
    print(*A)

    flip = []
    for i in range(n):
        idx = n - i - 1
        for j in range(n - i):
            if A[idx] < A[j]:
                idx = j
        if idx == n - i - 1:
            continue
        if idx:
            flip.append(n - idx)
            A[:idx+1] = reversed(A[:idx+1])
        flip.append(i + 1)
        A[:n-i] = reversed(A[:n-i])
    
    print(*flip, 0)
