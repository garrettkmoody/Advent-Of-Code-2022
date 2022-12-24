def main():
    # part1()
    part2()

class Node:
    def __init__(self, val, next = None, back = None) -> None:
        self.val = val
        self.next = next
        self.back = back

def part1():

    with open('input.txt') as f:
        lines = f.readlines()
        head = Node(int(lines[0]))
        originalOrder= [head]
        current = head
        for i in range(1, len(lines)):
            originalOrder.append(Node(int(lines[i])))
            current.next = originalOrder[-1]
            originalOrder[-1].back = current
            current = current.next
        
        originalOrder[-1].next = head
        head.back = originalOrder[-1]

        
        for node in originalOrder:

            if node.val != 0:
                node.back.next = node.next
                node.next.back = node.back

                current = node

                for i in range(abs(node.val)):
                    if node.val > 0:
                        current = current.next
                    else:
                        current = current.back

                if node.val < 0:
                    current = current.back
                
                node.next = current.next
                current.next.back = node
                current.next = node
                node.back = current
        
        node1 = 1000 % len(lines)
        node2 = 2000 % len(lines)
        node3 = 3000 % len(lines)
        
        nodes = {}
        current = head
        startCount = False
        counter = 0
        
        while len(nodes) != 3:
            if counter == node1:
                nodes[1] = current.val
            elif counter == node2:
                nodes[2] = current.val
            elif counter == node3:
                nodes[3] = current.val
            elif current.val == 0:
                startCount = True
            
            if startCount:
                counter += 1
            current = current.next
            

    print("Solution to Part 1: {}".format(sum([nodes[x] for x in [1,2,3]])))

def part2():

    key = 811589153

    with open('input.txt') as f:
        lines = f.readlines()
        head = Node(int(lines[0]) * key)
        zeroNode = None
        originalOrder= [head]
        current = head
        for i in range(1, len(lines)):
            originalOrder.append(Node(int(lines[i]) * key))
            if int(lines[i]) == 0:
                zeroNode = originalOrder[-1]
            current.next = originalOrder[-1]
            originalOrder[-1].back = current
            current = current.next
        
        originalOrder[-1].next = head
        head.back = originalOrder[-1]
        
        for _ in range(10):
            for node in originalOrder:

                if node.val != 0:
                    node.back.next = node.next
                    node.next.back = node.back

                    current = node
                    
                    traverseVal = node.val % (len(lines) - 1) if node.val > 0 else node.val % -(len(lines)-1)
                    
                    for i in range(abs(traverseVal)):
                        if node.val > 0:
                            current = current.next
                        else:
                            current = current.back

                    if node.val < 0:
                        current = current.back
                    
                    node.next = current.next
                    current.next.back = node
                    current.next = node
                    node.back = current
        
        currentNode = head
        counter = 0
        while counter < 7:
            print(currentNode.val, end=' ')
            counter += 1
            currentNode = currentNode.next

        node1 = 1000 % len(lines)
        node2 = 2000 % len(lines)
        node3 = 3000 % len(lines)
        nodes = {}
        current = zeroNode
        counter = 0
        while len(nodes) != 3:
            
            if counter == node1:
                nodes[1] = current.val
            elif counter == node2:
                nodes[2] = current.val
            elif counter == node3:
                nodes[3] = current.val
            
            counter += 1
            current = current.next
            

    print("Solution to Part 2: {}".format(sum([nodes[x] for x in [1,2,3]])))

if __name__ == '__main__':
    main()