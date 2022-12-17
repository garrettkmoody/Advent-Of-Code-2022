#reduce graph
def reduceGraph(adjMatrix, flowDict):
    # badKeys = []
    # for key in adjMatrix:
    #     if key != 'AA' and flowDict[key] == 0:
    #         for i in range(len(adjMatrix[key])-1):
    #             for j in range(i + 1, len(adjMatrix[key])):
    #                 leftValve = adjMatrix[key][i]
    #                 rightValve = adjMatrix[key][j]
    #                 newDistance = leftValve[1] + rightValve[1]
    #                 found = False
    #                 for z, valve in enumerate(adjMatrix[leftValve[0]]):
    #                     if valve[0] == rightValve[0] and valve[1] > newDistance:
    #                         found = True
    #                         adjMatrix[leftValve[0]][z] = (rightValve[0], newDistance)
    #                         adjMatrix[leftValve[0]] = [x for x in adjMatrix[leftValve[0]] if x[0] != key]
    #                         for x, valve in enumerate(adjMatrix[rightValve[0]]):
    #                             if valve[0] == leftValve[0]:
    #                                 adjMatrix[rightValve[0]][x] = (leftValve[0], newDistance)
    #                                 adjMatrix[rightValve[0]] = [x for x in adjMatrix[rightValve[0]] if x[0] != key]
    #                 if not found:
    #                     adjMatrix[leftValve[0]].append((rightValve[0], newDistance))
    #                     adjMatrix[rightValve[0]].append((leftValve[0], newDistance))
    #                     adjMatrix[leftValve[0]] = [x for x in adjMatrix[leftValve[0]] if x[0] != key]
    #                     adjMatrix[rightValve[0]] = [x for x in adjMatrix[rightValve[0]] if x[0] != key]
    #         badKeys.append(key)
    # for key in badKeys:
    #     del adjMatrix[key]
    
    print(dijkstra_algorithm(adjMatrix, 'AA'))


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.keys())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}
 
    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}
 
    # We'll use max_value to initialize the "infinity" value of the unvisited nodes   
    max_value = float('inf')
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0   
    shortest_path[start_node] = 0
    
    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes: # Iterate over the nodes
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph[current_min_node]
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + 1
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node
 
        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path


 