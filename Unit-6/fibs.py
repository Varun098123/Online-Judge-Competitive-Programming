import sys
import math

# Function to generate Fibonacci numbers up to n
def fibonacci_up_to(n):
    f = []
    a, b = 1, 2
    f.append(a)
    while b <= n:
        f.append(b)
        a, b = b, a + b
    return f

def main():
    f = fibonacci_up_to(10**100)  # Generate Fibonacci numbers up to 10^100
    input_lines = sys.stdin.read().strip().split('\n')
    
    for line in input_lines:
        a, b = map(int, line.split())
        if a == 0 and b == 0:
            break
        
        i = 0
        while i < len(f) and f[i] < a:
            i += 1
        
        count = 0
        while i < len(f) and f[i] <= b:
            count += 1
            i += 1
        
        print(count)

if __name__ == "__main__":
    main()
