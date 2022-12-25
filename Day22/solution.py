from enum import Enum
import re


def main():
    part1()
    # part2()

class Direction:
    RIGHT = 0
    DOWN = 1
    LEFT = 2
    UP = 3
    
class GameManager:

    def __init__(self, startPos : tuple, board : dict) -> None:
        self.currentPos = startPos
        self.board = board
        self.direction = Direction.RIGHT

    def rotatePlayer(self, turn : str):
        
        if turn == 'R':
            self.direction = (self.direction + 1) % 4
        elif turn == 'L':
            self.direction = (self.direction + 3) % 4
        else:
            print("Invalid turn direction!")

    def movePlayer(self, steps : int):

        dirOffsetMap = {
            Direction.RIGHT : (0, 1),
            Direction.DOWN : (1, 0),
            Direction.LEFT : (0, -1),
            Direction.UP : (-1, 0)
        }

        for _ in range(steps):

            newLocation = self.getValidLocation((self.currentPos[0] + dirOffsetMap[self.direction][0],
            self.currentPos[1] + dirOffsetMap[self.direction][1]))

            if newLocation:
                self.currentPos = newLocation
            else:
                break
            
    
    def getValidLocation(self, coordinate : tuple):
        
        reverseOffsetMap = {
            Direction.RIGHT : (0, -1),
            Direction.DOWN : (-1, 0),
            Direction.LEFT : (0, 1),
            Direction.UP : (1, 0)
        }

        if coordinate not in self.board:
            newCoord = coordinate
            while True:
                potCoord = (newCoord[0] + reverseOffsetMap[self.direction][0], newCoord[1] + reverseOffsetMap[self.direction][1])
                if potCoord in self.board:
                    newCoord = potCoord
                else:
                    break
            if self.board[newCoord] == '.':
                return newCoord
            elif self.board[newCoord] == '#':
                return None
        elif self.board[coordinate] == '.':
            return coordinate
        elif self.board[coordinate] == '#':
            return None


def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        
        boardMap = {}
        movement = lines[-1]
        startPosition = None

        for i in range(len(lines) - 2):
            for j in range(len(lines[i])):
                if lines[i][j] == '#':
                    boardMap[(i,j)] = '#'
                elif lines[i][j] == '.':
                    if not startPosition:
                        startPosition = (i,j)
                    boardMap[(i,j)] = '.'
        
        newGame = GameManager(startPosition, boardMap)

        result = [x for x in re.split('(\d+)', movement) if x != '']
        
        for command in result:
            if command in ['L','R']:
                newGame.rotatePlayer(command)
            else:
                newGame.movePlayer(int(command))

        answer = 1000 * (newGame.currentPos[0] + 1) + 4 * (newGame.currentPos[1] + 1) + newGame.direction

    print("Solution to Part 1: {}".format(answer))

def part2():

    with open('input.txt') as f:
        lines = f.readlines()
        prio = 0
        for line in lines:
            elf1, elf2 = line.split(',')
            elf1 = elf1.split('-')
            elf2 = elf2.split('-')
       
            if int(elf1[0]) <= int(elf2[0]) and int(elf2[0]) <= int(elf1[1]):
                prio += 1
            elif int(elf2[0]) <= int(elf1[0]) and int(elf1[0]) <= int(elf2[1]):
                prio += 1
            
   

    print("Solution to Part 2: {}".format(prio))

if __name__ == '__main__':
    main()