def ac():
    if n != m:
        return False
    for i in range(m):
        if A[i] != B[i]:
            return False
    return True

def pe():
    digits_a = ''.join(c for row in A for c in row if c.isdigit())
    digits_b = ''.join(c for row in B for c in row if c.isdigit())
    return digits_a == digits_b

def judge():
    if ac():
        return "Accepted"
    elif pe():
        return "Presentation Error"
    else:
        return "Wrong Answer"

cases = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    A = [input() for _ in range(n)]
    
    m = int(input())
    B = [input() for _ in range(m)]
    
    print(f"Run #{cases + 1}: {judge()}")
    cases += 1
