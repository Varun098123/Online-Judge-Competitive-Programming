def cycle(n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 1
    if n % 2 == 0:
        memo[n] = 1 + cycle(n // 2, memo)
    else:
        memo[n] = 1 + cycle(3 * n + 1, memo)
    return memo[n]

def solve(i, j, memo):
    return max(cycle(n, memo) for n in range(i, j + 1))

if __name__ == '__main__':
    memo = {}
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")
    
    for line in data:
        i, j = map(int, line.split())
        ans = solve(min(i, j), max(i, j), memo)
        print(f'{i} {j} {ans}')
