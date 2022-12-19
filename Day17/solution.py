def main():
    part1()
    part2()

class TetrisBoard:

    def __init__(self):
        self.height = 0
        self.allCoords = set([])
        self.pieces = []

        rockCoords = [(2, 0),(3,0),(4,0),(5,0)]
        self.pieces.append(rockCoords)
        rockCoords = [(3,0),(2,1),(3,1),(4,1),(3,2)]
        self.pieces.append(rockCoords)
        rockCoords = [(2,0),(3,0),(4,0),(4,1),(4,2)]
        self.pieces.append(rockCoords)
        rockCoords = [(2,0),(2,1),(2,2),(2,3)]
        self.pieces.append(rockCoords)
        rockCoords = [(2,0),(3,0),(2,1),(3,1)]
        self.pieces.append(rockCoords)

    def playGame(self, directions, num_rocks):

        directionPointer = 0
        rockPointer = 0

        firstIndex = None
        indexDifference = None
        firstHeight = None
        heightDifference = None
        foundStats = False
        for i in range(num_rocks):
            atRest = False
            rockcoords = self.pieces[rockPointer % 5]
        
            spawnRockCoords = [(x[0], x[1] + self.height + 3) for x in rockcoords]
           
            newRock = Rock(spawnRockCoords)

            while not atRest:
               
                adjustedPointer = directionPointer % len(directions)
                if not foundStats and adjustedPointer == 0 and i != 0:
                    if firstHeight == None:
                        firstHeight = self.height
                        firstIndex = i
                    elif heightDifference == None:
                        heightDifference = self.height - firstHeight
                        indexDifference = i - firstIndex
                        foundStats = True

                if directions[adjustedPointer] == '<':
                    if newRock.getLeft() != 0:
                        newCoords = [(x[0] - 1, x[1]) for x in newRock.coords]
                        goodMove = True
                        for coord in newCoords:
                            if coord in self.allCoords:
                                goodMove = False
                                break    
                        if goodMove:
                            newRock.coords = newCoords

                elif directions[adjustedPointer] == '>':
                    if newRock.getRight() != 6:
                        newCoords = [(x[0] + 1, x[1]) for x in newRock.coords]
                        goodMove = True
                        for coord in newCoords:
                            if coord in self.allCoords:
                                goodMove = False
                                break    
                        if goodMove:
                            newRock.coords = newCoords
                directionPointer += 1
               
                if newRock.getBottom() != 0:
                    newCoords = [(x[0], x[1] - 1) for x in newRock.coords]
                    goodMove = True
                    for coord in newCoords:
                        if coord in self.allCoords:
                            goodMove = False
                            break
                    if goodMove:
                        newRock.coords = newCoords
                        continue
                # print("Adding", newRock.coords)
                atRest = True
                self.height = max(self.height, newRock.getTop() + 1)
                for coord in newRock.coords:
                    self.allCoords.add(coord)
                # print(self.allCoords)
                # print(self.height)
            rockPointer += 1
        
        return {"first_index": firstIndex, "index_difference": indexDifference, "first_height": firstHeight, "height_difference": heightDifference}

class Rock:
    def __init__(self, coords):
        self.coords = coords
       

    def getLeft(self):
        return min([x[0] for x in self.coords])
    
    def getRight(self):
        return max([x[0] for x in self.coords])
    
    def getBottom(self):
        return min([x[1] for x in self.coords])
    
    def getTop(self):
        return max([x[1] for x in self.coords])



def part1():

    with open('input.txt') as f:
        line = f.read()
        
        newGame = TetrisBoard()
        newGame.playGame(line, 2022)

    print("Solution to Part 1: {}".format(newGame.height))

def part2():

    with open('input.txt') as f:
        line = f.read()
        newGame = TetrisBoard()
        stats = newGame.playGame(line, 10000)
        multiplyCount = (1000000000000 - stats["first_index"]) // stats["index_difference"]
        remainder = (1000000000000 - stats["first_index"]) % stats["index_difference"]
        answer = multiplyCount * stats["height_difference"]

        newGame = TetrisBoard()
        newGame.playGame(line, stats["first_index"] + remainder)
        answer += newGame.height


    print("Solution to Part 2: {}".format(answer))

if __name__ == '__main__':
    main()