import sys

def load_case():
    n_people = int(input())
    people = []
    for _ in range(n_people):
        people.append(int(input()))
    return people

def get_cross_candidates(before):
    candidates = []
    l = len(before)
    if l > 3:
        t1 = before[1] + before[0] + before[l - 1] + before[1]
        t2 = before[l - 1] + before[0] + before[l - 2] + before[0]
        if t1 <= t2:
            candidates = [(before[0], before[1]), (before[0],), (before[l - 2], before[l - 1]), (before[1],)]
        else:
            candidates = [(before[0], before[l - 2]), (before[0],), (before[0], before[l - 1]), (before[0],)]
        before.pop()
        before.pop()
    elif l == 3:
        candidates = [(before[0], before[1]), (before[0],), (before[0], before[2])]
        before[:] = []
    elif l == 2:
        candidates = [(before[0], before[1])]
        before[:] = []
    else:
        candidates = [(before[0],)]
        before[:] = []
    return candidates

def cross_strategy(people):
    order = []
    before = sorted(people)
    seconds = 0
    while len(before):
        candidates = get_cross_candidates(before)
        for c in candidates:
            seconds += max(c)
            order.append(c)
    return seconds, order

if __name__ == '__main__':
    cases = int(input())
    for c in range(cases):
        input()  # Discard the empty line
        people = load_case()
        seconds, order = cross_strategy(people)
        print(seconds)
        for p in order:
            print(" ".join(map(str, p)))
        if c < cases - 1:
            print('')  # Empty line after each case except the last one
