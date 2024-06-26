import sys
import math

def main():
    input = sys.stdin.read().strip().split('\n')
    t = int(input[0])
    results = []
    
    for line in input[1:t+1]:
        x, y = map(int, line.split())
        L = y - x
        steps = 0
        n = int(math.sqrt(L))
        steps = n
        L -= n * (n + 1) // 2
        
        while L > 0:
            while n * (n + 1) // 2 > L:
                n -= 1
            
            if n * (n + 1) // 2 == L:
                L = 0
                steps += n
            else:
                L -= n
                steps += 1
        
        results.append(steps)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
