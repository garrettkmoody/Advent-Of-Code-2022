#reduce graph
def reduceGraph(adjMatrix, flowDict):

    zeroKeys = [x for x in adjMatrix.keys() if flowDict[x] == 0]
    
    distancesDict = {}
    distancesDict['AA'] = dijkstra_algorithm(adjMatrix, 'AA')[1]
    for key in [key for key in adjMatrix.keys() if flowDict[key] > 0]:
        distancesDict[key] = dijkstra_algorithm(adjMatrix, key)[1]
    for key in distancesDict:
        for zeroKey in zeroKeys:
            if zeroKey in distancesDict[key]:
                del distancesDict[key][zeroKey]
    
    for key in distancesDict:
        print(distancesDict[key])

    return distancesDict

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


 