def main():
    part1()
    part2()


def part1():

    with open('input.txt') as f:
        line = f.readline()

        uniqueSet = set([])
        endChar = None
        for i in range(len(line)):
            uniqueSet.add(line[i])
            for j in range(i, i + 4):
                uniqueSet.add(line[j])

            if len(uniqueSet) == 4:
                endChar = i + 4
                break
            else:
                uniqueSet.clear()

    print("Solution to Part 1: {}".format(endChar))


def part2():
    with open('input.txt') as f:
        line = f.readline()

        uniqueSet = set([])
        endChar = None
        for i in range(len(line)):
            uniqueSet.add(line[i])

            for j in range(i, i + 14):
                uniqueSet.add(line[j])

            if len(uniqueSet) == 14:
                endChar = i + 14
                break
            else:
                uniqueSet.clear()

    print("Solution to Part 2: {}".format(endChar))


if __name__ == '__main__':
    main()
