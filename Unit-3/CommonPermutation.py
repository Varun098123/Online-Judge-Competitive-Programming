import sys

def main():
    for line in sys.stdin:
        count1 = [0] * 128
        count2 = [0] * 128
        
        for c in line.strip():
            count1[ord(c)] += 1
        
        line = sys.stdin.readline()
        for c in line.strip():
            count2[ord(c)] += 1
        
        for i in range(128):
            for _ in range(min(count1[i], count2[i])):
                sys.stdout.write(chr(i))
        
        sys.stdout.write("\n")

if __name__ == "__main__":
    main()
