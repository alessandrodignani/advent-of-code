def main():
    third = 0
    second = 0
    first = 0
    current = 0
    with open('input.txt') as f:
        for num in f.readlines():
            if num == '\n':
                if current > third:
                    third = current
                    first, second, third = sorted((first, second, third), reverse=True)
                current = 0
            else:
                current += int(num)
    print(first + second + third)


if __name__ == '__main__':
    main()
