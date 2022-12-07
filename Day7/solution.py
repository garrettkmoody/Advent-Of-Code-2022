def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        stack = []
        directory = {}
        currentDirectory = None
        
        for line in lines:

            if '$ cd ..\n' == line:
                stack.pop()
                continue
            if '$ cd ' in line:
                path = ""
                for name in stack:
                    path += name
                currentDirectory = line.split()[2] + path
                stack.append(currentDirectory)

                directory[currentDirectory] = 0
                continue
            if '$ ls\n' == line:
                continue

            if line.split()[0].isdigit():
                directory[currentDirectory] += int(line.split()[0])
                for dir in stack[:-1]:
                    directory[dir] += int(line.split()[0])
            else:
                path = ""
                for name in stack:
                    path += name
                if line.split()[1] + path not in directory: 
                    directory[line.split()[1] + path] = 0
                else:
                    directory[line.split()[1] + path] = 0

        summer = 0
        for key in directory:
            
            if directory[key] <= 100000:
                summer += directory[key]
           


    print("Solution to Part 1: {}".format(summer))

    
def part2():

    with open('input.txt') as f:
        lines = f.readlines()
        stack = []
        directory = {}
        currentDirectory = None
        for line in lines:

            if '$ cd ..\n' == line:
                stack.pop()
                continue
            if '$ cd ' in line:
                path = ""
                for name in stack:
                    path += name
                currentDirectory = line.split()[2] + path
                stack.append(currentDirectory)

                directory[currentDirectory] = 0
                continue
            if '$ ls\n' == line:
                continue

            if line.split()[0].isdigit():
                directory[currentDirectory] += int(line.split()[0])
                for dir in stack[:-1]:
                    directory[dir] += int(line.split()[0])
            else:
                path = ""
                for name in stack:
                    path += name
                if line.split()[1] + path not in directory: 
                    directory[line.split()[1] + path] = 0
                else:
                    directory[line.split()[1] + path] = 0

        potdelete = []
        for key in directory:
            if directory[key] >= 30000000 - (70000000 - directory['/']):
                potdelete.append(directory[key])

    print("Solution to Part 2: {}".format(min(potdelete)))
            


if __name__ == '__main__':
    main()