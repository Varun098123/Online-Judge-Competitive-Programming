import sys

def main():
    fac = [1] * 13
    for i in range(1, 13):
        fac[i] = i * fac[i - 1]
    
    results = []
    for line in sys.stdin:
        n, k = map(int, line.split())
        if n == 0 and k == 0:
            break
        
        product = 1
        factors = list(map(int, input().split()))
        for n_i in factors:
            product *= fac[n_i]
        
        result = fac[n] // product
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
