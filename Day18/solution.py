import queue
import multiprocessing as mp
import itertools

def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        prio = 0
        coordinates = set([])
        checkedCoords = set([])
        surfaceArea = len(lines) * 6
        for line in lines:
            x = line.split(',')
            coordinates.add((int(x[0]),int(x[1]),int(x[2])))
            
        
        for coord in coordinates:
            potentialCoord = (coord[0] + 1, coord[1], coord[2])
            if potentialCoord in coordinates and potentialCoord not in checkedCoords:
                checkedCoords.add(coord)
                surfaceArea -= 2
               
               

            potentialCoord = (coord[0] - 1, coord[1], coord[2])
            if potentialCoord in coordinates and potentialCoord not in checkedCoords:
                checkedCoords.add(coord)
                surfaceArea -= 2
               

            potentialCoord = (coord[0], coord[1] + 1, coord[2])
            if potentialCoord in coordinates and potentialCoord not in checkedCoords:
                checkedCoords.add(coord)
                surfaceArea -= 2
              
                

            potentialCoord = (coord[0], coord[1] - 1, coord[2])
            if potentialCoord in coordinates and potentialCoord not in checkedCoords:
                checkedCoords.add(coord)
                surfaceArea -= 2
              
                

            potentialCoord = (coord[0], coord[1], coord[2] + 1)
            if potentialCoord in coordinates and potentialCoord not in checkedCoords:
                checkedCoords.add(coord)
                surfaceArea -= 2
               
                

            potentialCoord = (coord[0], coord[1], coord[2] - 1)
            if potentialCoord in coordinates and potentialCoord not in checkedCoords:
                checkedCoords.add(coord)
                surfaceArea -= 2
                

    print("Solution to Part 1: {}".format(surfaceArea))

def part2():
    with open('input.txt') as f:
        space = []
        # checker = [] # find maximum coordinate in x, y, or z
        lines = f.readlines()
        for line in lines:
            block = line.strip()
            block = [int(x) for x in block.split(',')]
            space.append(tuple(block))
            # checker.extend(block)
    # print(max(checker))

    enclosed_airblocks = find_enclosed(space)
    print("num enclosed airblocks", len(enclosed_airblocks))
    sa_airblocks = 0
    sa_total = 0
    for block in enclosed_airblocks:
        sa_airblocks += 6 - find_adjacent(block, enclosed_airblocks)
    for block in space:
        sa_total += 6 - find_adjacent(block, space)
    print(sa_total - sa_airblocks)

def find_enclosed(space):
    check_range = 20
    space_all = list(itertools.product(range(check_range + 1), repeat=3))
    airblocks = [block for block in space_all if block not in space]
    print("got airblocks", len(airblocks))
    pool = mp.Pool(mp.cpu_count())
    results = pool.starmap(touches_air, [(b, space) for b in airblocks])
    enclosed_airblocks = [b for b, r in zip(airblocks, results) if not r]
    return enclosed_airblocks

def find_adjacent(block, space):
    num_adj = 0
    for b in space:
        if abs(b[0] - block[0]) + abs(b[1] - block[1]) + abs(b[2] - block[2]) == 1:
            num_adj += 1
    return num_adj

def touches_air(block, space):
    check_range = 20
    visited = set()
    to_visit = queue.Queue()
    to_visit.put(block)
    while not to_visit.empty():
        b = to_visit.get()
        if b in visited:
            continue
        visited.add(b)
        if b in space:
            continue
        if b[0] == check_range or b[1] == check_range or b[2] == check_range:
            return True
        for i in range(-1, 2):
            if i == 0:
                continue
            to_visit.put((b[0] + i, b[1], b[2]))
            to_visit.put((b[0], b[1] + i, b[2]))
            to_visit.put((b[0], b[1], b[2] + i))
    print(block, 'does not touch air')
    return False
        

    
        
        

      

if __name__ == '__main__':
    main()