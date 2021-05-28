import pprint
import math

def loadfile(file_name):
    txt = open(file_name, "r")
    maze = []
    count = 0
    count_1 = 0
    for i in txt:
        #print(i)
        row = i.split()
        for j in range(len(row)):
            if row[j] == "+" or row[j] == "P":
                st = row.pop(j)
                st += " "
                st += str(count)
                count += 1
                row.insert(j, st)

            elif row[j] == "s" or row[j] == "S" or row[j] == "P":
                st = row.pop(j)
                st += " "
                st += str(count_1)
                count_1 += 1
                row.insert(j, st)
        maze.append(row)
    return maze

def make_coordinates(maze):
    startY = 3
    maze_final = []
    for i in maze:
        maze2 = []
        startX = 120
        for j in i:
            maze3 = [j, startX, startY]
            startX += 20
            maze2.append(maze3)
        maze_final.append(maze2)
        startY += 20
    return maze_final

def make_edges(maze, edges, edges_final):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j][0].split()[0] == "+":
                edges.append(maze[i][j])
                for k in range(i + 1, len(maze)):
                    if maze[k][j][0].split()[0] == "+" and maze[k][j] != maze[i][j]:
                        edges.append(["Down: ", maze[k][j]])
                        break
                    if maze[k][j][0] == "w" or maze[k][j][0] == "s":
                        break
                for l in range(j + 1, len(maze[i])):
                    if maze[i][l][0].split()[0] == "+":
                        edges.append(["Right: ", maze[i][l]])
                        break
                    if maze[i][l][0] == "w" or maze[i][l][0] == "s":
                        break
    for i in range(len(edges)):
        e = []
        if edges[i][0].split()[0] == "+":
            e.append(edges[i])
            for j in range(i + 1, len(edges)):
                if edges[j][0].split()[0] == "+":
                    break
                else:
                    e.append(edges[j])
        if e:
            edges_final.append(e)
    return edges_final

def addNodes(node_graph, edges_final):
    for i in edges_final:
        node_graph[i[0][0]] = {"(x, y)": [i[0][1], i[0][2]], "Up": [], "Down": [], "Left": [], "Right": []}
    return node_graph

def addEdges(node_Graph, edges_final):
    for i in edges_final:
        for j in range(1, len(i)):
            b = i[j]
            if b[0] == "Down: ":
                node_Graph[i[0][0]]["Down"].append(b[1][0])
                node_Graph[b[1][0]]["Up"].append(i[0][0])
            elif b[0] == "Right: ":
                node_Graph[i[0][0]]["Right"].append(b[1][0])
                node_Graph[b[1][0]]["Left"].append(i[0][0])
    return node_Graph

def construct_graph(file_name, edges, edges_final, node_graph):
    maze = loadfile(file_name)
    maze = make_coordinates(maze)
    make_edges(maze, edges, edges_final)
    addNodes(node_graph, edges_final)
    addEdges(node_graph, edges_final)
    return maze

def construct_wall_node_graph(maze, wall_node_graph):
    wall_edges = []
    wall_edges_final = []
    wall_edges_final = wall_make_edges(maze, wall_edges, wall_edges_final)
    addNodes(wall_node_graph, wall_edges_final)
    addEdges(wall_node_graph, wall_edges_final)
    print(wall_node_graph)

def wall_make_edges(maze, wall_edges, wall_edges_final):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            h = maze[i][j]
            h1 = maze[i][j][0].split()
            h2 = maze[i][j][0].split()[0]
            if maze[i][j][0].split()[0] == "s" or maze[i][j][0].split()[0] == "S":
                wall_edges.append(maze[i][j])
                count = 0
                for k in range(i + 1, len(maze)):
                    if (maze[k][j][0].split()[0] == "s" or maze[k][j][0].split()[0] == "S") and maze[k][j] != maze[i][j]:
                        if count == 0 and maze[k][j][0].split()[0] == "s":
                            break
                        elif maze[k][j][0] == "." or maze[k][j][0] == "p":
                            break
                        elif maze[k][j][0] == "w":
                            continue
                        else:
                            wall_edges.append(["Down: ", maze[k][j]])
                            break
                    if maze[k][j][0] == "." or maze[k][j][0] == "p":
                        break
                    count += 1
                count = 0
                for l in range(j + 1, len(maze[i])):
                    if maze[i][l][0].split()[0] == "s" or maze[i][l][0].split()[0] == "S":
                        if count == 0 and maze[i][l][0].split()[0] == "s":
                            break
                        elif maze[i][l][0] == "." or maze[i][l][0] == "p":
                            break
                        elif maze[i][l][0] == "w":
                            continue
                        else:
                            wall_edges.append(["Right: ", maze[i][l]])
                            break
                    if maze[i][l][0] == "." or maze[i][l][0] == "p":
                        break
                    count += 1
    for i in range(len(wall_edges)):
        e = []
        if wall_edges[i][0].split()[0] == "s" or wall_edges[i][0].split()[0] == "S":
            e.append(wall_edges[i])
            for j in range(i + 1, len(wall_edges)):
                if wall_edges[j][0].split()[0] == "s" or wall_edges[j][0].split()[0] == "S":
                    break
                else:
                    e.append(wall_edges[j])
        if e:
            wall_edges_final.append(e)
    return wall_edges_final

def add_distance(node_graph):
    for i in node_graph:
        x1, y1 = node_graph[i]["(x, y)"][0], node_graph[i]["(x, y)"][1]
        for j in node_graph[i]:
            if j != "(x, y)":
                if node_graph[i][j]:
                    node = node_graph[i][j][0]
                    x2, y2 = node_graph[node]["(x, y)"][0], node_graph[node]["(x, y)"][1]
                    distance = math.sqrt(((y2 - y1) ** 2) + ((x2 - x1) ** 2))
                    node_graph[i][j].append(distance)

file_name ="C:\\Users\\Zohaib\\PycharmProjects\\untitled\\Pacman level_11.txt"
edges = []
edges_final = []
node_graph = {}
wall_node_graph = {}
maze = construct_graph(file_name, edges, edges_final, node_graph)
wall_node_graph = construct_wall_node_graph(maze, wall_node_graph)
add_distance(node_graph)
##print(wall_node_graph)
##print(node_graph)

def dijkstra1(Graph, Source):
    d = {}
    d[Source] = [Source, 0]
    for v in Graph:
        if v != Source:
            d[v] = ["", math.inf]
    visited = []
    for i in Graph:
        current_node = ""
        small = math.inf
        for node in d:
            if node not in visited and d[node][-1] < small:
                small = d[node][1]
                current_node = node
        visited.append(current_node)
        for n in Graph[current_node]:
            if n != "(x, y)" and Graph[current_node][n]:
                if Graph[current_node][n][0] not in visited:
                    weight = Graph[current_node][n][1]
                    if d[Graph[current_node][n][0]][1] > small + weight:
                        d[Graph[current_node][n][0]][1] = small + weight
                        d[Graph[current_node][n][0]][0] = current_node
    return d

def getShortestPath1(G, From, to):
    a = dijkstra1(G, From)
    lst = []
    for i in G:
        for j in G:
            t = ()
            if j == to and a[to][1] != 0:
                t += (a[to][0], to, a[to][1])
                to = a[to][0]
                lst.append(t)
    return lst[::-1]


def portal():

#print(maze)
#print(getShortestPath1(node_graph, "+ 0", "+ 2"))


