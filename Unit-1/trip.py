n = int(input())

if n>0:
    trip = []
    for i in range(n):
        a = float(input())
        trip.append(a)

    total = 0
    avg = 0

    for i in range(n):
        total = total+trip[i]

    avg = total/n

    total = 0
    for i in range(n):
        if trip[i] > avg:
            total = total+(trip[i]-avg)
    print(f"${(total):.2f}")