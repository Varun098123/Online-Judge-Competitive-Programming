def main():
    t = int(input().strip())
    input()  # Consume the newline after t
    while t > 0:
        penalty_map = {}
        solved_map = {}
        accumulate_map = {}
        while True:
            try:
                line = input().strip()
                if not line:
                    break
                id, qId, time, L = map(str, line.split())
                id, qId, time = int(id), int(qId), int(time)
                if id not in solved_map:
                    solved_map[id] = set()
                    penalty_map[id] = 0
                    accumulate_map[id] = [0] * 10
                if qId in solved_map[id]:
                    continue
                if L == 'C':
                    penalty_map[id] += time
                    penalty_map[id] += accumulate_map[id][qId]
                    solved_map[id].add(qId)
                elif L == 'I':
                    accumulate_map[id][qId] += 20
            except EOFError:
                break
        res = [(k, len(v), penalty_map[k]) for k, v in solved_map.items()]
        res.sort(key=lambda x: (-x[1], x[2], x[0]))

        for id, solved, penalty in res:
            print(id, solved, penalty)
        if t > 1:
            print()

        t -= 1

if __name__ == "__main__":
    main()
