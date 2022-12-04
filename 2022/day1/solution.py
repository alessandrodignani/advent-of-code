def main():
    best = 0
    current = 0
    with open('input.txt') as f:
        for num in f.readlines():
            if num == '\n':
                if current > best:
                    best = current
                current = 0
            else:
                current += int(num)
    print(best)


if __name__ == '__main__':
    main()
