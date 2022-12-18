from helper_functions import *

def main():
    # part1()
    part2()

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

def simulatePath2(path,path2,flowDict,newGraph):
    time = 25
    score = 0
    previousValve = 'AA'

    visited = set([])
    for valve in path:
        if valve == 'AA':
            continue
        flow = flowDict[valve]
        distance = newGraph[previousValve][valve]
        if (time - distance) * flow < 1:
            break
        if valve not in visited:
            if time < 17:
                break
            score += (time - distance) * flow
            visited.add(valve)
        time -= distance + 1
        previousValve = valve
    
    time = 25
    previousValve = 'AA'
    for valve in path2:
        if valve == 'AA':
            continue
        flow = flowDict[valve]
        distance = newGraph[previousValve][valve]
        if (time - distance) * flow < 1:
            break
        if valve not in visited:
            score += (time - distance) * flow
            visited.add(valve)
        time -= distance + 1
        previousValve = valve

    return score

def findPaths2(currentPath, newGraph, visited, flowDict, paths, time):

    currentValve = currentPath[-1]
    
    if len(currentPath) == len(newGraph):
        paths.append(currentPath)
        return
   
    biggestScore = max([(time - newGraph[currentValve][x]) * flowDict[x] for x in newGraph[currentValve] if x not in visited])
    if biggestScore < 1:
        paths.append(currentPath)
        return
    for key in newGraph[currentValve]:
        if key not in visited:
            updatedVisited = set(visited)
            updatedVisited.add(key)
            updatedPath = list(currentPath)
            updatedPath.append(key)  
            tempTime = time - (newGraph[currentValve][key] + 1)
    
            
            findPaths2(updatedPath, newGraph, updatedVisited, flowDict, paths, tempTime)

def part2():

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

        findPaths2(['AA'], newGraph, set(['AA']), flowDict, paths, 29)
        
        
        print(len(paths))
        
        maxScore = 0
        for i in range(len(paths) - 1):
            for j in range(i + 1, len(paths)):
                maxScore = max(maxScore, simulatePath2(paths[i], paths[j], flowDict, newGraph))
                # maxScore = max(maxScore, simulatePath2(paths[j], paths[i], flowDict, newGraph))  
            if i % 100 == 0:
                print('ran')
        
        print(maxScore)
            
        
        
        answer = max([simulatePath(path, flowDict, newGraph) for path in paths])

    print("Solution to Part 2: {}".format(answer))

if __name__ == '__main__':
    main()