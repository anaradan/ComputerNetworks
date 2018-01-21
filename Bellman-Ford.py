## Implementation of Bellman-Ford algorithm

import pdb

#function initializes distances and predecessors
#for each node distance from source is infinite and there is no predecessors
#distance source from itself is 0
def initialize(graph, source):
    d = {} #distances
    p = {} #predecessors
    
    for node in graph:
        d[node] = float('Inf') #set value of nodes to infinite
        p[node] = None #set value of predecessors to 0
    d[source] = 0 # source has no distance from itself
    return d, p


#function checks if there is shorter path to specific node
def relax(node, neighbour, graph, d, p):
    #if distance between node and his neighboor is shorter
    #than current saved value
    if d[neighbour] > d[node] + graph[node][neighbour]:
        # smaller value is saved
        d[neighbour]  = d[node] + graph[node][neighbour]
        #predecessor of the neighboor is node that is checked
        p[neighbour] = node

#function that implements algorithm
def bellman_ford(graph, source):
    #initialization of distance and predecessors
    d, p = initialize(graph, source)
    #looping through each node as many times as there is nodes
    for i in range(len(graph)-1):
        for u in graph: #for each node in graph
            for v in graph[u]: #for each neighboor
                relax(u, v, graph, d, p) #check if current path is shorter than saved one

    #check if there is negativ cycle
    #loop through each node once
    for u in graph:
        for v in graph[u]: #for each neighboor of u
            #distance of source to neighboor has to be smaller than
            #distance of current node and distance between node and neighboor 
            assert d[v] <= d[u] + graph[u][v] 
    return d, p

#sets graph
def test():
    graph = {
        'a': {'b': -2, 'c': 1, 'd': 4},
        'b': {'e': 3},
        'c': {'b': -3, 'd': 2},
        'd': {'e': -1},
        'e': {'c': 5}
        }

    d, p = bellman_ford(graph, 'a')
    print ("The shortest distance from source a to all other nodes is:")
    for u in graph:
        print(u,"=",d[u])
    print ("Paths from source a to all other nodes(predecessors of nodes):")
    for u in graph:
        print(u,"=",p[u])

#main
if __name__ == '__main__': test()
