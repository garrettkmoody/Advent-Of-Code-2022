def main():
    part1()
    part2()

specialNumber = 1

class Monkey:
    items = []
    operation = None
    test = None
    monkey_true = None
    monkey_false = None
    inspectionCount = 0
    part2 = False

    def inspect(self):

        if len(self.items) == 0:
            return -1
        self.inspectionCount += 1
        item = self.items.pop(0)
        
        if self.operation[0] == '+':
            if self.operation[1] == 'old':
                item += item
            else:
                item += int(self.operation[1])
        elif self.operation[0] == '*':
            if self.operation[1] == 'old':
                item *= item
            else:
                item *= int(self.operation[1])

        if not self.part2:
            item = item // 3
        else:    
            overFlow = len(str(item)) - len(str(specialNumber))

            while overFlow > 0:
                multiplyNumber = int(str(item)[0:overFlow])
                item -= (specialNumber * multiplyNumber)
                overFlow = len(str(item)) - len(str(specialNumber))

        if item % self.test == 0:
            return (item, self.monkey_true)
        else:
            return (item, self.monkey_false)


def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        monkeys = []
        currentMonkey = Monkey()
        
        for line in lines:
            if 'Starting items' in line:
                currentMonkey.items = [int(x) for x in line[17:].split(',')]
            elif 'Operation' in line:
                currentMonkey.operation = line[23:].split()
            elif 'Test' in line:
                currentMonkey.test = int(line[20:])
            elif 'If true' in line:
                currentMonkey.monkey_true = int(line[29:])
            elif 'If false' in line:
                currentMonkey.monkey_false = int(line[30:])
            elif '\n' == line:
                monkeys.append(currentMonkey)
                currentMonkey = Monkey()

        for _ in range(20): 
            for monkey in monkeys:
                while True:
                    info = monkey.inspect()
                    if info == -1:
                        break
                    item, location = info  
                    monkeys[location].items.append(item)  
        max1 = 0
        max2 = 0
        for monkey in monkeys:
            if monkey.inspectionCount > max1:
                max2 = max1
                max1 = monkey.inspectionCount
                
            elif monkey.inspectionCount > max2:
                max2 = monkey.inspectionCount

    print("Solution to Part 1: {}".format(max1 * max2))

def part2():

    with open('input.txt') as f:
        lines = f.readlines()
        monkeys = []
        currentMonkey = Monkey()

        for line in lines:
            currentMonkey.part2 = True
            if 'Starting items' in line:
                currentMonkey.items = [int(x) for x in line[17:].split(',')]
            elif 'Operation' in line:
                currentMonkey.operation = line[23:].split()
            elif 'Test' in line:
                currentMonkey.test = int(line[20:])
            elif 'If true' in line:
                currentMonkey.monkey_true = int(line[29:])
            elif 'If false' in line:
                currentMonkey.monkey_false = int(line[30:])
            elif '\n' == line:
                monkeys.append(currentMonkey)
                currentMonkey = Monkey()

        global specialNumber
        for monkey in monkeys:
            specialNumber *= monkey.test

        for _ in range(10000):
            for monkey in monkeys:
                while True:
                    info = monkey.inspect()
                    if info == -1:
                        break
                    item, location = info  
                    monkeys[location].items.append(item)
        max1 = 0
        max2 = 0
        for monkey in monkeys:
            if monkey.inspectionCount > max1:
                max2 = max1
                max1 = monkey.inspectionCount
                
            elif monkey.inspectionCount > max2:
                max2 = monkey.inspectionCount     

    print("Solution to Part 2: {}".format(max1 * max2))

if __name__ == '__main__':
    main()