def main():
    part1()
    part2()

def part1():
    
    with open('input.txt') as f:

        stacks = []
        stacks.append(['T', 'D', 'W', 'Z', 'V', 'P'])
        stacks.append(['L', 'S', 'W', 'V', 'F', 'J', 'D'])
        stacks.append(['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'])
        stacks.append(['R', 'S', 'J'])
        stacks.append(['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'])
        stacks.append(['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'])
        stacks.append(['V', 'J', 'P', 'C', 'B', 'D', 'N'])
        stacks.append(['P', 'T', 'B', 'Q'])
        stacks.append(['H', 'G', 'Z', 'R', 'C'])

        lines = f.readlines()
       
        for line in lines:
            lineInput = line.split(' ')
            loopNum = int(lineInput[1])
            start = int(lineInput[3])
            end = int(lineInput[5])

           
            for _ in range(loopNum):
                stacks[end - 1].append(stacks[start - 1][-1])
                stacks[start - 1].pop()

            newStr = ""

            for list in stacks:
                if list:
                    newStr += list[-1]
            
    

    print("Solution to Part 1: {}".format(newStr))

def part2():

    with open('input.txt') as f:

        stacks = []
        stacks.append(['T', 'D', 'W', 'Z', 'V', 'P'])
        stacks.append(['L', 'S', 'W', 'V', 'F', 'J', 'D'])
        stacks.append(['Z', 'M', 'L', 'S', 'V', 'T', 'B', 'H'])
        stacks.append(['R', 'S', 'J'])
        stacks.append(['C', 'Z', 'B', 'G', 'F', 'M', 'L', 'W'])
        stacks.append(['Q', 'W', 'V', 'H', 'Z', 'R', 'G', 'B'])
        stacks.append(['V', 'J', 'P', 'C', 'B', 'D', 'N'])
        stacks.append(['P', 'T', 'B', 'Q'])
        stacks.append(['H', 'G', 'Z', 'R', 'C'])

        lines = f.readlines()
       
        for line in lines:
            lineInput = line.split(' ')
            loopNum = int(lineInput[1])
            start = int(lineInput[3])
            end = int(lineInput[5])

            newList = []
            for _ in range(loopNum):
                newList.append(stacks[start - 1][-1])
                
                stacks[start - 1].pop()

            newList.reverse()
            stacks[end - 1].extend(newList)
            newStr = ""

            for list in stacks:
                if list:

                    newStr += list[-1]
    

    print("Solution to Part 2: {}".format(newStr))


if __name__ == '__main__':
    main()