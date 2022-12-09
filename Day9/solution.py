def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()

        currentTail = (0,0)
        currentHead = (0,0)

        uniqueVisits = set([])

        uniqueVisits.add(currentTail)

        for line in lines:
            direction, steps = line.split()
            
            for _ in range(int(steps)):

                if direction == 'U':
                    currentHead = (currentHead[0], currentHead[1] + 1)

                elif direction == 'D':
                    currentHead = (currentHead[0], currentHead[1] - 1)
                    
                elif direction == 'R':
                    currentHead = (currentHead[0] + 1, currentHead[1])
                    
                elif direction == 'L':
                    currentHead = (currentHead[0] - 1, currentHead[1])
                  
                currentTail = moveTail(currentTail, currentHead, uniqueVisits)
            
    print("Solution to Part 1: {}".format(len(uniqueVisits)))

def moveTail(currentTail, currentHead, uniqueVisit):

    if abs(currentTail[0] - currentHead[0]) < 2 and abs(currentTail[1] - currentHead[1]) < 2:
        return currentTail
    else:
     
        if currentHead[0] > currentTail[0] and currentHead[1] == currentTail[1]:
           
            currentTail = (currentTail[0] + 1, currentTail[1])
            uniqueVisit.add(currentTail)
            return currentTail
        
      
        elif currentHead[0] < currentTail[0] and currentHead[1] == currentTail[1]:
            currentTail = (currentTail[0] - 1, currentTail[1])
            uniqueVisit.add(currentTail)
            return currentTail
       
        elif currentHead[0] == currentTail[0] and currentHead[1] > currentTail[1]:
            currentTail = (currentTail[0], currentTail[1]+1)
            uniqueVisit.add(currentTail)
            return currentTail
      
        elif currentHead[0] == currentTail[0] and currentHead[1] < currentTail[1]:
            currentTail = (currentTail[0], currentTail[1]-1)
            uniqueVisit.add(currentTail)
            return currentTail
        
        elif currentHead[0] != currentTail[0] and currentHead[1] != currentTail[1]:
            
            if abs(currentHead[0] - currentTail[0]) == 2 and abs(currentHead[1] - currentTail[1]) == 2:
                if currentHead[0] > currentTail[0]:

                    currentTail = (currentTail[0] + 1, currentTail[1])
                else:
                    currentTail = (currentTail[0] - 1, currentTail[1])

                if currentHead[1] > currentTail[1]:

                    currentTail = (currentTail[0], currentTail[1] + 1)
                else:
                    currentTail = (currentTail[0], currentTail[1] - 1)

            else:

                if abs(currentHead[0] - currentTail[0]) == 1:
                    currentTail = (currentHead[0], currentTail[1])
                    if currentHead[1] > currentTail[1]:

                        currentTail = (currentTail[0], currentTail[1] + 1)
                    else:
                    
                        currentTail = (currentTail[0], currentTail[1] - 1)
                else:
                    currentTail = (currentTail[0], currentHead[1])
                    if currentHead[0] > currentTail[0]:
                        currentTail = (currentTail[0] + 1, currentTail[1])
                    else:
                        currentTail = (currentTail[0] - 1, currentTail[1])

                
            uniqueVisit.add(currentTail)
            return currentTail
        
        

def part2():

    with open('input.txt') as f:
        lines = f.readlines()

        rope = []

        for _ in range(10):
            rope.append((0,0))

        
        uniqueVisits = set([])

        uniqueVisits.add((0,0))

        for line in lines:
            direction, steps = line.split()
            
            for _ in range(int(steps)):

                if direction == 'U':
                    rope[0] = (rope[0][0], rope[0][1] + 1)

                elif direction == 'D':
                    rope[0] = (rope[0][0], rope[0][1] - 1)
                    
                elif direction == 'R':
                    rope[0] = (rope[0][0] + 1, rope[0][1])
                    
                elif direction == 'L':
                    rope[0] = (rope[0][0] - 1, rope[0][1])

                for i in range(1,10):
                    if i == 9:
                        rope[i] = moveTail2(rope[i], rope[i - 1], uniqueVisits, True)
        
                    
                    rope[i] = moveTail2(rope[i], rope[i - 1], uniqueVisits, False)

            
            
    print("Solution to Part 2: {}".format(len(uniqueVisits)))

def moveTail2(currentTail, currentHead, uniqueVisit, tail):

    if abs(currentTail[0] - currentHead[0]) < 2 and abs(currentTail[1] - currentHead[1]) < 2:
        return currentTail
    else:
   
        if currentHead[0] > currentTail[0] and currentHead[1] == currentTail[1]:
           
            currentTail = (currentTail[0] + 1, currentTail[1])
            if tail:
                uniqueVisit.add(currentTail)
             
            return currentTail
        
      
        elif currentHead[0] < currentTail[0] and currentHead[1] == currentTail[1]:
            currentTail = (currentTail[0] - 1, currentTail[1])
            if tail:
                uniqueVisit.add(currentTail)
               

            return currentTail
    
        elif currentHead[0] == currentTail[0] and currentHead[1] > currentTail[1]:
            currentTail = (currentTail[0], currentTail[1]+1)
            if tail:
                uniqueVisit.add(currentTail)

            return currentTail
  
        elif currentHead[0] == currentTail[0] and currentHead[1] < currentTail[1]:
            currentTail = (currentTail[0], currentTail[1]-1)
            if tail:
                uniqueVisit.add(currentTail)  

            return currentTail
     
        elif currentHead[0] != currentTail[0] and currentHead[1] != currentTail[1]:
            
            if currentHead[0] > currentTail[0]:

                currentTail = (currentTail[0] + 1, currentTail[1])
            else:
                currentTail = (currentTail[0] - 1, currentTail[1])

            if currentHead[1] > currentTail[1]:

                currentTail = (currentTail[0], currentTail[1] + 1)
            else:
                currentTail = (currentTail[0], currentTail[1] - 1)
                
            if tail:
                uniqueVisit.add(currentTail)
                
            
            return currentTail

if __name__ == '__main__':
    main()