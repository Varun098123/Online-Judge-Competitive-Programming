"""
Program : The Trip

Name  :  Varun Vishnu Kotgire
Class :  TYCSE-A
Roll  :  79
Batch :  T4
"""

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


"""
Output

4
15.00
15.01
3.00
3.01
$12.00

3
10.00
20.00
30.00
$10.00

0
"""