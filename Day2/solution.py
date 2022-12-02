def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()

        score = 0

        scoreDict = {'X': 1, 'Y': 2, 'Z': 3}
        winDict = {'A': 'Z', 'B': 'X', 'C': 'Y'}
        tieDict = {'A': 'X', 'B': 'Y', 'C': 'Z'}

        for line in lines:
            
            opp, me = line.split()
            
            score += scoreDict[me]
            if tieDict[opp] == me:
                score += 3
                continue
            if winDict[opp] != me:
                score += 6
            

    print("Solution to Part 1: {}".format(score))

def part2():

    with open('input.txt') as f:
        lines = f.readlines()

        score = 0

        scoreDict = {'X': 1, 'Y': 2, 'Z': 3}
        winDict = {'A': 'Z', 'B': 'X', 'C': 'Y'}
        tieDict = {'A': 'X', 'B': 'Y', 'C': 'Z'}
        loseDict = {'A': 'Y', 'B': 'Z', 'C': 'X'}

        for line in lines:
            
            opp, me = line.split()
            
            if me == 'X':
                score += scoreDict[winDict[opp]]
            elif me == 'Y':
                score += scoreDict[tieDict[opp]]
                score += 3
            else:
                score += scoreDict[loseDict[opp]]
                score += 6
            

    print("Solution to Part 2: {}".format(score))

if __name__ == '__main__':
    main()