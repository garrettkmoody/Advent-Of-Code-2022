def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        grid = []
        for line in lines:
            tempRow = []
            for char in line:
                if char != '\n':
                    tempRow.append(char)
            grid.append(list(tempRow))
        visibleTrees = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                  
                visibleTrees += checkVisible(i,j,grid)
                
    print("Solution to Part 1: {}".format(visibleTrees))

def checkVisible(i, j, grid):
    visible = True
    for tempj in range(j - 1, -1, -1):
        if grid[i][tempj] >= grid[i][j]:
            visible = False
            break
    if visible:
        return 1

    visible = True
    for tempj in range(j + 1, len(grid[i])):
        if grid[i][tempj] >= grid[i][j]:
            visible = False
            break
    if visible:
        return 1

    visible = True
    for tempi in range(i - 1, -1, -1):
        if grid[tempi][j] >= grid[i][j]:
            visible = False
            break
    if visible:
        return 1

    visible = True
    for tempi in range(i + 1, len(grid)):
        if grid[tempi][j] >= grid[i][j]:
            visible = False
            break
    if visible:
        return 1
    return 0

def part2():
    with open('input.txt') as f:
        lines = f.readlines()
        
        grid = []
        for line in lines:
            tempRow = []
            for char in line:
                if char != '\n':
                    tempRow.append(char)
    
            grid.append(list(tempRow))

        maxScore = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                
                maxScore = max(checkMax(i,j,grid), maxScore)
                
    print("Solution to Part 2: {}".format(maxScore))

def checkMax(i, j, grid):
    max = []
    tempMax = 0
    for tempj in range(j - 1, -1, -1):
        tempMax += 1
        if grid[i][tempj] >= grid[i][j]:
            break
    max.append(tempMax)
    tempMax = 0
 
    for tempj in range(j + 1, len(grid[i])):
        tempMax += 1
        if grid[i][tempj] >= grid[i][j]:
            break
    max.append(tempMax)
    tempMax = 0
   
    for tempi in range(i - 1, -1, -1):
        tempMax += 1
        if grid[tempi][j] >= grid[i][j]:
            break
    max.append(tempMax)
    tempMax = 0
    
    for tempi in range(i + 1, len(grid)):
        tempMax += 1
        if grid[tempi][j] >= grid[i][j]:
            break
    max.append(tempMax)

    tempMax = 1
    for num in max:
        tempMax *= num
    return tempMax

if __name__ == '__main__':
    main()