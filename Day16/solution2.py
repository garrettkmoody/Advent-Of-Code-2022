from helper_functions import *

def main():
    part1()
    # part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        prio = 0
        adjMatrix = {}
        flowDict = {}
        for line in lines:
            seg1, seg2 = line.split(';')
            seg1 = seg1.split()
            adjMatrix[seg1[1]] = [valve.strip().replace(',','') for valve in seg2.split()[4:]]
            flowDict[seg1[1]] = int(seg1[4].split('=')[1])
        
        newGraph = reduceGraph(adjMatrix, flowDict)
        scores = []
        time = 29
        visited = set(['AA'])
        currentValve = 'AA'
        
        while True:
            if time <= 0:
                break
            for key in newGraph[currentValve]:
                if key in visited or key == currentValve:
                    continue
                
                tempTime = time
                tempScore = 0
                expectedValue = (tempTime - newGraph[currentValve][key]) * flowDict[key]
               
                #time elapsed
                tempTime -= newGraph[currentValve][key] + 1

                tempScore += expectedValue
                
                tempScore += max([(tempTime - newGraph[key][x]) * flowDict[x] for x in newGraph[key] if x not in visited and key != x])
                
                scores.append((key, tempScore))
            if currentValve == 'DD':
                print(scores)
            chosenPath = None
            maxScore = 0
            for i in range(len(scores)):
                if scores[i][1] > maxScore:
                    maxScore = scores[i][1]
                    chosenPath = scores[i][0]
            scores.clear()
            time -= newGraph[currentValve][chosenPath] + 1
            print(time)
            currentValve = chosenPath
            visited.add(currentValve)
            print(currentValve)
        

    print("Solution to Part 1: {}".format(prio))

# def part2():

#     with open('input.txt') as f:
#         lines = f.readlines()
#         prio = 0
#         for line in lines:
#             elf1, elf2 = line.split(',')
#             elf1 = elf1.split('-')
#             elf2 = elf2.split('-')
       
#             if int(elf1[0]) <= int(elf2[0]) and int(elf2[0]) <= int(elf1[1]):
#                 prio += 1
#             elif int(elf2[0]) <= int(elf1[0]) and int(elf1[0]) <= int(elf2[1]):
#                 prio += 1
            
   

#     print("Solution to Part 2: {}".format(prio))

if __name__ == '__main__':
    main()