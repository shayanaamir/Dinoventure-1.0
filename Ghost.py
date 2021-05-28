def ghosts():
    x, y = 0, 0
    movex, movey = 0, 0

    while True:
        random.randiant = move(1, 2, 3, 4)
        if random.randiant == 1:
            movex = -1
        elif random.randiant == 2:
            movex = +1
        elif random.randiant == 3:
            movey = -1
        elif random.randiant == 4:
            movey = +1

        x += movex
        y += movey

def clyde(node_graph, to, start_node_clyde):
    x, y = 0, 0
    movex, movey = 0, 0

    while True:
        random.randiant = move(1, 2, 3, 4)
        if random.randiant == 1:
            movex = -1
        elif random.randiant == 2:
            movex = +1
        elif random.randiant == 3:
            movey = -1
        elif random.randiant == 4:
            movey = +1

        x += movex
        y += movey


clyde_picture = pygame.image.load("Clyde.png")
print(clyde_picture)
clyde_speed_left = -speed
clyde_speed_right = speed
clyde_speed_up = -speed
clyde_speed_down = speed
clyde_x = node_graph["+ 6"]["(x, y)"][0]
clyde_y = node_graph["+ 6"]["(x, y)"][1]
start_node_clyde = "+ 6"
clyde_path = clyde(node_graph, (x, y), start_node_clyde)
clyde_speed_x = 0
clyde_speed_y = 0