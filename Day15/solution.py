import multiprocessing as mp

def main():
    part1()
    part2()


def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        targetRowDict = {}
        targetRow = 2000000
        for line in lines:
            sensor, beacon = line.split(':')
            sensor = sensor.split()
            beacon = beacon.split()
            s1, s2, b1, b2 = sensor[2], sensor[3], beacon[4], beacon[5]
            s1 = int(s1.replace(',', '').split('=')[1])
            s2 = int(s2.split('=')[1])
            b1 = int(b1.replace(',', '').split('=')[1])
            b2 = int(b2.split('=')[1])

            manhat = abs(s1 - b1) + abs(s2 - b2)
            if b2 == targetRow:
                targetRowDict[b1] = False

            for i in range(s1-manhat, s1 + manhat + 1):
                currentManhat = abs(s1 - i) + abs(s2 - targetRow)
                if currentManhat <= manhat:
                    if i not in targetRowDict or targetRowDict[i] != False:
                        targetRowDict[i] = True

            cantBlocks = 0
            for key in targetRowDict:
                if targetRowDict[key] == True:
                    cantBlocks += 1
    print("Solution to Part 1: {}".format(cantBlocks))


def part2():

    with open('input.txt') as f:
        lines = f.readlines()
        targetCoords = []
        manhats = []
        for line in lines:
            sensor, beacon = line.split(':')
            sensor = sensor.split()
            beacon = beacon.split()
            s1, s2, b1, b2 = sensor[2], sensor[3], beacon[4], beacon[5]
            s1 = int(s1.replace(',', '').split('=')[1])
            s2 = int(s2.split('=')[1])
            b1 = int(b1.replace(',', '').split('=')[1])
            b2 = int(b2.split('=')[1])

            manhat = abs(s1 - b1) + abs(s2 - b2)
            manhats.append((manhat, s1, s2))
            offset = 0
            for i in range(s2 - manhat - 1, s2):
                if offset == 0:
                    if s1 <= 4000000 and s1 >= 0 and i <= 4000000 and i >= 0:
                        targetCoords.append((s1, i))
                else:
                    if s1 - offset <= 4000000 and s1 - offset >= 0 and i <= 4000000 and i >= 0:
                        targetCoords.append((s1 - offset, i))
                    if s1 + offset <= 4000000 and s1 + offset >= 0 and i <= 4000000 and i >= 0:
                        targetCoords.append((s1 + offset, i))

                offset += 1

            for i in range(s2, s2 + manhat + 2):
                if offset == 0:
                    if s1 <= 4000000 and s1 >= 0 and i <= 4000000 and i >= 0:
                        targetCoords.append((s1, i))
                else:
                    if s1 - offset <= 4000000 and s1 - offset >= 0 and i <= 4000000 and i >= 0:
                        targetCoords.append((s1 - offset, i))
                    if s1 + offset <= 4000000 and s1 + offset >= 0 and i <= 4000000 and i >= 0:
                        targetCoords.append((s1 + offset, i))

                offset -= 1

            print("Adding Potential Coordinates")
        print("Preparing to search", len(targetCoords), "coordinates ;(")

        num_cpus = mp.cpu_count()
        pool = mp.Pool(num_cpus)
        manager = mp.Manager()
        answer = manager.dict()
        partitions = list(split(targetCoords, num_cpus))
      
        for partition in partitions:
            pool.apply_async(searchCoordinates, args=(partition, manhats, answer))
    
        pool.close()
        while len(answer) == 0:
            pass
        pool.terminate()  

    


def potentialCoord(coord, manhats):
    for manhat, s1, s2 in manhats:
        currentManhat = abs(s1 - coord[0]) + abs(s2 - coord[1])
        if currentManhat <= manhat:
            return False
    return True

def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

def searchCoordinates(targetCoords, manhats, answer):
    for coord in targetCoords:
        if potentialCoord(coord, manhats):
            finalAnswer = coord[0]*4000000+coord[1]
            print("Solution to Part 2: {}".format(finalAnswer))
            answer["answer"] = finalAnswer
            break

if __name__ == '__main__':
    main()
