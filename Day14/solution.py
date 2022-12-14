def main():
    part1()
    part2()


class SandCoord:
    def __init__(self, col, depth):
        self.col = col
        self.depth = depth

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        sandBlocks = 0
        caveGrid = []
        for _ in range(200):
            row = []
            for _ in range(550):
                row.append('.')
            caveGrid.append(list(row))
        
        for line in lines:
            coords = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in line.split(' -> ')]
            coords = [SandCoord(x[0], x[1]) for x in coords]
            for i in range(len(coords) - 1):
                if coords[i].col == coords[i+1].col:
                    
                    depth = min(coords[i].depth, coords[i+1].depth)
                    depth2 = max(coords[i].depth, coords[i+1].depth)
                    for j in range(depth, depth2 + 1):
                        caveGrid[j][coords[i].col] = '#'
                else:
                    col = min(coords[i].col, coords[i+1].col)
                    col2 = max(coords[i].col, coords[i+1].col)
                    for j in range(col, col2 + 1):
                        caveGrid[coords[i].depth][j] = '#'

        while dropSand(SandCoord(500, 0), caveGrid):
            sandBlocks += 1
   
    print("Solution to Part 1: {}".format(sandBlocks))


def dropSand(coord, caveGrid):
    
    if coord.depth == 199:
        return False
    # if we are looking at a solid block
    if caveGrid[coord.depth][coord.col] != '.':
        if caveGrid[coord.depth][coord.col - 1] == '.':
            return dropSand(SandCoord(coord.col - 1, coord.depth + 1), caveGrid)
        if caveGrid[coord.depth][coord.col + 1] == '.':
            return dropSand(SandCoord(coord.col + 1, coord.depth + 1), caveGrid)
        
        # sand at rest
        caveGrid[coord.depth - 1][coord.col] = 'o'
        return True
    else:
        return dropSand(SandCoord(coord.col, coord.depth + 1), caveGrid)
    
def dropSand2(coord, caveGrid):
    
    # if we are looking at a solid block
 
    if caveGrid[coord.depth][coord.col] != '.':
        if caveGrid[coord.depth][coord.col - 1] == '.':
            return dropSand2(SandCoord(coord.col - 1, coord.depth + 1), caveGrid)
        if caveGrid[coord.depth][coord.col + 1] == '.':
            return dropSand2(SandCoord(coord.col + 1, coord.depth + 1), caveGrid)
        
        # sand at rest
        if coord.depth - 1 == 0:
            return False
        caveGrid[coord.depth - 1][coord.col] = 'o'
        return True
    else:
        return dropSand2(SandCoord(coord.col, coord.depth + 1), caveGrid)


def part2():
    with open('input.txt') as f:
        lines = f.readlines()
        sandBlocks = 0
        caveGrid = []
        for _ in range(200):
            row = []
            for _ in range(1000):
                row.append('.')
            caveGrid.append(list(row))

        maxDepth = 0
        
        for line in lines:
            coords = [(int(x.split(',')[0]), int(x.split(',')[1])) for x in line.split(' -> ')]
            coords = [SandCoord(x[0], x[1]) for x in coords]
            maxDepth = max(maxDepth, max([x.depth for x in coords]))

            for i in range(len(coords) - 1):
                if coords[i].col == coords[i+1].col:  
                    depth = min(coords[i].depth, coords[i+1].depth)
                    depth2 = max(coords[i].depth, coords[i+1].depth)
                    for j in range(depth, depth2 + 1):
                        caveGrid[j][coords[i].col] = '#'
                else:
                    col = min(coords[i].col, coords[i+1].col)
                    col2 = max(coords[i].col, coords[i+1].col)
                    for j in range(col, col2 + 1):
                        caveGrid[coords[i].depth][j] = '#'

        # build floor
        for j in range(len(caveGrid[0])):
            caveGrid[maxDepth + 2][j] = '#'

        while dropSand2(SandCoord(500, 0), caveGrid):
            sandBlocks += 1

    print("Solution to Part 2: {}".format(sandBlocks + 1))

if __name__ == '__main__':
    main()