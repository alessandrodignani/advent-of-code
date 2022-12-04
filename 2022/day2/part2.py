# A for Rock, B for Paper, and C for Scissors
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
# 1 point for Rock, 2 for Paper, and 3 for Scissors
# 0 points if you lost, 3 if the round was a draw, and 6 if you won

def get_points(opponent, result):
    match (opponent, result):
        case ('A', 'X'): return 3
        case ('A', 'Y'): return 4
        case ('A', 'Z'): return 8
        case ('B', 'X'): return 1
        case ('B', 'Y'): return 5
        case ('B', 'Z'): return 9
        case ('C', 'X'): return 2
        case ('C', 'Y'): return 6
        case ('C', 'Z'): return 7


def main():
    score = 0
    with open('input.txt') as f:
        for line in f.readlines():
            opponent, _, result = line.strip()
            score += get_points(opponent, result)
    print(score)


if __name__ == '__main__':
    main()
