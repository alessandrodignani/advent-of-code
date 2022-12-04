# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 point for Rock, 2 for Paper, and 3 for Scissors
# 0 points if you lost, 3 if the round was a draw, and 6 if you won

def get_points(o, u):
    match (o, u):
        case ('A', 'X'): return 4
        case ('A', 'Y'): return 8
        case ('A', 'Z'): return 3
        case ('B', 'X'): return 1
        case ('B', 'Y'): return 5
        case ('B', 'Z'): return 9
        case ('C', 'X'): return 7
        case ('C', 'Y'): return 2
        case ('C', 'Z'): return 6


def main():
    score = 0
    with open('input.txt') as f:
        for line in f.readlines():
            o, _, u = line.strip()
            score += get_points(o, u)
    print(score)


if __name__ == '__main__':
    main()
