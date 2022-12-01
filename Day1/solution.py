def main():
    part1()
    part2()

def part1():
    maxCalories = float('-inf')

    with open('input.txt') as f:
        lines = f.readlines()

        currentElfCalories = 0

        for line in lines:
            if line != '\n':
                currentElfCalories += int(line)
            else:
                maxCalories = max(currentElfCalories, maxCalories)
                currentElfCalories = 0
    
    print("Solution to Part 1: {}".format(maxCalories))

def part2():

    firstElf = float('-inf')
    secondElf = float('-inf')
    thirdElf = float('-inf')

    with open('input.txt') as f:
        lines = f.readlines()

        currentElfCalories = 0

        for line in lines:
            if line != '\n':
                currentElfCalories += int(line)
            else:
                if currentElfCalories > firstElf:
                    thirdElf = secondElf
                    secondElf = firstElf
                    firstElf = currentElfCalories
                elif currentElfCalories > secondElf:
                    thirdElf = secondElf
                    secondElf = currentElfCalories
                elif currentElfCalories > thirdElf:
                    thirdElf = currentElfCalories

                currentElfCalories = 0
    
    print("Solution to Part 2: {}".format(firstElf + secondElf + thirdElf))

if __name__ == '__main__':
    main()