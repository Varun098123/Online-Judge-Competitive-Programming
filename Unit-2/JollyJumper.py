while True:
    try:
        sequence = list(map(int, input().split()))
    except EOFError:
        break
        
    length = sequence[0]
    differences = [0] * length
    
    for i in range(2, len(sequence)):
        diff = abs(sequence[i] - sequence[i-1])
        if 0 < diff < length:
            differences[diff] = 1
        
    print("Jolly" if sum(differences) == length - 1 else "Not jolly")
