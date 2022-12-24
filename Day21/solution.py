def main():
    part1()
    part2()

def part1():

    with open('input.txt') as f:
        lines = [line.replace(':','').split() for line in f.readlines()]
        monkey_log = {}
        for line in lines:
            if len(line) == 4:
                monkey_log[line[0]] = line[1:]
            else:
                monkey_log[line[0]] = int(line[1])
        
        answer = int(beautifulRecursion("root", monkey_log))

    print("Solution to Part 1: {}".format(answer))

def beautifulRecursion(monkey, monkey_log):

    if isinstance(monkey_log[monkey],int):
        return monkey_log[monkey]
    
    operator = monkey_log[monkey][1]
    if operator == '+':
        return beautifulRecursion(monkey_log[monkey][0], monkey_log) + beautifulRecursion(monkey_log[monkey][2], monkey_log)
    elif operator == '-':
        return beautifulRecursion(monkey_log[monkey][0], monkey_log) - beautifulRecursion(monkey_log[monkey][2], monkey_log)
    elif operator == '*':
        return beautifulRecursion(monkey_log[monkey][0], monkey_log) * beautifulRecursion(monkey_log[monkey][2], monkey_log)
    elif operator == '/':
        return beautifulRecursion(monkey_log[monkey][0], monkey_log) / beautifulRecursion(monkey_log[monkey][2], monkey_log)

def gorgeousRecursion(monkey, monkey_log):

    if isinstance(monkey_log[monkey],int):
        return monkey_log[monkey]
    
    operator = monkey_log[monkey][1]
    if monkey == 'root':
        return (beautifulRecursion(monkey_log[monkey][0], monkey_log), beautifulRecursion(monkey_log[monkey][2], monkey_log))

    if operator == '+':
        return beautifulRecursion(monkey_log[monkey][0], monkey_log) + beautifulRecursion(monkey_log[monkey][2], monkey_log)
    elif operator == '-':
        return beautifulRecursion(monkey_log[monkey][0], monkey_log) - beautifulRecursion(monkey_log[monkey][2], monkey_log)
    elif operator == '*':
        return beautifulRecursion(monkey_log[monkey][0], monkey_log) * beautifulRecursion(monkey_log[monkey][2], monkey_log)
    elif operator == '/':
        return beautifulRecursion(monkey_log[monkey][0], monkey_log) / beautifulRecursion(monkey_log[monkey][2], monkey_log)

def part2():

    with open('input.txt') as f:
        lines = [line.replace(':','').split() for line in f.readlines()]
        monkey_log = {}
        for line in lines:
            if line[0] == 'humn':
                continue
            if len(line) == 4:
                monkey_log[line[0]] = line[1:]
            else:
                monkey_log[line[0]] = int(line[1])
        
        
        monkey_log['humn'] = 3509819803008
        
        while True:
            monkey_log['humn'] += 1
            if gorgeousRecursion("root", monkey_log)[0] == gorgeousRecursion("root", monkey_log)[1]:
                break

    print("Solution to Part 2: {}".format(monkey_log['humn']))

if __name__ == '__main__':
    main()