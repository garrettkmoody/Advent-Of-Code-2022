def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        goodPairs = 0
        pairCounter = 1
        pair = []
        for line in lines:
            
            if line == '\n':
                if recursiveCheck(pair[0], pair[1]):
                    goodPairs += pairCounter
                pair.clear()
                pairCounter += 1
                
            else:
                currentList = []
              
                depthList = [currentList]
                
                newLine = line.strip()
                for i in range(len(newLine)):
                    if newLine[i]== '[':
                        depthList.append([])
                    elif newLine[i] == ']':
                        depthList[-2].append(depthList[-1])
                        depthList.pop()
                    elif newLine[i].isdigit():
                        currentDigit = newLine[i]
                        if newLine[i + 1].isdigit():
                            currentDigit += newLine[i + 1]
                        currentDigit = int(currentDigit)
                        depthList[-1].append(currentDigit)
                      
                pair.append(currentList[0])

    print("Solution to Part 1: {}".format(goodPairs))

def recursiveCheck(value1, value2):

    #Base case 1, both are integers
    if isinstance(value1, int) and isinstance(value2, int):
        if value1 < value2:
            return 1
        elif value1 > value2:
            return 0
        else:
            return -1
    
    if isinstance(value1, int):
        value1 = [value1]
    if isinstance(value2, int):
        value2 = [value2]
    
    if len(value1) == 0 and len(value2) > 0:
        return 1
    elif len(value2) == 0 and len(value1) > 0:
        return 0

    for i in range(len(value1)):
        if i == len(value2):
            return 0
        checkNum = recursiveCheck(value1[i], value2[i])
      
        if checkNum != -1:
            return checkNum
        
        if i == len(value1) - 1 and len(value1) < len(value2):
            return 1
    
    return -1
        
def part2():

    with open('input.txt') as f:
        lines = f.readlines()
        packets = []
        packets.append([[2]])
        packets.append([[6]])
        for line in lines:
            if line == '\n':
                continue   
            else:
                currentList = []
              
                depthList = [currentList]
                
                newLine = line.strip()
                for i in range(len(newLine)):
                    if newLine[i]== '[':
                        depthList.append([])
                    elif newLine[i] == ']':
                        depthList[-2].append(depthList[-1])
                        depthList.pop()
                    elif newLine[i].isdigit():
                        currentDigit = newLine[i]
                        if newLine[i + 1].isdigit():
                            currentDigit += newLine[i + 1]
                        currentDigit = int(currentDigit)
                        depthList[-1].append(currentDigit)
                      
                packets.append(currentList[0])

        sorted = False
        while not sorted:
            sorted = True
            for i in range(len(packets) - 1):
                if not recursiveCheck(packets[i], packets[i + 1]):
                    packets[i], packets[i + 1] = packets[i + 1], packets[i]
                    sorted = False
        
        index1 = 0
        index2 = 0

        for i in range(len(packets)):
            if packets[i] == [[6]]:
                index1 = i + 1
            if packets[i] == [[2]]:
                index2 = i + 1
    print("Solution to Part 2: {}".format(index1 * index2))

if __name__ == '__main__':
    main()