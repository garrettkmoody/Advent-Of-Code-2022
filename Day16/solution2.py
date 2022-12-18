from helper_functions import *
import multiprocessing as mp

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
    time2 = 25
    p1 = 1
    p2 = 1
    score = 0
    previousValve1 = 'AA'
    previousValve2 = 'AA'
    visited = set([])
    while True:
        if p1 >= len(path) and p2 >= len(path2):
            break
        if time >= time2 and p1 < len(path):
            valve = path[p1]
            p1 += 1
            if valve in visited:
                break
            flow = flowDict[valve]
            distance = newGraph[previousValve1][valve]
            score += (time - distance) * flow
            time -= distance + 1
            visited.add(valve)
            previousValve1 = valve
           
        elif p2 < len(path2):
            valve = path2[p2]
            p2 += 1
            if valve in visited:
                break
            flow = flowDict[valve]
            distance = newGraph[previousValve2][valve]
            score += (time2 - distance) * flow
            time2 -= distance + 1
            visited.add(valve)
            previousValve2 = valve
        else:
            break
            

    return score

def findPaths2(currentPath, newGraph, visited, flowDict, paths, time):

    currentValve = currentPath[-1]
    
    if len(currentPath) == len(newGraph) // 2 + 1:
        paths.append(currentPath)
        return
   
    biggestScore = max([(time - newGraph[currentValve][x]) * flowDict[x] for x in newGraph[currentValve] if x not in visited])
    if biggestScore < 1:
        paths.append(currentPath)
        return
    for key in newGraph[currentValve]:
        if key not in visited and (time - newGraph[currentValve][key]) * flowDict[key] > biggestScore / 10:
            updatedVisited = set(visited)
            updatedVisited.add(key)
            updatedPath = list(currentPath)
            updatedPath.append(key)  
            tempTime = time - (newGraph[currentValve][key] + 1)
    
            
            findPaths2(updatedPath, newGraph, updatedVisited, flowDict, paths, tempTime)

def comparePaths(paths, i, flowDict, newGraph, maxScores):
    tempScore = 0
    for j in range(i + 1, len(paths)):
        # if 'AADDHHEE' in "".join(paths[i]) and 'AAJJBBCC' in "".join(paths[j]):
        #     print(simulatePath2(paths[i], paths[j], flowDict, newGraph))
        tempScore = max(tempScore, simulatePath2(paths[i], paths[j], flowDict, newGraph))
        # maxScore = max(maxScore, simulatePath2(paths[j], paths[i], flowDict, newGraph))  
    maxScores.append(tempScore)
    if i % 50 == 0:
        print(i)

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

        findPaths2(['AA'], newGraph, set(['AA']), flowDict, paths, 25)
        
        
        print(len(paths))
        
        print("cpus", mp.cpu_count())

        num_cores = mp.cpu_count()
        pool = mp.Pool(num_cores)
        maxScores = mp.Manager().list()

        for i in range(len(paths) - 1):
            pool.apply_async(comparePaths(paths, i, flowDict, newGraph, maxScores))

        pool.close()
        pool.join()
            

    print("Solution to Part 2: {}".format(max(maxScores)))

if __name__ == '__main__':
    main()