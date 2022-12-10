def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        signalstrength = 0
        x = 1
        cycle = 1
        check = 20
        for line in lines:
            
            command = line.split()
            if len(command) == 2:
                x += int(command[1])
                cycle += 2
            else:
                cycle += 1
    
            if cycle == check or cycle == check - 1:
                signalstrength += check * x
                check += 40
        

    print("Solution to Part 1: {}".format(signalstrength))

def part2():

    with open('input.txt') as f:
        with open('result.txt', 'w') as o:
            lines = f.readlines()  
            x = 1
            cycle = 0
            offset = False
            instructions = []
            currentRow = ""
            rowPointer = 0
            for i in range(len(lines) * 2 - 40):
                cycle += 1
                if i < len(lines):
                    line = lines[i]
                else:
                    line = "NOOP"

                #clock tick draw 1 pixel
                if abs(rowPointer - x) < 2:
                    currentRow += '#'
                else:
                    currentRow += '.'
                rowPointer += 1

                command = line.split()

                if len(command) == 2:
                    instructions.insert(0,int(command[1]))
                else:
                    instructions.insert(0,"NOOP")
                
                if cycle % 2 == offset:
                    val = instructions.pop()
                    if val == "NOOP":
                        offset = not offset
                    else:
                        x += val
                
                if rowPointer == 40:
                 
                    rowPointer = 0
                    o.write(currentRow + '\n')
                    currentRow = ""    



if __name__ == '__main__':
    main()