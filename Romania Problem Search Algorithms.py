

# Arad -> Shibiu:140, Timisoara:118, Zerind:75
# Bucharest -> Fagaras:211, Glurgiu:90, Pitesti:101, Urziceni:85
# Craiova -> Drobeta:120, Pitesti:101, Rimnicu Vilcea:146
# Deobeta -> Craiova:120, Mehadia:75
# Eforie -> Hirsova:86
# Fagaras -> Bucharest:211, Sibiu:99
# Giurgiu -> Bucharest:90
# Hirsova -> Eforie:86, Urziceni:98
# Iasi -> Neamt:87, Vaslui:92
# Lugoj -> Mehadia:70, Timisoara:111
# Mehadia -> Drobeta:75, Lugoj:70
# Neamt -> Iasi:87
# Oradea -> Sibiu:151, Zerind:71
# Pitesti -> Bucharest:101, Craiova:138, Rimnicu Vilcea:97
# Rimnicu Vilcea -> Craiova:146, Pitesti:97, Sibiu:80
# Sibiu -> Arad:140, Fagaras:99, Oradea:151, Pimnicu Vilcea:80
# Timisoara -> Arad:118, Lugoj:111
# Urziceni -> Bucharest:85, Hirsova:98, Vaslui:142
# Vaslui -> Iasi:92, Urziceni:142
# Zerind -> Arad:75, Oradea:71

# in alphabetical order

        # Arad, Bucharest, Craiova, ..., Urziceni, Vaslui, Zerind
mtx = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 140, 118, 0, 0, 75],   # Arad
       [0, 0, 0, 0, 0, 211, 90, 0, 0, 0, 0, 0, 0, 101, 0, 0, 0, 85, 0, 0],  # Bucharest
       [0, 0, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 138, 146, 0, 0, 0, 0, 0],  # Craiova
       [0, 0, 120, 0, 0, 0, 0, 0, 0, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0],     # Deobeta
       [0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],       # Eforie
       [0, 211, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99, 0, 0, 0, 0],     # Fagaras
       [0, 90, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],       # Giurgiu
       [0, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 98, 0, 0],      # Hirsova
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0, 0, 0, 92, 0],      # Iasi
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 0, 111, 0, 0, 0],     # Lugoj
       [0, 0, 0, 75, 0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],      # Mehadia
       [0, 0, 0, 0, 0, 0, 0, 0, 87, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],       # Neamt
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 151, 0, 0, 0, 71],     # Oradea
       [0, 101, 138, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 97, 0, 0, 0, 0, 0],   # Pitesti
       [0, 0, 146, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 97, 0, 80, 0, 0, 0, 0],    # Rimnicu Vilcea
       [140, 0, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 151, 0, 80, 0, 0, 0, 0, 0],  # Sibiu
       [118, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    # Timisoara
       [0, 85, 0, 0, 0, 0, 0, 98, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 142, 0],    # Urziceni
       [0, 0, 0, 0, 0, 0, 0, 0, 92, 0, 0, 0, 0, 0, 0, 0, 0, 142, 0, 0],     # Vaslui
       [75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 71, 0, 0, 0, 0, 0, 0, 0]]      # Zerind


def addInf(mtx):
    for i in range(0, len(mtx)):

        for j in range(0, len(mtx[0])):

            if mtx[i][j] == 0 and i != j:
                mtx[i][j] = float('inf')
            else:
                mtx[i][j] == mtx[i][j]


def floydWarshall(mtx, start, end):
        
    addInf(mtx)

    routes = []
    for x in range(0, len(mtx)):
        routes.append([])
        for y in range(0, len(mtx[0])):
            if(mtx[x][y] == float('inf')):
                routes[x].append(-1)
            else:
                routes[x].append(y)
                

    prev = mtx
    n = len(mtx)

    
    for k in range(0,n):

        for i in range(0,n):

            for j in range(0,n):
                if(prev[i][j] > prev[i][k] + prev[k][j]):
                    mtx[i][j] = prev[i][k] + prev[k][j]
                    routes[i][j] = routes[i][k] 
                else:
                    mtx[i][j] = prev[i][j]

    prev = mtx

    u = start
    v = end
    route = [u]
    while(u != v):
        u = routes[u][v]
        route.append(u)

    print(mtx)
    print("from "+str(start)+" to "+str(end)+": "+str(mtx[start][end]))
    print("path: "+str(route))

    
