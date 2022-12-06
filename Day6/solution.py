def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        line = f.readline()
      
        uniqueSet = list(line[:3])
        for i in range(3, len(line)):
            uniqueSet.append(line[i])
            done = False
            for j in range(len(uniqueSet)):
                if done:
                    break
                for e in range(j + 1, len(uniqueSet)):
                    if uniqueSet[j] == uniqueSet[e]:
                        uniqueSet.pop(0)
                        done = True
                        break
    
            if done == False:
                print("Solution to Part 1: {}".format(i + 1))
                break
   

def part2():

    with open('input.txt') as f:
        line = f.readline()
        uniqueSet = list(line[:13])
    
        for i in range(3, len(line)):
            uniqueSet.append(line[i])
            done = False
            for j in range(len(uniqueSet)):
                if done:
                    break
                for e in range(j + 1, len(uniqueSet)):
                    if uniqueSet[j] == uniqueSet[e]:
                        uniqueSet.pop(0)
                        done = True
                        break
            
            if done == False:
                print("Solution to Part 2: {}".format(i + 1))
                break
    

if __name__ == '__main__':
    main()