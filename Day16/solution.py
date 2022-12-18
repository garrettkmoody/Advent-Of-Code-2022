from helper_functions import *
import multiprocessing as mp

def main():
    part1()
    

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
        
        paths = []
        findPaths(['AA'], newGraph, set(['AA']), flowDict, paths, 29)
        print(len(paths))
        answer = max([simulatePath(path, flowDict, newGraph) for path in paths])

    print("Solution to Part 1: {}".format(answer))

def findPaths(currentPath, newGraph, visited, flowDict, paths, time):

    currentValve = currentPath[-1]
    
    if len(currentPath) == len(newGraph):
        paths.append(currentPath)
        return
   
    biggestScore = max([(time - newGraph[currentValve][x]) * flowDict[x] for x in newGraph[currentValve] if x not in visited])
    if biggestScore < 1:
        paths.append(currentPath)
        return
    for key in newGraph[currentValve]:
        if key not in visited and (time - newGraph[currentValve][key]) * flowDict[key] > biggestScore / 100:
            updatedVisited = set(visited)
            updatedVisited.add(key)
            updatedPath = list(currentPath)
            updatedPath.append(key)  
            tempTime = time - (newGraph[currentValve][key] + 1)
    
            
            findPaths(updatedPath, newGraph, updatedVisited, flowDict, paths, tempTime)


def simulatePath(path, flowDict, newGraph):
    time = 29
    score = 0
    previousValve = 'AA'
    for valve in path:
        if valve == 'AA':
            continue
        flow = flowDict[valve]
        distance = newGraph[previousValve][valve]
        if (time - distance) * flow < 1:
            break
        score += (time - distance) * flow
        time -= distance + 1
        previousValve = valve

    return score




if __name__ == '__main__':
    main()