def minimumDist(dist, visited):

    minimum = float('inf')

    for i in range(0, len(visited)):
        if(visited[i]==False and dist[i]<=minimum):
            minimum=dist[i]
            index=i

    return index

def dijkstra(mtx, start, end):
    dist = [float('inf')] * len(mtx)
    visited = [False] * len(mtx)


    routes = []
    for i in range(0, len(mtx)):
        routes.append([i])

    dist[start] = 0
    # current node
    for c in range(0,len(mtx)):
        mD = minimumDist(dist, visited)
        visited[mD]=True
        # checking all other nodes
        for v in range(0, len(mtx)):
            # not visited, there is a connection, it has a dist, and dist to mD + dist from mD to v < dist v 
            if(not visited[v] and mtx[mD][v] and dist[mD] != float('inf') and dist[mD]+mtx[mD][v] < dist[v]):
                dist[v] = dist[mD] + mtx[mD][v]
                routes[mD].append(v)
            

    second = False
    restart = False
    testRoutes = True
    testTotal = 0 
    path = []
    starting = True
    wrongStart = 0
    startIdx = 0
    prev = end
    while(testRoutes):
        if(restart):
            startIdx = wrongStart
            second = True
            restart = False
        
        for i in range(startIdx, len(routes)):
            if(restart):
                break
            for j in range(1, len(routes[i])):
                if(routes[i][j] == prev):
                    if(starting):
                        if (second):
                            startIdx = 0
                        wrongStart = i+1
                        starting = False
                    testTotal += mtx[i][prev]
                    path.insert(0, prev)
                    prev = routes[i][0]
                if(testTotal > dist[end]):
                    starting = True
                    testTotal = 0
                    prev = end
                    restart = True
                    path = []
                    break
                elif(testTotal == dist[end]):
                    testRoutes = False
                    
                
    path.insert(0, start)
        
        
    print("from "+str(start)+" to "+str(end)+": "+str(dist[end]))
    print("path: "+str(path))





def heuristicFunction(mtx, node, visitedList):

    smallest = float('inf')
    
    for i in range(0, len(visitedList)):

        if(visitedList[i] == False):

            if(mtx[node][i] < smallest and mtx[node][i] != 0):
                smallest = mtx[node][i]

    return smallest
            

def aStar(mtx, start, end):
    dist = [float('inf')] * len(mtx)
    visited = [False] * len(mtx)

    routes = []
    for i in range(0, len(mtx)):
        routes.append([i])

    dist[start] = 0
    # current node
    for c in range(0,len(mtx)):
        mD = minimumDist(dist, visited)
        visited[mD]=True
        # checking all other nodes
        for v in range(0, len(mtx)):
            # not visited, there is a connection, it has a dist, and cost of path from start to v + heuristic < dist v 
            if(not visited[v] and mtx[mD][v] and dist[mD] != float('inf') and dist[mD] + heuristicFunction(mtx,v,visited) < dist[v]):
                dist[v] = dist[mD] + mtx[mD][v]
                routes[mD].append(v)


    second = False
    restart = False
    testRoutes = True
    testTotal = 0 
    path = []
    starting = True
    wrongStart = 0
    startIdx = 0
    prev = end
    while(testRoutes):
        if(restart):
            startIdx = wrongStart
            second = True
            restart = False
        
        for i in range(startIdx, len(routes)):
            if(restart):
                break
            for j in range(1, len(routes[i])):
                if(routes[i][j] == prev):
                    if(starting):
                        if (second):
                            startIdx = 0
                        wrongStart = i+1
                        starting = False
                    testTotal += mtx[i][prev]
                    path.insert(0, prev)
                    prev = routes[i][0]
                if(testTotal > dist[end]):
                    starting = True
                    testTotal = 0
                    prev = end
                    restart = True
                    path = []
                    break
                elif(testTotal == dist[end]):
                    testRoutes = False
                    
                
    path.insert(0, start)
        
        
    print("from "+str(start)+" to "+str(end)+": "+str(dist[end]))
    print("path: "+str(path))



print("Dijkstra:")
dijkstra(mtx, 0, 1)
print("")
print("A*:")
aStar(mtx, 0, 1)
print("")
print("Floyd-Warshall:")
floydWarshall(mtx, 0, 1)



