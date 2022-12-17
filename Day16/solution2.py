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
        
        reduceGraph(adjMatrix, flowDict)
        # print(adjMatrix)
        # print(flowDict)
            
   

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