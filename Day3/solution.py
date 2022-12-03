def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        prio = 0

        for line in lines:
            
            com1 = line[:len(line)//2]
            com2 = line[len(line)//2:]
        
            for let in com1:
                if let in com2:   
                    if let.isupper():
                        prio += ord(let) - 64 + 26
                    else:
                        prio += ord(let) - 96
                    break

    print("Solution to Part 1: {}".format(prio))

def part2():

    with open('input.txt') as f:
        lines = f.readlines()

        
        prio = 0

        lineArr = []
        for line in lines:
            lineArr.append(line)
            if len(lineArr) == 3:
                
                for let in lineArr[0]:
                    if let in lineArr[1] and let in lineArr[2]:   
                        if let.isupper():
                            prio += ord(let) - 64 + 26
                        else:
                            prio += ord(let) - 96
                        lineArr.clear()
                        break
                
            

    print("Solution to Part 2: {}".format(prio))

if __name__ == '__main__':
    main()