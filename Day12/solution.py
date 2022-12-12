def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        startCoord = None
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == 'S':
                    startCoord = (i,j,0)

        visited = set([])
        queue = [startCoord]
        visited.add((startCoord[0], startCoord[1]))
        answer = None

        while queue:
            currentNode = queue.pop()
            currentElevation = lines[currentNode[0]][currentNode[1]]
            if currentElevation == 'S':
                currentElevation = 'a'

            if currentElevation == 'E':
                answer = currentNode[2]
                break
        
            # check above
            if currentNode[0] != 0:
                potentialNode = lines[currentNode[0] - 1][currentNode[1]]
                if potentialNode == 'E':
                    potentialNode = 'z'
                
                if ord(currentElevation) + 1 >= ord(potentialNode):
                    if (currentNode[0] - 1, currentNode[1]) not in visited:
                        visited.add((currentNode[0] - 1, currentNode[1]))
                        queue.insert(0, (currentNode[0] - 1, currentNode[1], currentNode[2] + 1))

            # check left
            if currentNode[1] != 0:
                potentialNode = lines[currentNode[0]][currentNode[1] - 1]
                if potentialNode == 'E':
                    potentialNode = 'z'
                if ord(currentElevation) + 1 >= ord(potentialNode):
                    if (currentNode[0], currentNode[1] - 1) not in visited:
                        visited.add((currentNode[0], currentNode[1] - 1))
                        queue.insert(0, (currentNode[0], currentNode[1] - 1, currentNode[2] + 1))

            # check right
            if currentNode[1] < len(lines[0]) - 2:
                potentialNode = lines[currentNode[0]][currentNode[1] + 1]
                if potentialNode == 'E':
                    potentialNode = 'z'
                if ord(currentElevation) + 1 >= ord(potentialNode):
                    if (currentNode[0], currentNode[1] + 1) not in visited:
                        visited.add((currentNode[0], currentNode[1] + 1))
                        queue.insert(0, (currentNode[0], currentNode[1] + 1, currentNode[2] + 1))
            
            # check below
            if currentNode[0] < len(lines) - 1:
                potentialNode = lines[currentNode[0] + 1][currentNode[1]]
                if potentialNode == 'E':
                    potentialNode = 'z'
                if ord(currentElevation) + 1 >= ord(potentialNode):
                    if (currentNode[0] + 1, currentNode[1]) not in visited:
                        visited.add((currentNode[0] + 1, currentNode[1]))
                        queue.insert(0, (currentNode[0] + 1, currentNode[1], currentNode[2] + 1))     

    print("Solution to Part 1: {}".format(answer))



def part2():

    with open('input.txt') as f:
        lines = f.readlines()
        startCoords = []
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == 'S' or lines[i][j] == 'a':
                    startCoords.append((i,j,0))

        answers = []

        for startCoord in startCoords:
            visited = set([])
            queue = [startCoord]
            visited.add((startCoord[0], startCoord[1]))
            while queue:
                currentNode = queue.pop()
                currentElevation = lines[currentNode[0]][currentNode[1]]
                if currentElevation == 'S':
                    currentElevation = 'a'

                if currentElevation == 'E':
                    answers.append(currentNode[2])
                    break
            
                # check above
                if currentNode[0] != 0:
                    potentialNode = lines[currentNode[0] - 1][currentNode[1]]
                    if potentialNode == 'E':
                        potentialNode = 'z'
                    
                    if ord(currentElevation) + 1 >= ord(potentialNode):
                        if (currentNode[0] - 1, currentNode[1]) not in visited:
                            visited.add((currentNode[0] - 1, currentNode[1]))
                            queue.insert(0, (currentNode[0] - 1, currentNode[1], currentNode[2] + 1))

                # check left
                if currentNode[1] != 0:
                    potentialNode = lines[currentNode[0]][currentNode[1] - 1]
                    if potentialNode == 'E':
                        potentialNode = 'z'
                    if ord(currentElevation) + 1 >= ord(potentialNode):
                        if (currentNode[0], currentNode[1] - 1) not in visited:
                            visited.add((currentNode[0], currentNode[1] - 1))
                            queue.insert(0, (currentNode[0], currentNode[1] - 1, currentNode[2] + 1))

                # check right
                if currentNode[1] < len(lines[0]) - 2:
                    potentialNode = lines[currentNode[0]][currentNode[1] + 1]
                    if potentialNode == 'E':
                        potentialNode = 'z'
                    if ord(currentElevation) + 1 >= ord(potentialNode):
                        if (currentNode[0], currentNode[1] + 1) not in visited:
                            visited.add((currentNode[0], currentNode[1] + 1))
                            queue.insert(0, (currentNode[0], currentNode[1] + 1, currentNode[2] + 1))
                
                # check below
                if currentNode[0] < len(lines) - 1:
                    potentialNode = lines[currentNode[0] + 1][currentNode[1]]
                    if potentialNode == 'E':
                        potentialNode = 'z'
                    if ord(currentElevation) + 1 >= ord(potentialNode):
                        if (currentNode[0] + 1, currentNode[1]) not in visited:
                            visited.add((currentNode[0] + 1, currentNode[1]))
                            queue.insert(0, (currentNode[0] + 1, currentNode[1], currentNode[2] + 1))
            

    print("Solution to Part 2: {}".format(min(answers)))

if __name__ == '__main__':
    main()