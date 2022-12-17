def main():
    part1()
    # part2()


class ValveManager:
    def __init__(self, released_pressure = 0, open_flow = 0, path = ['AA'], time = 1, on_valves = set([]), bad_visit=set([])):
        self.released_pressure = released_pressure
        self.open_flow = open_flow
        self.path = path
        self.time = time
        self.on_valves = on_valves
        self.bad_visit = bad_visit

    def tick(self):
        if self.time < 31:
            self.released_pressure += self.open_flow
            self.time += 1

    def turnValveOn(self, valve, flow):
        self.on_valves.add(valve)
        self.open_flow += flow

    def isValveOn(self, valve):
        return valve in self.on_valves

    def allValvesOn(self):
        return len(self.on_valves) == 6
    
def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        prio = 0
        adjMatrix = {}
        flowDict = {}
        emptyValves = 0
        goodValves = 0
        for line in lines:
            seg1, seg2 = line.split(';')
            seg1 = seg1.split()
            adjMatrix[seg1[1]] = [(valve.strip().replace(',',''), 1) for valve in seg2.split()[4:]]
            flowDict[seg1[1]] = int(seg1[4].split('=')[1])
            if int(seg1[4].split('=')[1]) == 0:
                emptyValves += 1
            else:
                goodValves += 1
        print(emptyValves, goodValves)
        
        
        #reduce graph
        badKeys = []
        for key in adjMatrix:
            if key != 'AA' and flowDict[key] == 0:
                for i in range(len(adjMatrix[key])-1):
                    for j in range(i + 1, len(adjMatrix[key])):
                        leftValve = adjMatrix[key][i]
                        rightValve = adjMatrix[key][j]
                        newDistance = leftValve[1] + rightValve[1]
                        found = False
                        for z, valve in enumerate(adjMatrix[leftValve[0]]):
                            if valve[0] == rightValve[0] and valve[1] > newDistance:
                                found = True
                                adjMatrix[leftValve[0]][z] = (rightValve[0], newDistance)
                                adjMatrix[leftValve[0]] = [x for x in adjMatrix[leftValve[0]] if x[0] != key]
                                for x, valve in enumerate(adjMatrix[rightValve[0]]):
                                    if valve[0] == leftValve[0]:
                                        adjMatrix[rightValve[0]][x] = (leftValve[0], newDistance)
                                        adjMatrix[rightValve[0]] = [x for x in adjMatrix[rightValve[0]] if x[0] != key]
                        if not found:
                            adjMatrix[leftValve[0]].append((rightValve[0], newDistance))
                            adjMatrix[rightValve[0]].append((leftValve[0], newDistance))
                            adjMatrix[leftValve[0]] = [x for x in adjMatrix[leftValve[0]] if x[0] != key]
                            adjMatrix[rightValve[0]] = [x for x in adjMatrix[rightValve[0]] if x[0] != key]
                badKeys.append(key)
        for key in badKeys:
            del adjMatrix[key]

        degreeDict = {}
        for key in adjMatrix:
            degreeDict[key] = len(adjMatrix[key])
        print(degreeDict)
        print(adjMatrix)
        flows = []
        visited = {}
        findPaths(ValveManager(), adjMatrix, flows, visited, flowDict, degreeDict, {})
        # iterativePathFind(ValveManager(), adjMatrix, flows, flowDict)
        print(len(flows))
        maxIndex = 0
        flower = 0
        for i, flow in enumerate(flows):
            if flow[0] > flower:
                flower = flow[0]
                maxIndex = i
        print(flower, flows[maxIndex][1])
        
    print("Solution to Part 1: {}".format(prio))

