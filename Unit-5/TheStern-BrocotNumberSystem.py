while True:
    n, m = map(int, input().split())
    if n == 0:
        break
    if n == 1 and m == 1:
        break

    l1, l2 = 0, 1
    m1, m2 = 1, 1
    r1, r2 = 1, 0

    while m1 != n or m2 != m:
        if m1 * m > m2 * n:  # move left
            t1, t2 = m1, m2
            m1 += l1
            m2 += l2
            r1, r2 = t1, t2
            print("L", end="")
        else:  # move right
            t1, t2 = m1, m2
            m1 += r1
            m2 += r2
            l1, l2 = t1, t2
            print("R", end="")
    print()