def findPaths(currentValveManager, adjMatrix, flows, visited, flowDict,degreeDict,badVisit):
    huntSet = set([currentValveManager.path[0]])
    for i in range(1, len(currentValveManager.path)):
        if len(currentValveManager.path) > 1 and currentValveManager.path[i] == currentValveManager.path[i-1]:
            huntSet = set([currentValveManager.path[i]])
            continue
        elif currentValveManager.path[i] in huntSet:
            return
        huntSet.add(currentValveManager.path[i])
     
    if len(currentValveManager.path) > 2:
        if currentValveManager.path[-1] == currentValveManager.path[-3]:
            return
    

    if currentValveManager.allValvesOn() or currentValveManager.time > 30:
        for _ in range(10):
            currentValveManager.tick()
        flows.append((currentValveManager.released_pressure, currentValveManager.path))
        return

    newVisit = dict(visited)
    badVisit = dict(badVisit)  
    if not currentValveManager.isValveOn(currentValveManager.path[-1]) and flowDict[currentValveManager.path[-1]] != 0:
        
        newValveManager = ValveManager(currentValveManager.released_pressure, currentValveManager.open_flow,
        list(currentValveManager.path), currentValveManager.time, set(currentValveManager.on_valves))
        newValveManager.tick()
        currentValve = newValveManager.path[-1]
        newValveManager.turnValveOn(currentValve, flowDict[currentValve])
        newValveManager.path += [currentValve]
        findPaths(newValveManager, adjMatrix, flows, dict(visited), flowDict,degreeDict, badVisit)

    for valve, distance in adjMatrix[currentValveManager.path[-1]]:
        badVisit = dict(badVisit)
        if valve in badVisit and badVisit[valve] == degreeDict[valve]:
            continue
        newValveManager = ValveManager(currentValveManager.released_pressure, currentValveManager.open_flow,
        list(currentValveManager.path), currentValveManager.time, set(currentValveManager.on_valves))
        for _ in range(distance):
            newValveManager.tick()
        if len(currentValveManager.path) == 1:
            print('AA')
        # if len(adjMatrix[currentValveManager.path[-1]]) == 1:
        if currentValveManager.path[-1] in badVisit:
            badVisit[currentValveManager.path[-1]] += 1
        else:
            badVisit[currentValveManager.path[-1]] = 1
        if valve not in newVisit:
            newVisit[valve] = 1
            newValveManager.path += [valve]
            findPaths(newValveManager, adjMatrix, flows, newVisit, flowDict,degreeDict, badVisit)
        else:
            # if newVisit[valve] < 10:
            #     newVisit[valve] += 1
            newValveManager.path += [valve]
            findPaths(newValveManager, adjMatrix, flows, newVisit, flowDict,degreeDict, badVisit)
            # else:
            #     newValveManager.path += ["STOPPED"]
            #     for _ in range(30):
            #         newValveManager.tick()
            #     flows.append((newValveManager.released_pressure, newValveManager.path))
            #     return

def iterativePathFind(currentValveManager, adjMatrix, flows, flowDict):

    queue = [currentValveManager]

    while queue:
        current = queue.pop()
        badFlag = False
        huntSet = set([current.path[0]])
        for i in range(1, len(current.path)):
            if len(current.path) > 1 and current.path[i] == current.path[i-1]:
                huntSet = set([current.path[i]])
                continue
            elif current.path[i] in huntSet:
                badFlag = True
                break
            huntSet.add(current.path[i])
        if badFlag:
            continue
        if len(current.path) > 2:
            if current.path[-1] == current.path[-3]:
                continue
        
        if current.allValvesOn() or current.time > 30:
            for _ in range(10):
                current.tick()
            flows.append((current.released_pressure, current.path))
            continue
 
        if not current.isValveOn(current.path[-1]) and flowDict[current.path[-1]] != 0:
            
            newValveManager = ValveManager(current.released_pressure, current.open_flow,
            list(current.path), current.time, set(current.on_valves), set(current.bad_visit))
            newValveManager.tick()
            currentValve = newValveManager.path[-1]
            newValveManager.turnValveOn(currentValve, flowDict[currentValve])
            newValveManager.path += [currentValve]
            queue.insert(0,newValveManager)

        for valve, distance in adjMatrix[current.path[-1]]:
            
            if valve in current.bad_visit:
                continue
            newValveManager = ValveManager(current.released_pressure, current.open_flow,
            list(current.path), current.time, set(current.on_valves), set(current.bad_visit))

            for _ in range(distance):
                newValveManager.tick()
            if len(current.path) == 1:
                print('AA')
            newValveManager.path += [valve]
            if len(adjMatrix[current.path[-1]]) == 1:
                newValveManager.bad_visit.add(valve)
                
            queue.insert(0,newValveManager)

            
        


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