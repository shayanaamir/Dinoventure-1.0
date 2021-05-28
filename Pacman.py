import pygame
import time
import math

pygame.init()

display_width = 1024
display_height = 670

gameDisplay = pygame.display.set_mode((display_width, display_height))  # window size

pygame.display.set_caption("Pacman")  # set window title

clock = pygame.time.Clock()

def pacman(x, y, file):
    #Pacman = pygame.draw.circle(gameDisplay, Yellow, (int(x), int(y)), 7)
    #circle = pygame.Surface((60, 60), pygame.SRCALPHA)
    gameDisplay.blit(file, (int(x) - 10, int(y) - 10))

def blinky_draw(blinky_x, blinky_y):
    #Pacman = pygame.draw.circle(gameDisplay, red, (int(x), int(y)), 7)
    #circle = pygame.Surface((60, 60), pygame.SRCALPHA)
    gameDisplay.blit(blinky_picture, (blinky_x - 10, blinky_y - 10))

def clyde_draw(clyde_x, clyde_y):
    #Pacman = pygame.draw.circle(gameDisplay, red, (int(x), int(y)), 7)
    #circle = pygame.Surface((60, 60), pygame.SRCALPHA)
    gameDisplay.blit(clyde_picture, (clyde_x - 10, clyde_y - 10))

def main(x, y, node_graph, speed_right, speed_left, speed_up, speed_down, maze, wall_node_graph, Pacman_right, Pacman_left, Pacman_up, Pacman_down, file, blinky_speed_left, blinky_speed_right, blinky_speed_up, blinky_speed_down, blinky_x, blinky_y, start_node_blinky, blinky_path, blinky_speed_x, blinky_speed_y):
    if blinky_path:
        destination_node_blinky = blinky_path[0][1]
        destination_node_blinky_x = node_graph[blinky_path[0][1]]["(x, y)"][0]
        destination_node_blinky_y = node_graph[blinky_path[0][1]]["(x, y)"][1]
    while True:
        for event in pygame.event.get():  # gets event
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    end_node_x = node_exist_left(node_graph, x, y)
                    end_node_y = -10
                    if x != end_node_x:
                        file = Pacman_left
                        speed_x = speed_left
                        speed_y = 0
                        a, b = ghost_node_check_left(node_graph, x, y)
                        blinky_speed_x = 0
                        blinky_speed_y = 0
                        if blinky_path:
                            destination_node_blinky = blinky_path[0][1]
                            destination_node_blinky_x = node_graph[blinky_path[0][1]]["(x, y)"][0]
                            destination_node_blinky_y = node_graph[blinky_path[0][1]]["(x, y)"][1]
                        while True:
                            blinky_x += blinky_speed_x
                            blinky_y += blinky_speed_y
                            if True:
                                if blinky_x == destination_node_blinky_x and blinky_y == destination_node_blinky_y:
                                    start_node_blinky = destination_node_blinky
                                    blinky_path = blinky(node_graph, (a, b), start_node_blinky)
                                    if len(blinky_path) == 0:
                                        if blinky_x < x and y == blinky_y:
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_x > x and y == blinky_y:
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y < y and x == blinky_x:
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y > y and x == blinky_x:
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                if blinky_path:
                                    destination_node_blinky = blinky_path[0][1]
                                    destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                    destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    if blinky_y == destination_node_blinky_y:
                                        if blinky_x > destination_node_blinky_x:
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_x < destination_node_blinky_x:
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif blinky_x == destination_node_blinky_x:
                                        if blinky_y > destination_node_blinky_y:
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y < destination_node_blinky_y:
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                else:
                                    if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                                        blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                                        blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                                        if x > blinky_x and blinky_ghost_right == True:
                                            node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Left"]:
                                                start_node_blinky = node_graph[node_blinky]["Left"][0]
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif x < blinky_x and blinky_ghost_left == True:
                                            node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Right"]:
                                                start_node_blinky = node_graph[node_blinky]["Right"][0]
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                                        blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                                        blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                                        if y > blinky_y and blinky_ghost_down == True:
                                            node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Up"]:
                                                start_node_blinky = node_graph[node_blinky]["Up"][0]
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif y < blinky_y and blinky_ghost_up == True:
                                            node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Down"]:
                                                start_node_blinky = node_graph[node_blinky]["Down"][0]
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                            else:
                                if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                                    blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                                    blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                                    if x > blinky_x and blinky_ghost_right == True:
                                        node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Left"]:
                                            start_node_blinky = node_graph[node_blinky]["Left"][0]
                                        blinky_speed_x = blinky_speed_right
                                        blinky_speed_y = 0
                                        destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif x < blinky_x and blinky_ghost_left == True:
                                        node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Right"]:
                                            start_node_blinky = node_graph[node_blinky]["Right"][0]
                                        blinky_speed_x = blinky_speed_left
                                        blinky_speed_y = 0
                                        destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                                    blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                                    blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                                    if y > blinky_y and blinky_ghost_down == True:
                                        node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Up"]:
                                            start_node_blinky = node_graph[node_blinky]["Up"][0]
                                        blinky_speed_y = blinky_speed_down
                                        blinky_speed_x = 0
                                        destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif y < blinky_y and blinky_ghost_up == True:
                                        node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Down"]:
                                            start_node_blinky = node_graph[node_blinky]["Down"][0]
                                        blinky_speed_y = blinky_speed_up
                                        blinky_speed_x = 0
                                        destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                            x += speed_x
                            y += speed_y
                            plot_positions(node_graph, maze, wall_node_graph, pellets_eaten, x, y)
                            pacman(x, y, file)
                            blinky_draw(blinky_x, blinky_y)
                            pygame.display.update()
                            gameDisplay.fill(black)
                            for event_1 in pygame.event.get():
                                if event_1.type == pygame.KEYDOWN:
                                    if event_1.key == pygame.K_LEFT:
                                        if speed_x == 0:
                                            for i in node_graph:
                                                if y > node_graph[i]["(x, y)"][1] - 15 and y < node_graph[i]["(x, y)"][1] + 15 and x == node_graph[i]["(x, y)"][0]:
                                                    y = node_graph[i]["(x, y)"][1]
                                                    end_node_x = node_exist_left(node_graph, x, y)
                                                    if end_node_x == x:
                                                        end_node_x = -10
                                                if end_node_x != x and y == node_graph[i]["(x, y)"][1] and end_node_x != -10:
                                                    file = Pacman_left
                                                    speed_x = speed_left
                                                    speed_y = 0
                                                    end_node_y = -10
                                                    break
                                        else:
                                            if speed_x == speed_right:
                                                file = Pacman_left
                                                speed_x = speed_left
                                                Min = math.inf
                                                for i in node_graph:
                                                    if y in node_graph[i]["(x, y)"]:
                                                        if node_graph[i]["(x, y)"][0] - x < Min and node_graph[i]["(x, y)"][0] - x > 0:
                                                            Min = node_graph[i]["(x, y)"][0] - x
                                                            x_left = node_graph[i]["(x, y)"][0]
                                                end_node_x = node_exist_left(node_graph, x_left, y)
                                    elif event_1.key == pygame.K_RIGHT:
                                        if speed_x == 0:
                                            for i in node_graph:
                                                if y > node_graph[i]["(x, y)"][1] - 15 and y < node_graph[i]["(x, y)"][1] + 15 and x == node_graph[i]["(x, y)"][0]:
                                                    y = node_graph[i]["(x, y)"][1]
                                                    end_node_x = node_exist_right(node_graph, x, y)
                                                    if end_node_x == x:
                                                        end_node_x = -10
                                                if end_node_x != x and y == node_graph[i]["(x, y)"][1] and end_node_x != -10:
                                                    file = Pacman_right
                                                    speed_x = speed_right
                                                    speed_y = 0
                                                    end_node_y = -10
                                                    break
                                        else:
                                            if speed_x == speed_left:
                                                file = Pacman_right
                                                speed_x = speed_right
                                                Min = math.inf
                                                for i in node_graph:
                                                    if y in node_graph[i]["(x, y)"]:
                                                        if x - node_graph[i]["(x, y)"][0] < Min and x - node_graph[i]["(x, y)"][0] > 0:
                                                            Min = x - node_graph[i]["(x, y)"][0]
                                                            x_right = node_graph[i]["(x, y)"][0]
                                                end_node_x = node_exist_right(node_graph, x_right, y)
                                    elif event_1.key == pygame.K_UP:
                                        if speed_y == 0:
                                            for i in node_graph:
                                                if x > node_graph[i]["(x, y)"][0] - 15 and x < node_graph[i]["(x, y)"][0] + 15 and y == node_graph[i]["(x, y)"][1]:
                                                    x = node_graph[i]["(x, y)"][0]
                                                    end_node_y = node_exist_up(node_graph, x, y)
                                                    if end_node_y == y:
                                                        end_node_y = -10
                                                if end_node_y != y and x == node_graph[i]["(x, y)"][0] and end_node_y != -10:
                                                    file = Pacman_up
                                                    speed_x = 0
                                                    speed_y = speed_up
                                                    end_node_x = -10
                                                    break
                                        else:
                                            if speed_y == speed_down:
                                                file = Pacman_up
                                                speed_y = speed_up
                                                Min = math.inf
                                                for i in node_graph:
                                                    if x in node_graph[i]["(x, y)"]:
                                                        if y - node_graph[i]["(x, y)"][1] < Min and y - node_graph[i]["(x, y)"][1] > 0:
                                                            Min = y - node_graph[i]["(x, y)"][1]
                                                            y_up = node_graph[i]["(x, y)"][1]
                                                end_node_y = node_exist_up(node_graph, x, y_up)
                                    elif event_1.key == pygame.K_DOWN:
                                        if speed_y == 0:
                                            for i in node_graph:
                                                if x > node_graph[i]["(x, y)"][0] - 15 and x < node_graph[i]["(x, y)"][0] + 15 and y == node_graph[i]["(x, y)"][1]:
                                                    x = node_graph[i]["(x, y)"][0]
                                                    end_node_y = node_exist_down(node_graph, x, y)
                                                    if end_node_y == y:
                                                        end_node_y = -10
                                                if end_node_y != y and x == node_graph[i]["(x, y)"][0] and end_node_y != -10:
                                                    file = Pacman_down
                                                    speed_x = 0
                                                    speed_y = speed_down
                                                    end_node_x = -10
                                                    break
                                        else:
                                            if speed_y == speed_up:
                                                file = Pacman_down
                                                speed_y = speed_down
                                                Min = math.inf
                                                for i in node_graph:
                                                    if x in node_graph[i]["(x, y)"]:
                                                        if node_graph[i]["(x, y)"][1] - y < Min and node_graph[i]["(x, y)"][1] - y > 0:
                                                            Min = node_graph[i]["(x, y)"][1] - y
                                                            y_down = node_graph[i]["(x, y)"][1]
                                                end_node_y = node_exist_down(node_graph, x, y_down)
                            if x == end_node_x:
                                break
                            if y == end_node_y:
                                break
                            if speed_x == speed_right:
                                a, b = ghost_node_check_right(node_graph, x, y)
                            elif speed_x == speed_left:
                                a, b = ghost_node_check_left(node_graph, x, y)
                            elif speed_y == speed_up:
                                a, b = ghost_node_check_up(node_graph, x, y)
                            elif speed_y == speed_down:
                                a, b = ghost_node_check_down(node_graph, x, y)
                elif event.key == pygame.K_RIGHT:
                    end_node_x = node_exist_right(node_graph, x, y)
                    end_node_y = -10
                    if x != end_node_x:
                        speed_x = speed_right
                        speed_y = 0
                        file = Pacman_right
                        a, b = ghost_node_check_right(node_graph, x, y)
                        blinky_speed_x = 0
                        blinky_speed_y = 0
                        if blinky_path:
                            destination_node_blinky = blinky_path[0][1]
                            destination_node_blinky_x = node_graph[blinky_path[0][1]]["(x, y)"][0]
                            destination_node_blinky_y = node_graph[blinky_path[0][1]]["(x, y)"][1]
                        while True:
                            blinky_x += blinky_speed_x
                            blinky_y += blinky_speed_y
                            if True:
                                if blinky_x == destination_node_blinky_x and blinky_y == destination_node_blinky_y:
                                    start_node_blinky = destination_node_blinky
                                    blinky_path = blinky(node_graph, (a, b), start_node_blinky)
                                    if len(blinky_path) == 0:
                                        if blinky_x < x and y == blinky_y:
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_x > x and y == blinky_y:
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y < y and x == blinky_x:
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y > y and x == blinky_x:
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                if blinky_path:
                                    destination_node_blinky = blinky_path[0][1]
                                    destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                    destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    if blinky_y == destination_node_blinky_y:
                                        if blinky_x > destination_node_blinky_x:
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_x < destination_node_blinky_x:
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif blinky_x == destination_node_blinky_x:
                                        if blinky_y > destination_node_blinky_y:
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y < destination_node_blinky_y:
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                else:
                                    if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                                        blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                                        blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                                        if x > blinky_x and blinky_ghost_right == True:
                                            node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Left"]:
                                                start_node_blinky = node_graph[node_blinky]["Left"][0]
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif x < blinky_x and blinky_ghost_left == True:
                                            node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Right"]:
                                                start_node_blinky = node_graph[node_blinky]["Right"][0]
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                                        blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                                        blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                                        if y > blinky_y and blinky_ghost_down == True:
                                            node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Up"]:
                                                start_node_blinky = node_graph[node_blinky]["Up"][0]
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif y < blinky_y and blinky_ghost_up == True:
                                            node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Down"]:
                                                start_node_blinky = node_graph[node_blinky]["Down"][0]
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                            else:
                                if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                                    blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                                    blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                                    if x > blinky_x and blinky_ghost_right == True:
                                        node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Left"]:
                                            start_node_blinky = node_graph[node_blinky]["Left"][0]
                                        blinky_speed_x = blinky_speed_right
                                        blinky_speed_y = 0
                                        destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif x < blinky_x and blinky_ghost_left == True:
                                        node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Right"]:
                                            start_node_blinky = node_graph[node_blinky]["Right"][0]
                                        blinky_speed_x = blinky_speed_left
                                        blinky_speed_y = 0
                                        destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                                    blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                                    blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                                    if y > blinky_y and blinky_ghost_down == True:
                                        node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Up"]:
                                            start_node_blinky = node_graph[node_blinky]["Up"][0]
                                        blinky_speed_y = blinky_speed_down
                                        blinky_speed_x = 0
                                        destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif y < blinky_y and blinky_ghost_up == True:
                                        node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Down"]:
                                            start_node_blinky = node_graph[node_blinky]["Down"][0]
                                        blinky_speed_y = blinky_speed_up
                                        blinky_speed_x = 0
                                        destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                            x += speed_x
                            y += speed_y
                            plot_positions(node_graph, maze, wall_node_graph, pellets_eaten, x, y)
                            pacman(x, y, file)
                            blinky_draw(blinky_x, blinky_y)
                            pygame.display.update()
                            gameDisplay.fill(black)
                            for event_2 in pygame.event.get():
                                if event_2.type == pygame.KEYDOWN:
                                    if event_2.key == pygame.K_LEFT:
                                        if speed_x == 0:
                                            for i in node_graph:
                                                if y > node_graph[i]["(x, y)"][1] - 15 and y < node_graph[i]["(x, y)"][1] + 15 and x == node_graph[i]["(x, y)"][0]:
                                                    y = node_graph[i]["(x, y)"][1]
                                                    end_node_x = node_exist_left(node_graph, x, y)
                                                    if end_node_x == x:
                                                        end_node_x = -10
                                                if end_node_x != x and y == node_graph[i]["(x, y)"][1] and end_node_x != -10:
                                                    file = Pacman_left
                                                    speed_x = speed_left
                                                    speed_y = 0
                                                    end_node_y = -10
                                                    break
                                        else:
                                            if speed_x == speed_right:
                                                file = Pacman_left
                                                speed_x = speed_left
                                                Min = math.inf
                                                for i in node_graph:
                                                    if y in node_graph[i]["(x, y)"]:
                                                        if node_graph[i]["(x, y)"][0] - x < Min and node_graph[i]["(x, y)"][0] - x > 0:
                                                            Min = node_graph[i]["(x, y)"][0] - x
                                                            x_left  = node_graph[i]["(x, y)"][0]
                                                end_node_x = node_exist_left(node_graph, x_left, y)
                                    elif event_2.key == pygame.K_RIGHT:
                                        if speed_x == 0:
                                            for i in node_graph:
                                                if y > node_graph[i]["(x, y)"][1] - 15 and y < node_graph[i]["(x, y)"][1] + 15 and x == node_graph[i]["(x, y)"][0]:
                                                    y = node_graph[i]["(x, y)"][1]
                                                    end_node_x = node_exist_right(node_graph, x, y)
                                                    if end_node_x == x:
                                                        end_node_x = -10
                                                if end_node_x != x and y == node_graph[i]["(x, y)"][1] and end_node_x != -10:
                                                    file = Pacman_right
                                                    speed_x = speed_right
                                                    speed_y = 0
                                                    end_node_y = -10
                                                    break
                                        else:
                                            if speed_x == speed_left:
                                                file = Pacman_right
                                                speed_x = speed_right
                                                Min = math.inf
                                                for i in node_graph:
                                                    if y in node_graph[i]["(x, y)"]:
                                                        if x - node_graph[i]["(x, y)"][0] < Min and x - node_graph[i]["(x, y)"][0] > 0:
                                                            Min = x - node_graph[i]["(x, y)"][0]
                                                            x_right = node_graph[i]["(x, y)"][0]
                                                end_node_x = node_exist_right(node_graph, x_right, y)
                                    elif event_2.key == pygame.K_UP:
                                        if speed_y == 0:
                                            for i in node_graph:
                                                if x > node_graph[i]["(x, y)"][0] - 15 and x < node_graph[i]["(x, y)"][0] + 15 and y == node_graph[i]["(x, y)"][1]:
                                                    x = node_graph[i]["(x, y)"][0]
                                                    end_node_y = node_exist_up(node_graph, x, y)
                                                    if end_node_y == y:
                                                        end_node_y = -10
                                                if end_node_y != y and x == node_graph[i]["(x, y)"][0] and end_node_y != -10:
                                                    file = Pacman_up
                                                    speed_x = 0
                                                    speed_y = speed_up
                                                    end_node_x = -10
                                                    break
                                        else:
                                            if speed_y == speed_down:
                                                file = Pacman_up
                                                speed_y = speed_up
                                                Min = math.inf
                                                for i in node_graph:
                                                    if x in node_graph[i]["(x, y)"]:
                                                        if y - node_graph[i]["(x, y)"][1] < Min and y - node_graph[i]["(x, y)"][1] > 0:
                                                            Min = y - node_graph[i]["(x, y)"][1]
                                                            y_up = node_graph[i]["(x, y)"][1]
                                                end_node_y = node_exist_up(node_graph, x, y_up)
                                    elif event_2.key == pygame.K_DOWN:
                                        if speed_y == 0:
                                            for i in node_graph:
                                                if x > node_graph[i]["(x, y)"][0] - 15 and x < node_graph[i]["(x, y)"][0] + 15 and y == node_graph[i]["(x, y)"][1]:
                                                    x = node_graph[i]["(x, y)"][0]
                                                    end_node_y = node_exist_down(node_graph, x, y)
                                                    if end_node_y == y:
                                                        end_node_y = -10
                                                if end_node_y != y and x == node_graph[i]["(x, y)"][0] and end_node_y != -10:
                                                    file = Pacman_down
                                                    speed_x = 0
                                                    speed_y = speed_down
                                                    end_node_x = -10
                                                    break
                                        else:
                                            if speed_y == speed_up:
                                                file = Pacman_down
                                                speed_y = speed_down
                                                Min = math.inf
                                                for i in node_graph:
                                                    if x in node_graph[i]["(x, y)"]:
                                                        if node_graph[i]["(x, y)"][1] - y < Min and node_graph[i]["(x, y)"][1] - y > 0:
                                                            Min =node_graph[i]["(x, y)"][1] - y
                                                            y_down = node_graph[i]["(x, y)"][1]
                                                end_node_y = node_exist_down(node_graph, x, y_down)
                            if x == end_node_x:
                                break
                            if y == end_node_y:
                                break
                            if speed_x == speed_right:
                                a, b = ghost_node_check_right(node_graph, x, y)
                            elif speed_x == speed_left:
                                a, b = ghost_node_check_left(node_graph, x, y)
                            elif speed_y == speed_up:
                                a, b = ghost_node_check_up(node_graph, x, y)
                            elif speed_y == speed_down:
                                a, b = ghost_node_check_down(node_graph, x, y)
                elif event.key == pygame.K_UP:
                    end_node_y = node_exist_up(node_graph, x, y)
                    end_node_x = -10
                    if y != end_node_y:
                        speed_x = 0
                        speed_y = speed_up
                        file = Pacman_up
                        a, b = ghost_node_check_up(node_graph, x, y)
                        blinky_speed_x = 0
                        blinky_speed_y = 0
                        if blinky_path:
                            destination_node_blinky = blinky_path[0][1]
                            destination_node_blinky_x = node_graph[blinky_path[0][1]]["(x, y)"][0]
                            destination_node_blinky_y = node_graph[blinky_path[0][1]]["(x, y)"][1]
                        while True:
                            blinky_x += blinky_speed_x
                            blinky_y += blinky_speed_y
                            if True:
                                if blinky_x == destination_node_blinky_x and blinky_y == destination_node_blinky_y:
                                    start_node_blinky = destination_node_blinky
                                    blinky_path = blinky(node_graph, (a, b), start_node_blinky)
                                    if len(blinky_path) == 0:
                                        if blinky_x < x and y == blinky_y:
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_x > x and y == blinky_y:
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y < y and x == blinky_x:
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y > y and x == blinky_x:
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                if blinky_path:
                                    destination_node_blinky = blinky_path[0][1]
                                    destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                    destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    if blinky_y == destination_node_blinky_y:
                                        if blinky_x > destination_node_blinky_x:
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_x < destination_node_blinky_x:
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif blinky_x == destination_node_blinky_x:
                                        if blinky_y > destination_node_blinky_y:
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y < destination_node_blinky_y:
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                else:
                                    if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                                        blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                                        blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                                        if x > blinky_x and blinky_ghost_right == True:
                                            node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Left"]:
                                                start_node_blinky = node_graph[node_blinky]["Left"][0]
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif x < blinky_x and blinky_ghost_left == True:
                                            node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Right"]:
                                                start_node_blinky = node_graph[node_blinky]["Right"][0]
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                                        blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                                        blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                                        if y > blinky_y and blinky_ghost_down == True:
                                            node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Up"]:
                                                start_node_blinky = node_graph[node_blinky]["Up"][0]
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif y < blinky_y and blinky_ghost_up == True:
                                            node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Down"]:
                                                start_node_blinky = node_graph[node_blinky]["Down"][0]
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                            else:
                                if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                                    blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                                    blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                                    if x > blinky_x and blinky_ghost_right == True:
                                        node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Left"]:
                                            start_node_blinky = node_graph[node_blinky]["Left"][0]
                                        blinky_speed_x = blinky_speed_right
                                        blinky_speed_y = 0
                                        destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif x < blinky_x and blinky_ghost_left == True:
                                        node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Right"]:
                                            start_node_blinky = node_graph[node_blinky]["Right"][0]
                                        blinky_speed_x = blinky_speed_left
                                        blinky_speed_y = 0
                                        destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                                    blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                                    blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                                    if y > blinky_y and blinky_ghost_down == True:
                                        node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Up"]:
                                            start_node_blinky = node_graph[node_blinky]["Up"][0]
                                        blinky_speed_y = blinky_speed_down
                                        blinky_speed_x = 0
                                        destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif y < blinky_y and blinky_ghost_up == True:
                                        node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Down"]:
                                            start_node_blinky = node_graph[node_blinky]["Down"][0]
                                        blinky_speed_y = blinky_speed_up
                                        blinky_speed_x = 0
                                        destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                            x += speed_x
                            y += speed_y
                            plot_positions(node_graph, maze, wall_node_graph, pellets_eaten, x, y)
                            pacman(x, y, file)
                            blinky_draw(blinky_x, blinky_y)
                            pygame.display.update()
                            gameDisplay.fill(black)
                            for event_3 in pygame.event.get():
                                if event_3.type == pygame.KEYDOWN:
                                    if event_3.key == pygame.K_LEFT:
                                        if speed_x == 0:
                                            for i in node_graph:
                                                if y > node_graph[i]["(x, y)"][1] - 15 and y < node_graph[i]["(x, y)"][1] + 15 and x == node_graph[i]["(x, y)"][0]:
                                                    y = node_graph[i]["(x, y)"][1]
                                                    end_node_x = node_exist_left(node_graph, x, y)
                                                    if end_node_x == x:
                                                        end_node_x = -10
                                                if end_node_x != x and y == node_graph[i]["(x, y)"][1] and end_node_x != -10:
                                                    file = Pacman_left
                                                    speed_x = speed_left
                                                    speed_y = 0
                                                    end_node_y = -10
                                                    break
                                        else:
                                            if speed_x == speed_right:
                                                file = Pacman_left
                                                speed_x = speed_left
                                                Min = math.inf
                                                for i in node_graph:
                                                    if y in node_graph[i]["(x, y)"]:
                                                        if node_graph[i]["(x, y)"][0] - x < Min and node_graph[i]["(x, y)"][0] - x > 0:
                                                            Min = node_graph[i]["(x, y)"][0] - x
                                                            x_left = node_graph[i]["(x, y)"][0]
                                                end_node_x = node_exist_left(node_graph, x_left, y)
                                    elif event_3.key == pygame.K_RIGHT:
                                        if speed_x == 0:
                                            for i in node_graph:
                                                if y > node_graph[i]["(x, y)"][1] - 15 and y < node_graph[i]["(x, y)"][1] + 15 and x == node_graph[i]["(x, y)"][0]:
                                                    y = node_graph[i]["(x, y)"][1]
                                                    end_node_x = node_exist_right(node_graph, x, y)
                                                    if end_node_x == x:
                                                        end_node_x = -10
                                                if end_node_x != x and y == node_graph[i]["(x, y)"][1] and end_node_x != -10:
                                                    file = Pacman_right
                                                    speed_x = speed_right
                                                    speed_y = 0
                                                    end_node_y = -10
                                                    break
                                        else:
                                            if speed_x == speed_left:
                                                file = Pacman_right
                                                speed_x = speed_right
                                                Min = math.inf
                                                for i in node_graph:
                                                    if y in node_graph[i]["(x, y)"]:
                                                        if x - node_graph[i]["(x, y)"][0] < Min and x - node_graph[i]["(x, y)"][0] > 0:
                                                            Min = x - node_graph[i]["(x, y)"][0]
                                                            x_right = node_graph[i]["(x, y)"][0]
                                                end_node_x = node_exist_right(node_graph, x_right, y)
                                    elif event_3.key == pygame.K_UP:
                                        if speed_y == 0:
                                            for i in node_graph:
                                                if x > node_graph[i]["(x, y)"][0] - 15 and x < node_graph[i]["(x, y)"][0] + 15 and y == node_graph[i]["(x, y)"][1]:
                                                    x = node_graph[i]["(x, y)"][0]
                                                    end_node_y = node_exist_up(node_graph, x, y)
                                                    if end_node_y == y:
                                                        end_node_y = -10
                                                if end_node_y != y and x == node_graph[i]["(x, y)"][0] and end_node_y != -10:
                                                    file = Pacman_up
                                                    speed_x = 0
                                                    speed_y = speed_up
                                                    end_node_x = -10
                                                    break
                                        else:
                                            if speed_y == speed_down:
                                                file = Pacman_up
                                                speed_y = speed_up
                                                Min = math.inf
                                                for i in node_graph:
                                                    if x in node_graph[i]["(x, y)"]:
                                                        if y - node_graph[i]["(x, y)"][1] < Min and y - node_graph[i]["(x, y)"][1] > 0:
                                                            Min = y - node_graph[i]["(x, y)"][1]
                                                            y_up = node_graph[i]["(x, y)"][1]
                                                end_node_y = node_exist_up(node_graph, x, y_up)
                                    elif event_3.key == pygame.K_DOWN:
                                        if speed_y == 0:
                                            for i in node_graph:
                                                if x > node_graph[i]["(x, y)"][0] - 15 and x < node_graph[i]["(x, y)"][0] + 15 and y == node_graph[i]["(x, y)"][1]:
                                                    x = node_graph[i]["(x, y)"][0]
                                                    end_node_y = node_exist_down(node_graph, x, y)
                                                    if end_node_y == y:
                                                        end_node_y = -10
                                                if end_node_y != y and x == node_graph[i]["(x, y)"][0] and end_node_y != -10:
                                                    file = Pacman_down
                                                    speed_x = 0
                                                    speed_y = speed_down
                                                    end_node_x = -10
                                                    break
                                        else:
                                            if speed_y == speed_up:
                                                file = Pacman_down
                                                speed_y = speed_down
                                                Min = math.inf
                                                for i in node_graph:
                                                    if x in node_graph[i]["(x, y)"]:
                                                        if node_graph[i]["(x, y)"][1] - y < Min and node_graph[i]["(x, y)"][1] - y > 0:
                                                            Min = node_graph[i]["(x, y)"][1] - y
                                                            y_down = node_graph[i]["(x, y)"][1]
                                                end_node_y = node_exist_down(node_graph, x, y_down)
                            if x == end_node_x:
                                break
                            if y == end_node_y:
                                break
                            if speed_x == speed_right:
                                a, b = ghost_node_check_right(node_graph, x, y)
                            elif speed_x == speed_left:
                                a, b = ghost_node_check_left(node_graph, x, y)
                            elif speed_y == speed_up:
                                a, b = ghost_node_check_up(node_graph, x, y)
                            elif speed_y == speed_down:
                                a, b = ghost_node_check_down(node_graph, x, y)
                elif event.key == pygame.K_DOWN:
                    end_node_y = node_exist_down(node_graph, x, y)
                    end_node_x = -10
                    if y != end_node_y:
                        speed_x = 0
                        speed_y = speed_down
                        file = Pacman_down
                        a, b = ghost_node_check_down(node_graph, x, y)
                        blinky_speed_x = 0
                        blinky_speed_y = 0
                        if blinky_path:
                            destination_node_blinky = blinky_path[0][1]
                            destination_node_blinky_x = node_graph[blinky_path[0][1]]["(x, y)"][0]
                            destination_node_blinky_y = node_graph[blinky_path[0][1]]["(x, y)"][1]
                        while True:
                            blinky_x += blinky_speed_x
                            blinky_y += blinky_speed_y
                            if True:
                                if blinky_x == destination_node_blinky_x and blinky_y == destination_node_blinky_y:
                                    start_node_blinky = destination_node_blinky
                                    blinky_path = blinky(node_graph, (a, b), start_node_blinky)
                                    if len(blinky_path) == 0:
                                        if blinky_x < x and y == blinky_y:
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_x > x and y == blinky_y:
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y < y and x == blinky_x:
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y > y and x == blinky_x:
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                if blinky_path:
                                    destination_node_blinky = blinky_path[0][1]
                                    destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                    destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    if blinky_y == destination_node_blinky_y:
                                        if blinky_x > destination_node_blinky_x:
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_x < destination_node_blinky_x:
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif blinky_x == destination_node_blinky_x:
                                        if blinky_y > destination_node_blinky_y:
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif blinky_y < destination_node_blinky_y:
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                else:
                                    if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                                        blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                                        blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                                        if x > blinky_x and blinky_ghost_right == True:
                                            node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Left"]:
                                                start_node_blinky = node_graph[node_blinky]["Left"][0]
                                            blinky_speed_x = blinky_speed_right
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif x < blinky_x and blinky_ghost_left == True:
                                            node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Right"]:
                                                start_node_blinky = node_graph[node_blinky]["Right"][0]
                                            blinky_speed_x = blinky_speed_left
                                            blinky_speed_y = 0
                                            destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                                        blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                                        blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                                        if y > blinky_y and blinky_ghost_down == True:
                                            node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Up"]:
                                                start_node_blinky = node_graph[node_blinky]["Up"][0]
                                            blinky_speed_y = blinky_speed_down
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                        elif y < blinky_y and blinky_ghost_up == True:
                                            node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            if node_graph[node_blinky]["Down"]:
                                                start_node_blinky = node_graph[node_blinky]["Down"][0]
                                            blinky_speed_y = blinky_speed_up
                                            blinky_speed_x = 0
                                            destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                            destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                            destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                            else:
                                if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                                    blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                                    blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                                    if x > blinky_x and blinky_ghost_right == True:
                                        node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Left"]:
                                            start_node_blinky = node_graph[node_blinky]["Left"][0]
                                        blinky_speed_x = blinky_speed_right
                                        blinky_speed_y = 0
                                        destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif x < blinky_x and blinky_ghost_left == True:
                                        node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Right"]:
                                            start_node_blinky = node_graph[node_blinky]["Right"][0]
                                        blinky_speed_x = blinky_speed_left
                                        blinky_speed_y = 0
                                        destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                                    blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                                    blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                                    if y > blinky_y and blinky_ghost_down == True:
                                        node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Up"]:
                                            start_node_blinky = node_graph[node_blinky]["Up"][0]
                                        blinky_speed_y = blinky_speed_down
                                        blinky_speed_x = 0
                                        destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                                    elif y < blinky_y and blinky_ghost_up == True:
                                        node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                        if node_graph[node_blinky]["Down"]:
                                            start_node_blinky = node_graph[node_blinky]["Down"][0]
                                        blinky_speed_y = blinky_speed_up
                                        blinky_speed_x = 0
                                        destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                            x += speed_x
                            y += speed_y
                            plot_positions(node_graph, maze, wall_node_graph, pellets_eaten, x, y)
                            pacman(x, y, file)
                            blinky_draw(blinky_x, blinky_y)

                            pygame.display.update()
                            gameDisplay.fill(black)
                            for event_4 in pygame.event.get():
                                if event_4.type == pygame.KEYDOWN:
                                    if event_4.key == pygame.K_LEFT:
                                        if speed_x == 0:
                                            for i in node_graph:
                                                if y > node_graph[i]["(x, y)"][1] - 15 and y < node_graph[i]["(x, y)"][1] + 15 and x == node_graph[i]["(x, y)"][0]:
                                                    y = node_graph[i]["(x, y)"][1]
                                                    end_node_x = node_exist_left(node_graph, x, y)
                                                    if end_node_x == x:
                                                        end_node_x = -10
                                                if end_node_x != x and y == node_graph[i]["(x, y)"][1] and end_node_x != -10:
                                                    file = Pacman_left
                                                    speed_x = speed_left
                                                    speed_y = 0
                                                    end_node_y = -10
                                                    break
                                        else:
                                            if speed_x == speed_right:
                                                file = Pacman_left
                                                speed_x = speed_left
                                                Min = math.inf
                                                for i in node_graph:
                                                    if y in node_graph[i]["(x, y)"]:
                                                        if node_graph[i]["(x, y)"][0] - x < Min and node_graph[i]["(x, y)"][0] - x > 0:
                                                            Min = node_graph[i]["(x, y)"][0] - x
                                                            x_left = node_graph[i]["(x, y)"][0]
                                                end_node_x = node_exist_left(node_graph, x_left, y)
                                    elif event_4.key == pygame.K_RIGHT:
                                        if speed_x == 0:
                                            for i in node_graph:
                                                if y > node_graph[i]["(x, y)"][1] - 15 and y < node_graph[i]["(x, y)"][1] + 15 and x == node_graph[i]["(x, y)"][0]:
                                                    y = node_graph[i]["(x, y)"][1]
                                                    end_node_x = node_exist_right(node_graph, x, y)
                                                    if end_node_x == x:
                                                        end_node_x = -10
                                                if end_node_x != x and y == node_graph[i]["(x, y)"][1] and end_node_x != -10:
                                                    file = Pacman_right
                                                    speed_x = speed_right
                                                    speed_y = 0
                                                    end_node_y = -10
                                                    break
                                        else:
                                            if speed_x == speed_left:
                                                file = Pacman_right
                                                speed_x = speed_right
                                                Min = math.inf
                                                for i in node_graph:
                                                    if y in node_graph[i]["(x, y)"]:
                                                        if x - node_graph[i]["(x, y)"][0] < Min and x - node_graph[i]["(x, y)"][0] > 0:
                                                            Min = x - node_graph[i]["(x, y)"][0]
                                                            x_right = node_graph[i]["(x, y)"][0]
                                                end_node_x = node_exist_right(node_graph, x_right, y)
                                    elif event_4.key == pygame.K_UP:
                                        if speed_y == 0:
                                            for i in node_graph:
                                                if x > node_graph[i]["(x, y)"][0] - 15 and x < node_graph[i]["(x, y)"][0] + 15 and y == node_graph[i]["(x, y)"][1]:
                                                    x = node_graph[i]["(x, y)"][0]
                                                    end_node_y = node_exist_up(node_graph, x, y)
                                                    if end_node_y == y:
                                                        end_node_y = -10
                                                if end_node_y != y and x == node_graph[i]["(x, y)"][0] and end_node_y != -10:
                                                    file = Pacman_up
                                                    speed_x = 0
                                                    speed_y = speed_up
                                                    end_node_x = -10
                                                    break
                                        else:
                                            if speed_y == speed_down:
                                                file = Pacman_up
                                                speed_y = speed_up
                                                Min = math.inf
                                                for i in node_graph:
                                                    if x in node_graph[i]["(x, y)"]:
                                                        if y - node_graph[i]["(x, y)"][1] < Min and y - node_graph[i]["(x, y)"][1] > 0:
                                                            Min = y - node_graph[i]["(x, y)"][1]
                                                            y_up = node_graph[i]["(x, y)"][1]
                                                end_node_y = node_exist_up(node_graph, x, y_up)
                                    elif event_4.key == pygame.K_DOWN:
                                        if speed_y == 0:
                                            for i in node_graph:
                                                if x > node_graph[i]["(x, y)"][0] - 15 and x < node_graph[i]["(x, y)"][0] + 15 and y == node_graph[i]["(x, y)"][1]:
                                                    x = node_graph[i]["(x, y)"][0]
                                                    end_node_y = node_exist_down(node_graph, x, y)
                                                    if end_node_y == y:
                                                        end_node_y = -10
                                                if end_node_y != y and x == node_graph[i]["(x, y)"][0] and end_node_y != -10:
                                                    file = Pacman_down
                                                    speed_x = 0
                                                    speed_y = speed_down
                                                    end_node_x = -10
                                                    break
                                        else:
                                            if speed_y == speed_up:
                                                file = Pacman_down
                                                speed_y = speed_down
                                                Min = math.inf
                                                for i in node_graph:
                                                    if x in node_graph[i]["(x, y)"]:
                                                        if node_graph[i]["(x, y)"][1] - y < Min and node_graph[i]["(x, y)"][1] - y > 0:
                                                            Min = node_graph[i]["(x, y)"][1] - y
                                                            y_down = node_graph[i]["(x, y)"][1]
                                                end_node_y = node_exist_down(node_graph, x, y_down)
                            if x == end_node_x:
                                break
                            if y == end_node_y:
                                break
                            if speed_x == speed_right:
                                a, b = ghost_node_check_right(node_graph, x, y)
                            elif speed_x == speed_left:
                                a, b = ghost_node_check_left(node_graph, x, y)
                            elif speed_y == speed_up:
                                a, b = ghost_node_check_up(node_graph, x, y)
                            elif speed_y == speed_down:
                                a, b = ghost_node_check_down(node_graph, x, y)
        blinky_x += blinky_speed_x
        blinky_y += blinky_speed_y
        if blinky_path:
            if blinky_x == destination_node_blinky_x and blinky_y == destination_node_blinky_y:
                start_node_blinky = destination_node_blinky
                blinky_path = blinky(node_graph, (a, b), start_node_blinky)
                if len(blinky_path) == 0:
                    if blinky_x < x and y == blinky_y:
                        blinky_speed_x = blinky_speed_right
                        blinky_speed_y = 0
                        destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                    elif blinky_x > x and y == blinky_y:
                        blinky_speed_x = blinky_speed_left
                        blinky_speed_y = 0
                        destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                    elif blinky_y < y and x == blinky_x:
                        blinky_speed_y = blinky_speed_down
                        blinky_speed_x = 0
                        destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                    elif blinky_y > y and x == blinky_x:
                        blinky_speed_y = blinky_speed_up
                        blinky_speed_x = 0
                        destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
            if blinky_path:
                destination_node_blinky = blinky_path[0][1]
                destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                if blinky_y == destination_node_blinky_y:
                    if blinky_x > destination_node_blinky_x:
                        blinky_speed_x = blinky_speed_left
                        blinky_speed_y = 0
                        destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                    elif blinky_x < destination_node_blinky_x:
                        blinky_speed_x = blinky_speed_right
                        blinky_speed_y = 0
                        destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                elif blinky_x == destination_node_blinky_x:
                    if blinky_y > destination_node_blinky_y:
                        blinky_speed_y = blinky_speed_up
                        blinky_speed_x = 0
                        destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                    elif blinky_y < destination_node_blinky_y:
                        blinky_speed_y = blinky_speed_down
                        blinky_speed_x = 0
                        destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
            else:
                if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                    blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                    blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                    if x > blinky_x and blinky_ghost_right == True:
                        node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                        if node_graph[node_blinky]["Left"]:
                            start_node_blinky = node_graph[node_blinky]["Left"][0]
                        blinky_speed_x = blinky_speed_right
                        blinky_speed_y = 0
                        destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                    elif x < blinky_x and blinky_ghost_left == True:
                        node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                        if node_graph[node_blinky]["Right"]:
                            start_node_blinky = node_graph[node_blinky]["Right"][0]
                        blinky_speed_x = blinky_speed_left
                        blinky_speed_y = 0
                        destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                    blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                    blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                    if y > blinky_y and blinky_ghost_down == True:
                        node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                        if node_graph[node_blinky]["Up"]:
                            start_node_blinky = node_graph[node_blinky]["Up"][0]
                        blinky_speed_y = blinky_speed_down
                        blinky_speed_x = 0
                        destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                    elif y < blinky_y and blinky_ghost_up == True:
                        node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                        if node_graph[node_blinky]["Down"]:
                            start_node_blinky = node_graph[node_blinky]["Down"][0]
                        blinky_speed_y = blinky_speed_up
                        blinky_speed_x = 0
                        destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                        destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                        destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
        else:
            if y == blinky_y and (blinky_speed_x == blinky_speed_left or blinky_speed_x == blinky_speed_right):
                blinky_ghost_right = ghost_right(node_graph, blinky_x, blinky_y)
                blinky_ghost_left = ghost_left(node_graph, blinky_x, blinky_y)
                if x > blinky_x and blinky_ghost_right == True:
                    node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                    if node_graph[node_blinky]["Left"]:
                        start_node_blinky = node_graph[node_blinky]["Left"][0]
                    blinky_speed_x = blinky_speed_right
                    blinky_speed_y = 0
                    destination_node_blinky = ghost_node_right(node_graph, blinky_x, blinky_y)
                    destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                    destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                elif x < blinky_x and blinky_ghost_left == True:
                    node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                    if node_graph[node_blinky]["Right"]:
                        start_node_blinky = node_graph[node_blinky]["Right"][0]
                    blinky_speed_x = blinky_speed_left
                    blinky_speed_y = 0
                    destination_node_blinky = ghost_node_left(node_graph, blinky_x, blinky_y)
                    destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                    destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
            elif x == blinky_x and (blinky_speed_y == blinky_speed_down or blinky_speed_y == blinky_speed_up):
                blinky_ghost_down = ghost_down(node_graph, blinky_x, blinky_y)
                blinky_ghost_up = ghost_up(node_graph, blinky_x, blinky_y)
                if y > blinky_y and blinky_ghost_down == True:
                    node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                    if node_graph[node_blinky]["Up"]:
                        start_node_blinky = node_graph[node_blinky]["Up"][0]
                    blinky_speed_y = blinky_speed_down
                    blinky_speed_x = 0
                    destination_node_blinky = ghost_node_down(node_graph, blinky_x, blinky_y)
                    destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                    destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
                elif y < blinky_y and blinky_ghost_up == True:
                    node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                    if node_graph[node_blinky]["Down"]:
                        start_node_blinky = node_graph[node_blinky]["Down"][0]
                    blinky_speed_y = blinky_speed_up
                    blinky_speed_x = 0
                    destination_node_blinky = ghost_node_up(node_graph, blinky_x, blinky_y)
                    destination_node_blinky_x = node_graph[destination_node_blinky]["(x, y)"][0]
                    destination_node_blinky_y = node_graph[destination_node_blinky]["(x, y)"][1]
        gameDisplay.fill(black)  # fills color
        plot_positions(node_graph, maze, wall_node_graph, pellets_eaten, x, y)
        pacman(x, y, file)
        a, b = x, y
        blinky(node_graph, (x, y), start_node_blinky)
        blinky_draw(blinky_x, blinky_y)
        clyde_draw(clyde_x, clyde_y)
        pygame.display.update()  # Updates the screen
        clock.tick(60)  # controls fps

def node_exist_down(node_graph, x, y):
    end_node_y = y
    for i in node_graph:
        if node_graph[i]["Down"]:
            if x in node_graph[i]["(x, y)"] and y in node_graph[i]["(x, y)"]:
                node = node_graph[i]["Down"][0]
                end_node_y = node_graph[node]["(x, y)"][1]
                while True:
                    if node_graph[node]["Down"]:
                        node = node_graph[node]["Down"][0]
                        end_node_y = node_graph[node]["(x, y)"][1]
                    else:
                        break
        if end_node_y != y:
            break
    return end_node_y

def node_exist_up(node_graph, x, y):
    end_node_y = y
    for i in node_graph:
        if node_graph[i]["Up"]:
            if x in node_graph[i]["(x, y)"] and y in node_graph[i]["(x, y)"]:
                node = node_graph[i]["Up"][0]
                end_node_y = node_graph[node]["(x, y)"][1]
                while True:
                    if node_graph[node]["Up"]:
                        node = node_graph[node]["Up"][0]
                        end_node_y = node_graph[node]["(x, y)"][1]
                    else:
                        break
        if end_node_y != y:
            break
    return end_node_y

def node_exist_right(node_graph, x, y):
    end_node_x = x
    for i in node_graph:
        if node_graph[i]["Right"]:
            if x in node_graph[i]["(x, y)"] and y in node_graph[i]["(x, y)"]:
                node = node_graph[i]["Right"][0]
                end_node_x = node_graph[node]["(x, y)"][0]
                while True:
                    if node_graph[node]["Right"]:
                        node = node_graph[node]["Right"][0]
                        end_node_x = node_graph[node]["(x, y)"][0]
                    else:
                        break
        if end_node_x != x:
            break
    return end_node_x

def node_exist_left(node_graph, x, y):
    end_node_x = x
    for i in node_graph:
        if node_graph[i]["Left"]:
            if x in node_graph[i]["(x, y)"] and y in node_graph[i]["(x, y)"]:
                node = node_graph[i]["Left"][0]
                end_node_x = node_graph[node]["(x, y)"][0]
                while True:
                    if node_graph[node]["Left"]:
                        node = node_graph[node]["Left"][0]
                        end_node_x = node_graph[node]["(x, y)"][0]
                    else:
                        break
        if end_node_x != x:
            break
    return end_node_x

def plot_positions(node_graph, maze, wall_node_graph, pellets_eaten, x, y):
    #pygame.draw.circle(gameDisplay, red, (node_graph["+ 5"]["(x, y)"][0], node_graph["+ 5"]["(x, y)"][1]), 10)
    for i in node_graph:
        for j in node_graph[i]:
            coordinates_start = node_graph[i]["(x, y)"]
            pygame.draw.circle(gameDisplay, red, (coordinates_start[0], coordinates_start[1]), 10)
            if j != "(x, y)" and node_graph[i][j]:
                node = node_graph[i][j][0]
                coordinates_end = node_graph[node]["(x, y)"]
                #pygame.draw.line(gameDisplay, white, (coordinates_start[0], coordinates_start[1]), (coordinates_end[0], coordinates_end[1]))
    for i in wall_node_graph:
        for j in wall_node_graph[i]:
            coordinates_start = wall_node_graph[i]["(x, y)"]
            if len(wall_node_graph[i][j]) == 1:
                node = wall_node_graph[i][j][0]
                coordinates_end = wall_node_graph[node]["(x, y)"]
                pygame.draw.line(gameDisplay, green, (coordinates_start[0], coordinates_start[1]), (coordinates_end[0], coordinates_end[1]))
    for i in maze:
        for j in i:
            if j[0] == "p":
                pellet_coordinate = [j[1], j[2]]
                if pellet_coordinate in pellets_eaten:
                    continue
                else:
                    pygame.draw.circle(gameDisplay, Yellow, (j[1], j[2]), 5)
                    if x == j[1] and y == j[2]:
                        pellets_eaten.append(pellet_coordinate)
                        #pygame.mixer.music.load('pacman_chomp.wav')
                        #pygame.mixer.music.play(1)


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

def blinky(node_graph, to, start_node_blinky):
    for i in node_graph:
        if to[0] in node_graph[i]["(x, y)"] and to[1] in node_graph[i]["(x, y)"]:
            destination = i
    lst = getShortestPath1(node_graph, start_node_blinky, destination)
    for i in lst:
        coordinate_start = node_graph[i[0]]["(x, y)"]
        coordinate_end = node_graph[i[1]]["(x, y)"]
        pygame.draw.line(gameDisplay, red, (coordinate_start[0], coordinate_start[1]), (coordinate_end[0], coordinate_end[1]))
    return lst


def clyde(node_graph, to, start_node_clyde):
    for i in node_graph:
        if to[0] in node_graph[i]["(x, y)"] and to[1] in node_graph[i]["(x, y)"]:
            destination = i
    lst = getShortestPath1(node_graph, start_node_clyde, destination)
    for i in lst:
        coordinate_start = node_graph[i[0]]["(x, y)"]
        coordinate_end = node_graph[i[1]]["(x, y)"]
        pygame.draw.line(gameDisplay, yellow, (coordinate_start[0], coordinate_start[1]),
                         (coordinate_end[0], coordinate_end[1]))
    return lst

def ghost_node_check_right(node_graph, x, y):
    Min = math.inf
    for i in node_graph:
        if y in node_graph[i]["(x, y)"]:
            if node_graph[i]["(x, y)"][0] - x < Min and node_graph[i]["(x, y)"][0] - x > 0:
                Min = node_graph[i]["(x, y)"][0] - x
                a = node_graph[i]["(x, y)"][0]
                b = node_graph[i]["(x, y)"][1]
    return a, b

def ghost_node_check_left(node_graph, x, y):
    Min = math.inf
    for i in node_graph:
        if y in node_graph[i]["(x, y)"]:
            if x - node_graph[i]["(x, y)"][0] < Min and x - node_graph[i]["(x, y)"][0] > 0:
                Min = x - node_graph[i]["(x, y)"][0]
                a = node_graph[i]["(x, y)"][0]
                b = node_graph[i]["(x, y)"][1]
    return a, b

def ghost_node_check_down(node_graph, x, y):
    Min = math.inf
    for i in node_graph:
        if x in node_graph[i]["(x, y)"]:
            if node_graph[i]["(x, y)"][1] - y < Min and node_graph[i]["(x, y)"][1] - y > 0:
                Min = node_graph[i]["(x, y)"][1] - y
                a = node_graph[i]["(x, y)"][0]
                b = node_graph[i]["(x, y)"][1]
    return a, b

def ghost_node_check_up(node_graph, x, y):
    Min = math.inf
    for i in node_graph:
        if x in node_graph[i]["(x, y)"]:
            if y - node_graph[i]["(x, y)"][1] < Min and y - node_graph[i]["(x, y)"][1] > 0:
                Min = y - node_graph[i]["(x, y)"][1]
                a = node_graph[i]["(x, y)"][0]
                b = node_graph[i]["(x, y)"][1]
    return a, b

def ghost_right(node_graph, ghost_x, ghost_y):
    for i in node_graph:
        if ghost_x in node_graph[i]["(x, y)"] and ghost_y in node_graph[i]["(x, y)"]:
            if node_graph[i]["Right"]:
                return True
            else:
                return False
    return True

def ghost_left(node_graph, ghost_x, ghost_y):
    for i in node_graph:
        if ghost_x in node_graph[i]["(x, y)"] and ghost_y in node_graph[i]["(x, y)"]:
            if node_graph[i]["Left"]:
                return True
            else:
                return False
    return True

def ghost_up(node_graph, ghost_x, ghost_y):
    for i in node_graph:
        if ghost_x in node_graph[i]["(x, y)"] and ghost_y in node_graph[i]["(x, y)"]:
            if node_graph[i]["Up"]:
                return True
            else:
                return False
    return True

def ghost_down(node_graph, ghost_x, ghost_y):
    for i in node_graph:
        if ghost_x in node_graph[i]["(x, y)"] and ghost_y in node_graph[i]["(x, y)"]:
            if node_graph[i]["Down"]:
                return True
            else:
                return False
    return True

def ghost_node_right(node_graph, ghost_x, ghost_y):
    Min = math.inf
    for i in node_graph:
        if ghost_y in node_graph[i]["(x, y)"]:
            if node_graph[i]["(x, y)"][0] - ghost_x <= Min and node_graph[i]["(x, y)"][0] - ghost_x > 0:
                Min = node_graph[i]["(x, y)"][0] - ghost_x
                node = i
    return node

def ghost_node_left(node_graph, ghost_x, ghost_y):
    Min = math.inf
    for i in node_graph:
        if ghost_y in node_graph[i]["(x, y)"]:
            if ghost_x - node_graph[i]["(x, y)"][0] <= Min and ghost_x - node_graph[i]["(x, y)"][0] > 0:
                Min = ghost_x - node_graph[i]["(x, y)"][0]
                node = i
    return node

def ghost_node_up(node_graph, ghost_x, ghost_y):
    Min = math.inf
    for i in node_graph:
        if ghost_x in node_graph[i]["(x, y)"]:
            if ghost_y - node_graph[i]["(x, y)"][1] <= Min and ghost_y - node_graph[i]["(x, y)"][1] > 0:
                Min = ghost_y - node_graph[i]["(x, y)"][1]
                node = i
    return node

def ghost_node_down(node_graph, ghost_x, ghost_y):
    Min = math.inf
    for i in node_graph:
        if ghost_x in node_graph[i]["(x, y)"]:
            if node_graph[i]["(x, y)"][1] - ghost_y <= Min and node_graph[i]["(x, y)"][1] - ghost_y > 0:
                Min = node_graph[i]["(x, y)"][1] - ghost_y
                node = i
    return node


x = 140
y = 163

speed = 0.5
speed_right = speed
speed_left = -speed
speed_up = -speed
speed_down = speed

pellets_eaten = []
pacmanImg_width = 25
pacmanImg_height = 25

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
Yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

blinky_picture = pygame.image.load("Blinky.png")
#pygame.mixer.music.load('Tobu & Itro - Sunburst [NCS Release].mp3')
#pygame.mixer.music.play(-1)
wall_node_graph = {'s 0': {'(x, y)': [120, 63], 'Up': [], 'Down': ['s 40'], 'Left': [], 'Right': ['s 1']}, 's 1': {'(x, y)': [380, 63], 'Up': [], 'Down': ['s 16'], 'Left': ['s 0'], 'Right': []}, 's 2': {'(x, y)': [400, 63], 'Up': [], 'Down': ['S 17'], 'Left': [], 'Right': ['s 3']}, 's 3': {'(x, y)': [660, 63], 'Up': [], 'Down': ['s 47'], 'Left': ['s 2'], 'Right': []}, 's 4': {'(x, y)': [160, 103], 'Up': [], 'Down': ['s 12'], 'Left': [], 'Right': ['s 5']}, 's 5': {'(x, y)': [220, 103], 'Up': [], 'Down': ['s 13'], 'Left': ['s 4'], 'Right': []}, 's 6': {'(x, y)': [260, 103], 'Up': [], 'Down': ['s 14'], 'Left': [], 'Right': ['s 7']}, 's 7': {'(x, y)': [340, 103], 'Up': [], 'Down': ['s 15'], 'Left': ['s 6'], 'Right': []}, 's 8': {'(x, y)': [440, 103], 'Up': [], 'Down': ['s 18'], 'Left': [], 'Right': ['s 9']}, 's 9': {'(x, y)': [520, 103], 'Up': [], 'Down': ['s 19'], 'Left': ['s 8'], 'Right': []}, 's 10': {'(x, y)': [560, 103], 'Up': [], 'Down': ['s 20'], 'Left': [], 'Right': ['s 11']}, 's 11': {'(x, y)': [620, 103], 'Up': [], 'Down': ['s 21'], 'Left': ['s 10'], 'Right': []}, 's 12': {'(x, y)': [160, 143], 'Up': ['s 4'], 'Down': [], 'Left': [], 'Right': ['s 13']}, 's 13': {'(x, y)': [220, 143], 'Up': ['s 5'], 'Down': [], 'Left': ['s 12'], 'Right': []}, 's 14': {'(x, y)': [260, 143], 'Up': ['s 6'], 'Down': [], 'Left': [], 'Right': ['s 15']}, 's 15': {'(x, y)': [340, 143], 'Up': ['s 7'], 'Down': [], 'Left': ['s 14'], 'Right': []}, 's 16': {'(x, y)': [380, 143], 'Up': ['s 1'], 'Down': [], 'Left': [], 'Right': ['S 17']}, 'S 17': {'(x, y)': [400, 143], 'Up': ['s 2'], 'Down': [], 'Left': ['s 16'], 'Right': []}, 's 18': {'(x, y)': [440, 143], 'Up': ['s 8'], 'Down': [], 'Left': [], 'Right': ['s 19']}, 's 19': {'(x, y)': [520, 143], 'Up': ['s 9'], 'Down': [], 'Left': ['s 18'], 'Right': []}, 's 20': {'(x, y)': [560, 143], 'Up': ['s 10'], 'Down': [], 'Left': [], 'Right': ['s 21']}, 's 21': {'(x, y)': [620, 143], 'Up': ['s 11'], 'Down': [], 'Left': ['s 20'], 'Right': []}, 's 22': {'(x, y)': [160, 183], 'Up': [], 'Down': ['S 32'], 'Left': [], 'Right': ['s 23']}, 's 23': {'(x, y)': [220, 183], 'Up': [], 'Down': ['S 33'], 'Left': ['s 22'], 'Right': []}, 's 24': {'(x, y)': [260, 183], 'Up': [], 'Down': ['s 60'], 'Left': [], 'Right': ['S 25']}, 'S 25': {'(x, y)': [280, 183], 'Up': [], 'Down': ['s 42'], 'Left': ['s 24'], 'Right': []}, 's 26': {'(x, y)': [320, 183], 'Up': [], 'Down': ['S 34'], 'Left': [], 'Right': ['s 27']}, 's 27': {'(x, y)': [460, 183], 'Up': [], 'Down': ['S 37'], 'Left': ['s 26'], 'Right': []}, 's 28': {'(x, y)': [500, 183], 'Up': [], 'Down': ['s 45'], 'Left': [], 'Right': ['S 29']}, 'S 29': {'(x, y)': [520, 183], 'Up': [], 'Down': ['S 63'], 'Left': ['s 28'], 'Right': []}, 's 30': {'(x, y)': [560, 183], 'Up': [], 'Down': ['S 38'], 'Left': [], 'Right': ['s 31']}, 's 31': {'(x, y)': [620, 183], 'Up': [], 'Down': ['S 39'], 'Left': ['s 30'], 'Right': []}, 'S 32': {'(x, y)': [160, 203], 'Up': ['s 22'], 'Down': [], 'Left': [], 'Right': ['S 33']}, 'S 33': {'(x, y)': [220, 203], 'Up': ['s 23'], 'Down': [], 'Left': ['S 32'], 'Right': []}, 'S 34': {'(x, y)': [320, 203], 'Up': ['s 26'], 'Down': [], 'Left': [], 'Right': ['s 35']}, 's 35': {'(x, y)': [380, 203], 'Up': [], 'Down': ['s 50'], 'Left': ['S 34'], 'Right': []}, 's 36': {'(x, y)': [400, 203], 'Up': [], 'Down': ['S 51'], 'Left': [], 'Right': ['S 37']}, 'S 37': {'(x, y)': [460, 203], 'Up': ['s 27'], 'Down': [], 'Left': ['s 36'], 'Right': []}, 'S 38': {'(x, y)': [560, 203], 'Up': ['s 30'], 'Down': [], 'Left': [], 'Right': ['S 39']}, 'S 39': {'(x, y)': [620, 203], 'Up': ['s 31'], 'Down': [], 'Left': ['S 38'], 'Right': []}, 's 40': {'(x, y)': [120, 243], 'Up': ['s 0'], 'Down': [], 'Left': [], 'Right': ['s 41']}, 's 41': {'(x, y)': [220, 243], 'Up': [], 'Down': ['s 59'], 'Left': ['s 40'], 'Right': []}, 's 42': {'(x, y)': [280, 243], 'Up': ['S 25'], 'Down': [], 'Left': [], 'Right': ['s 43']}, 's 43': {'(x, y)': [340, 243], 'Up': [], 'Down': ['S 49'], 'Left': ['s 42'], 'Right': []}, 's 44': {'(x, y)': [440, 243], 'Up': [], 'Down': ['S 52'], 'Left': [], 'Right': ['s 45']}, 's 45': {'(x, y)': [500, 243], 'Up': ['s 28'], 'Down': [], 'Left': ['s 44'], 'Right': []}, 's 46': {'(x, y)': [560, 243], 'Up': [], 'Down': ['s 64'], 'Left': [], 'Right': ['s 47']}, 's 47': {'(x, y)': [660, 243], 'Up': ['s 3'], 'Down': [], 'Left': ['s 46'], 'Right': []}, 's 48': {'(x, y)': [280, 263], 'Up': [], 'Down': ['S 61'], 'Left': [], 'Right': ['S 49']}, 'S 49': {'(x, y)': [340, 263], 'Up': ['s 43'], 'Down': [], 'Left': ['s 48'], 'Right': []}, 's 50': {'(x, y)': [380, 263], 'Up': ['s 35'], 'Down': [], 'Left': [], 'Right': ['S 51']}, 'S 51': {'(x, y)': [400, 263], 'Up': ['s 36'], 'Down': [], 'Left': ['s 50'], 'Right': []}, 'S 52': {'(x, y)': [440, 263], 'Up': ['s 44'], 'Down': [], 'Left': [], 'Right': ['s 53']}, 's 53': {'(x, y)': [500, 263], 'Up': [], 'Down': ['s 62'], 'Left': ['S 52'], 'Right': []}, 's 54': {'(x, y)': [320, 303], 'Up': [], 'Down': ['s 74'], 'Left': [], 'Right': ['s 55']}, 's 55': {'(x, y)': [360, 303], 'Up': [], 'Down': [], 'Left': ['s 54'], 'Right': []}, 's 56': {'(x, y)': [420, 303], 'Up': [], 'Down': [], 'Left': [], 'Right': ['s 57']}, 's 57': {'(x, y)': [460, 303], 'Up': [], 'Down': ['s 75'], 'Left': ['s 56'], 'Right': []}, 's 58': {'(x, y)': [120, 323], 'Up': [], 'Down': ['s 66'], 'Left': [], 'Right': ['s 59']}, 's 59': {'(x, y)': [220, 323], 'Up': ['s 41'], 'Down': [], 'Left': ['s 58'], 'Right': []}, 's 60': {'(x, y)': [260, 323], 'Up': ['s 24'], 'Down': [], 'Left': [], 'Right': ['S 61']}, 'S 61': {'(x, y)': [280, 323], 'Up': ['s 48'], 'Down': [], 'Left': ['s 60'], 'Right': []}, 's 62': {'(x, y)': [500, 323], 'Up': ['s 53'], 'Down': [], 'Left': [], 'Right': ['S 63']}, 'S 63': {'(x, y)': [520, 323], 'Up': ['S 29'], 'Down': [], 'Left': ['s 62'], 'Right': []}, 's 64': {'(x, y)': [560, 323], 'Up': ['s 46'], 'Down': [], 'Left': [], 'Right': ['s 65']}, 's 65': {'(x, y)': [660, 323], 'Up': [], 'Down': ['s 73'], 'Left': ['s 64'], 'Right': []}, 's 66': {'(x, y)': [120, 363], 'Up': ['s 58'], 'Down': [], 'Left': [], 'Right': ['s 67']}, 's 67': {'(x, y)': [220, 363], 'Up': [], 'Down': ['s 79'], 'Left': ['s 66'], 'Right': []}, 's 68': {'(x, y)': [260, 363], 'Up': [], 'Down': ['s 80'], 'Left': [], 'Right': ['S 69']}, 'S 69': {'(x, y)': [280, 363], 'Up': [], 'Down': ['S 81'], 'Left': ['s 68'], 'Right': []}, 's 70': {'(x, y)': [500, 363], 'Up': [], 'Down': ['s 86'], 'Left': [], 'Right': ['S 71']}, 'S 71': {'(x, y)': [520, 363], 'Up': [], 'Down': ['S 87'], 'Left': ['s 70'], 'Right': []}, 's 72': {'(x, y)': [560, 363], 'Up': [], 'Down': ['s 88'], 'Left': [], 'Right': ['s 73']}, 's 73': {'(x, y)': [660, 363], 'Up': ['s 65'], 'Down': [], 'Left': ['s 72'], 'Right': []}, 's 74': {'(x, y)': [320, 383], 'Up': ['s 54'], 'Down': [], 'Left': [], 'Right': ['s 75']}, 's 75': {'(x, y)': [460, 383], 'Up': ['s 57'], 'Down': [], 'Left': ['s 74'], 'Right': []}, 's 76': {'(x, y)': [320, 423], 'Up': [], 'Down': ['S 82'], 'Left': [], 'Right': ['s 77']}, 's 77': {'(x, y)': [460, 423], 'Up': [], 'Down': ['S 85'], 'Left': ['s 76'], 'Right': []}, 's 78': {'(x, y)': [120, 443], 'Up': [], 'Down': ['s 108'], 'Left': [], 'Right': ['s 79']}, 's 79': {'(x, y)': [220, 443], 'Up': ['s 67'], 'Down': [], 'Left': ['s 78'], 'Right': []}, 's 80': {'(x, y)': [260, 443], 'Up': ['s 68'], 'Down': [], 'Left': [], 'Right': ['S 81']}, 'S 81': {'(x, y)': [280, 443], 'Up': ['S 69'], 'Down': [], 'Left': ['s 80'], 'Right': []}, 'S 82': {'(x, y)': [320, 443], 'Up': ['s 76'], 'Down': [], 'Left': [], 'Right': ['s 83']}, 's 83': {'(x, y)': [380, 443], 'Up': [], 'Down': ['s 102'], 'Left': ['S 82'], 'Right': []}, 's 84': {'(x, y)': [400, 443], 'Up': [], 'Down': ['S 103'], 'Left': [], 'Right': ['S 85']}, 'S 85': {'(x, y)': [460, 443], 'Up': ['s 77'], 'Down': [], 'Left': ['s 84'], 'Right': []}, 's 86': {'(x, y)': [500, 443], 'Up': ['s 70'], 'Down': [], 'Left': [], 'Right': ['S 87']}, 'S 87': {'(x, y)': [520, 443], 'Up': ['S 71'], 'Down': [], 'Left': ['s 86'], 'Right': []}, 's 88': {'(x, y)': [560, 443], 'Up': ['s 72'], 'Down': [], 'Left': [], 'Right': ['s 89']}, 's 89': {'(x, y)': [660, 443], 'Up': [], 'Down': ['s 117'], 'Left': ['s 88'], 'Right': []}, 's 90': {'(x, y)': [160, 483], 'Up': [], 'Down': ['S 98'], 'Left': [], 'Right': ['s 91']}, 's 91': {'(x, y)': [220, 483], 'Up': [], 'Down': ['S 121'], 'Left': ['s 90'], 'Right': []}, 's 92': {'(x, y)': [260, 483], 'Up': [], 'Down': ['S 100'], 'Left': [], 'Right': ['s 93']}, 's 93': {'(x, y)': [340, 483], 'Up': [], 'Down': ['S 101'], 'Left': ['s 92'], 'Right': []}, 's 94': {'(x, y)': [440, 483], 'Up': [], 'Down': ['S 104'], 'Left': [], 'Right': ['s 95']}, 's 95': {'(x, y)': [520, 483], 'Up': [], 'Down': ['S 105'], 'Left': ['s 94'], 'Right': []}, 's 96': {'(x, y)': [560, 483], 'Up': [], 'Down': ['s 126'], 'Left': [], 'Right': ['s 97']}, 's 97': {'(x, y)': [620, 483], 'Up': [], 'Down': ['S 107'], 'Left': ['s 96'], 'Right': []}, 'S 98': {'(x, y)': [160, 503], 'Up': ['s 90'], 'Down': [], 'Left': [], 'Right': ['s 99']}, 's 99': {'(x, y)': [200, 503], 'Up': [], 'Down': ['s 120'], 'Left': ['S 98'], 'Right': []}, 'S 100': {'(x, y)': [260, 503], 'Up': ['s 92'], 'Down': [], 'Left': [], 'Right': ['S 101']}, 'S 101': {'(x, y)': [340, 503], 'Up': ['s 93'], 'Down': [], 'Left': ['S 100'], 'Right': []}, 's 102': {'(x, y)': [380, 503], 'Up': ['s 83'], 'Down': [], 'Left': [], 'Right': ['S 103']}, 'S 103': {'(x, y)': [400, 503], 'Up': ['s 84'], 'Down': [], 'Left': ['s 102'], 'Right': []}, 'S 104': {'(x, y)': [440, 503], 'Up': ['s 94'], 'Down': [], 'Left': [], 'Right': ['S 105']}, 'S 105': {'(x, y)': [520, 503], 'Up': ['s 95'], 'Down': [], 'Left': ['S 104'], 'Right': []}, 's 106': {'(x, y)': [580, 503], 'Up': [], 'Down': ['S 127'], 'Left': [], 'Right': ['S 107']}, 'S 107': {'(x, y)': [620, 503], 'Up': ['s 97'], 'Down': [], 'Left': ['s 106'], 'Right': []}, 's 108': {'(x, y)': [120, 543], 'Up': ['s 78'], 'Down': [], 'Left': [], 'Right': ['s 109']}, 's 109': {'(x, y)': [160, 543], 'Up': [], 'Down': ['S 119'], 'Left': ['s 108'], 'Right': []}, 's 110': {'(x, y)': [260, 543], 'Up': [], 'Down': ['s 131'], 'Left': [], 'Right': ['S 111']}, 'S 111': {'(x, y)': [280, 543], 'Up': [], 'Down': ['s 132'], 'Left': ['s 110'], 'Right': []}, 's 112': {'(x, y)': [320, 543], 'Up': [], 'Down': ['S 122'], 'Left': [], 'Right': ['s 113']}, 's 113': {'(x, y)': [460, 543], 'Up': [], 'Down': ['S 125'], 'Left': ['s 112'], 'Right': []}, 's 114': {'(x, y)': [500, 543], 'Up': [], 'Down': ['s 135'], 'Left': [], 'Right': ['S 115']}, 'S 115': {'(x, y)': [520, 543], 'Up': [], 'Down': ['s 136'], 'Left': ['s 114'], 'Right': []}, 's 116': {'(x, y)': [620, 543], 'Up': [], 'Down': ['S 128'], 'Left': [], 'Right': ['s 117']}, 's 117': {'(x, y)': [660, 543], 'Up': ['s 89'], 'Down': [], 'Left': ['s 116'], 'Right': []}, 's 118': {'(x, y)': [120, 563], 'Up': [], 'Down': ['s 144'], 'Left': [], 'Right': ['S 119']}, 'S 119': {'(x, y)': [160, 563], 'Up': ['s 109'], 'Down': [], 'Left': ['s 118'], 'Right': []}, 's 120': {'(x, y)': [200, 563], 'Up': ['s 99'], 'Down': [], 'Left': [], 'Right': ['S 121']}, 'S 121': {'(x, y)': [220, 563], 'Up': ['s 91'], 'Down': [], 'Left': ['s 120'], 'Right': []}, 'S 122': {'(x, y)': [320, 563], 'Up': ['s 112'], 'Down': [], 'Left': [], 'Right': ['s 123']}, 's 123': {'(x, y)': [380, 563], 'Up': [], 'Down': ['s 140'], 'Left': ['S 122'], 'Right': []}, 's 124': {'(x, y)': [400, 563], 'Up': [], 'Down': ['S 141'], 'Left': [], 'Right': ['S 125']}, 'S 125': {'(x, y)': [460, 563], 'Up': ['s 113'], 'Down': [], 'Left': ['s 124'], 'Right': []}, 's 126': {'(x, y)': [560, 563], 'Up': ['s 96'], 'Down': [], 'Left': [], 'Right': ['S 127']}, 'S 127': {'(x, y)': [580, 563], 'Up': ['s 106'], 'Down': [], 'Left': ['s 126'], 'Right': []}, 'S 128': {'(x, y)': [620, 563], 'Up': ['s 116'], 'Down': [], 'Left': [], 'Right': ['s 129']}, 's 129': {'(x, y)': [660, 563], 'Up': [], 'Down': ['s 145'], 'Left': ['S 128'], 'Right': []}, 's 130': {'(x, y)': [160, 603], 'Up': [], 'Down': ['S 138'], 'Left': [], 'Right': ['s 131']}, 's 131': {'(x, y)': [260, 603], 'Up': ['s 110'], 'Down': [], 'Left': ['s 130'], 'Right': []}, 's 132': {'(x, y)': [280, 603], 'Up': ['S 111'], 'Down': [], 'Left': [], 'Right': ['s 133']}, 's 133': {'(x, y)': [340, 603], 'Up': [], 'Down': ['S 139'], 'Left': ['s 132'], 'Right': []}, 's 134': {'(x, y)': [440, 603], 'Up': [], 'Down': ['S 142'], 'Left': [], 'Right': ['s 135']}, 's 135': {'(x, y)': [500, 603], 'Up': ['s 114'], 'Down': [], 'Left': ['s 134'], 'Right': []}, 's 136': {'(x, y)': [520, 603], 'Up': ['S 115'], 'Down': [], 'Left': [], 'Right': ['s 137']}, 's 137': {'(x, y)': [620, 603], 'Up': [], 'Down': ['S 143'], 'Left': ['s 136'], 'Right': []}, 'S 138': {'(x, y)': [160, 623], 'Up': ['s 130'], 'Down': [], 'Left': [], 'Right': ['S 139']}, 'S 139': {'(x, y)': [340, 623], 'Up': ['s 133'], 'Down': [], 'Left': ['S 138'], 'Right': []}, 's 140': {'(x, y)': [380, 623], 'Up': ['s 123'], 'Down': [], 'Left': [], 'Right': ['S 141']}, 'S 141': {'(x, y)': [400, 623], 'Up': ['s 124'], 'Down': [], 'Left': ['s 140'], 'Right': []}, 'S 142': {'(x, y)': [440, 623], 'Up': ['s 134'], 'Down': [], 'Left': [], 'Right': ['S 143']}, 'S 143': {'(x, y)': [620, 623], 'Up': ['s 137'], 'Down': [], 'Left': ['S 142'], 'Right': []}, 's 144': {'(x, y)': [120, 663], 'Up': ['s 118'], 'Down': [], 'Left': [], 'Right': ['s 145']}, 's 145': {'(x, y)': [660, 663], 'Up': ['s 129'], 'Down': [], 'Left': ['s 144'], 'Right': []}}
maze = [[['.', 120, 3], ['.', 140, 3], ['.', 160, 3], ['.', 180, 3], ['.', 200, 3], ['.', 220, 3], ['.', 240, 3], ['.', 260, 3], ['.', 280, 3], ['.', 300, 3], ['.', 320, 3], ['.', 340, 3], ['.', 360, 3], ['.', 380, 3], ['.', 400, 3], ['.', 420, 3], ['.', 440, 3], ['.', 460, 3], ['.', 480, 3], ['.', 500, 3], ['.', 520, 3], ['.', 540, 3], ['.', 560, 3], ['.', 580, 3], ['.', 600, 3], ['.', 620, 3], ['.', 640, 3], ['.', 660, 3]], [['.', 120, 23], ['.', 140, 23], ['.', 160, 23], ['.', 180, 23], ['.', 200, 23], ['.', 220, 23], ['.', 240, 23], ['.', 260, 23], ['.', 280, 23], ['.', 300, 23], ['.', 320, 23], ['.', 340, 23], ['.', 360, 23], ['.', 380, 23], ['.', 400, 23], ['.', 420, 23], ['.', 440, 23], ['.', 460, 23], ['.', 480, 23], ['.', 500, 23], ['.', 520, 23], ['.', 540, 23], ['.', 560, 23], ['.', 580, 23], ['.', 600, 23], ['.', 620, 23], ['.', 640, 23], ['.', 660, 23]], [['.', 120, 43], ['.', 140, 43], ['.', 160, 43], ['.', 180, 43], ['.', 200, 43], ['.', 220, 43], ['.', 240, 43], ['.', 260, 43], ['.', 280, 43], ['.', 300, 43], ['.', 320, 43], ['.', 340, 43], ['.', 360, 43], ['.', 380, 43], ['.', 400, 43], ['.', 420, 43], ['.', 440, 43], ['.', 460, 43], ['.', 480, 43], ['.', 500, 43], ['.', 520, 43], ['.', 540, 43], ['.', 560, 43], ['.', 580, 43], ['.', 600, 43], ['.', 620, 43], ['.', 640, 43], ['.', 660, 43]], [['s 0', 120, 63], ['w', 140, 63], ['w', 160, 63], ['w', 180, 63], ['w', 200, 63], ['w', 220, 63], ['w', 240, 63], ['w', 260, 63], ['w', 280, 63], ['w', 300, 63], ['w', 320, 63], ['w', 340, 63], ['w', 360, 63], ['s 1', 380, 63], ['s 2', 400, 63], ['w', 420, 63], ['w', 440, 63], ['w', 460, 63], ['w', 480, 63], ['w', 500, 63], ['w', 520, 63], ['w', 540, 63], ['w', 560, 63], ['w', 580, 63], ['w', 600, 63], ['w', 620, 63], ['w', 640, 63], ['s 3', 660, 63]], [['w', 120, 83], ['+ 0', 140, 83], ['p', 160, 83], ['p', 180, 83], ['p', 200, 83], ['p', 220, 83], ['+ 1', 240, 83], ['p', 260, 83], ['p', 280, 83], ['p', 300, 83], ['p', 320, 83], ['p', 340, 83], ['+ 2', 360, 83], ['w', 380, 83], ['w', 400, 83], ['+ 3', 420, 83], ['p', 440, 83], ['p', 460, 83], ['p', 480, 83], ['p', 500, 83], ['p', 520, 83], ['+ 4', 540, 83], ['p', 560, 83], ['p', 580, 83], ['p', 600, 83], ['p', 620, 83], ['+ 5', 640, 83], ['w', 660, 83]], [['w', 120, 103], ['p', 140, 103], ['s 4', 160, 103], ['w', 180, 103], ['w', 200, 103], ['s 5', 220, 103], ['p', 240, 103], ['s 6', 260, 103], ['w', 280, 103], ['w', 300, 103], ['w', 320, 103], ['s 7', 340, 103], ['p', 360, 103], ['w', 380, 103], ['w', 400, 103], ['p', 420, 103], ['s 8', 440, 103], ['w', 460, 103], ['w', 480, 103], ['w', 500, 103], ['s 9', 520, 103], ['p', 540, 103], ['s 10', 560, 103], ['w', 580, 103], ['w', 600, 103], ['s 11', 620, 103], ['p', 640, 103], ['w', 660, 103]], [['w', 120, 123], ['p', 140, 123], ['w', 160, 123], ['.', 180, 123], ['.', 200, 123], ['w', 220, 123], ['p', 240, 123], ['w', 260, 123], ['.', 280, 123], ['.', 300, 123], ['.', 320, 123], ['w', 340, 123], ['p', 360, 123], ['w', 380, 123], ['w', 400, 123], ['p', 420, 123], ['w', 440, 123], ['.', 460, 123], ['.', 480, 123], ['.', 500, 123], ['w', 520, 123], ['p', 540, 123], ['w', 560, 123], ['.', 580, 123], ['.', 600, 123], ['w', 620, 123], ['p', 640, 123], ['w', 660, 123]], [['w', 120, 143], ['p', 140, 143], ['s 12', 160, 143], ['w', 180, 143], ['w', 200, 143], ['s 13', 220, 143], ['p', 240, 143], ['s 14', 260, 143], ['w', 280, 143], ['w', 300, 143], ['w', 320, 143], ['s 15', 340, 143], ['p', 360, 143], ['s 16', 380, 143], ['S 17', 400, 143], ['p', 420, 143], ['s 18', 440, 143], ['w', 460, 143], ['w', 480, 143], ['w', 500, 143], ['s 19', 520, 143], ['p', 540, 143], ['s 20', 560, 143], ['w', 580, 143], ['w', 600, 143], ['s 21', 620, 143], ['p', 640, 143], ['w', 660, 143]], [['w', 120, 163], ['+ 6', 140, 163], ['p', 160, 163], ['p', 180, 163], ['p', 200, 163], ['p', 220, 163], ['+ 7', 240, 163], ['p', 260, 163], ['p', 280, 163], ['+ 8', 300, 163], ['p', 320, 163], ['p', 340, 163], ['+ 9', 360, 163], ['p', 380, 163], ['p', 400, 163], ['+ 10', 420, 163], ['p', 440, 163], ['p', 460, 163], ['+ 11', 480, 163], ['p', 500, 163], ['p', 520, 163], ['+ 12', 540, 163], ['p', 560, 163], ['p', 580, 163], ['p', 600, 163], ['p', 620, 163], ['+ 13', 640, 163], ['w', 660, 163]], [['w', 120, 183], ['p', 140, 183], ['s 22', 160, 183], ['w', 180, 183], ['w', 200, 183], ['s 23', 220, 183], ['p', 240, 183], ['s 24', 260, 183], ['S 25', 280, 183], ['.', 300, 183], ['s 26', 320, 183], ['w', 340, 183], ['w', 360, 183], ['w', 380, 183], ['w', 400, 183], ['w', 420, 183], ['w', 440, 183], ['s 27', 460, 183], ['.', 480, 183], ['s 28', 500, 183], ['S 29', 520, 183], ['p', 540, 183], ['s 30', 560, 183], ['w', 580, 183], ['w', 600, 183], ['s 31', 620, 183], ['p', 640, 183], ['w', 660, 183]], [['w', 120, 203], ['p', 140, 203], ['S 32', 160, 203], ['w', 180, 203], ['w', 200, 203], ['S 33', 220, 203], ['p', 240, 203], ['w', 260, 203], ['w', 280, 203], ['.', 300, 203], ['S 34', 320, 203], ['w', 340, 203], ['w', 360, 203], ['s 35', 380, 203], ['s 36', 400, 203], ['w', 420, 203], ['w', 440, 203], ['S 37', 460, 203], ['.', 480, 203], ['w', 500, 203], ['w', 520, 203], ['p', 540, 203], ['S 38', 560, 203], ['w', 580, 203], ['w', 600, 203], ['S 39', 620, 203], ['p', 640, 203], ['w', 660, 203]], [['w', 120, 223], ['+ 14', 140, 223], ['p', 160, 223], ['p', 180, 223], ['p', 200, 223], ['p', 220, 223], ['+ 15', 240, 223], ['w', 260, 223], ['w', 280, 223], ['+ 16', 300, 223], ['.', 320, 223], ['.', 340, 223], ['+ 17', 360, 223], ['w', 380, 223], ['w', 400, 223], ['+ 18', 420, 223], ['.', 440, 223], ['.', 460, 223], ['+ 19', 480, 223], ['w', 500, 223], ['w', 520, 223], ['+ 20', 540, 223], ['p', 560, 223], ['p', 580, 223], ['p', 600, 223], ['p', 620, 223], ['+ 21', 640, 223], ['w', 660, 223]], [['s 40', 120, 243], ['w', 140, 243], ['w', 160, 243], ['w', 180, 243], ['w', 200, 243], ['s 41', 220, 243], ['p', 240, 243], ['w', 260, 243], ['s 42', 280, 243], ['w', 300, 243], ['w', 320, 243], ['s 43', 340, 243], ['.', 360, 243], ['w', 380, 243], ['w', 400, 243], ['.', 420, 243], ['s 44', 440, 243], ['w', 460, 243], ['w', 480, 243], ['s 45', 500, 243], ['w', 520, 243], ['p', 540, 243], ['s 46', 560, 243], ['w', 580, 243], ['w', 600, 243], ['w', 620, 243], ['w', 640, 243], ['s 47', 660, 243]], [['.', 120, 263], ['.', 140, 263], ['.', 160, 263], ['.', 180, 263], ['.', 200, 263], ['w', 220, 263], ['p', 240, 263], ['w', 260, 263], ['s 48', 280, 263], ['w', 300, 263], ['w', 320, 263], ['S 49', 340, 263], ['.', 360, 263], ['s 50', 380, 263], ['S 51', 400, 263], ['.', 420, 263], ['S 52', 440, 263], ['w', 460, 263], ['w', 480, 263], ['s 53', 500, 263], ['w', 520, 263], ['p', 540, 263], ['w', 560, 263], ['.', 580, 263], ['.', 600, 263], ['.', 620, 263], ['.', 640, 263], ['.', 660, 263]], [['.', 120, 283], ['.', 140, 283], ['.', 160, 283], ['.', 180, 283], ['.', 200, 283], ['w', 220, 283], ['p', 240, 283], ['w', 260, 283], ['w', 280, 283], ['+ 22', 300, 283], ['.', 320, 283], ['.', 340, 283], ['+ 23', 360, 283], ['.', 380, 283], ['.', 400, 283], ['+ 24', 420, 283], ['.', 440, 283], ['.', 460, 283], ['+ 25', 480, 283], ['w', 500, 283], ['w', 520, 283], ['p', 540, 283], ['w', 560, 283], ['.', 580, 283], ['.', 600, 283], ['.', 620, 283], ['.', 640, 283], ['.', 660, 283]], [['.', 120, 303], ['.', 140, 303], ['.', 160, 303], ['.', 180, 303], ['.', 200, 303], ['w', 220, 303], ['p', 240, 303], ['w', 260, 303], ['w', 280, 303], ['.', 300, 303], ['s 54', 320, 303], ['w', 340, 303], ['s 55', 360, 303], ['.', 380, 303], ['.', 400, 303], ['s 56', 420, 303], ['w', 440, 303], ['s 57', 460, 303], ['.', 480, 303], ['w', 500, 303], ['w', 520, 303], ['p', 540, 303], ['w', 560, 303], ['.', 580, 303], ['.', 600, 303], ['.', 620, 303], ['.', 640, 303], ['.', 660, 303]], [['s 58', 120, 323], ['w', 140, 323], ['w', 160, 323], ['w', 180, 323], ['w', 200, 323], ['s 59', 220, 323], ['p', 240, 323], ['s 60', 260, 323], ['S 61', 280, 323], ['.', 300, 323], ['w', 320, 323], ['.', 340, 323], ['.', 360, 323], ['.', 380, 323], ['.', 400, 323], ['.', 420, 323], ['.', 440, 323], ['w', 460, 323], ['.', 480, 323], ['s 62', 500, 323], ['S 63', 520, 323], ['p', 540, 323], ['s 64', 560, 323], ['w', 580, 323], ['w', 600, 323], ['w', 620, 323], ['w', 640, 323], ['s 65', 660, 323]], [['+ 26', 120, 343], ['p', 140, 343], ['p', 160, 343], ['p', 180, 343], ['p', 200, 343], ['p', 220, 343], ['+ 27', 240, 343], ['.', 260, 343], ['.', 280, 343], ['+ 28', 300, 343], ['w', 320, 343], ['.', 340, 343], ['.', 360, 343], ['.', 380, 343], ['.', 400, 343], ['.', 420, 343], ['.', 440, 343], ['w', 460, 343], ['+ 29', 480, 343], ['.', 500, 343], ['.', 520, 343], ['+ 30', 540, 343], ['p', 560, 343], ['p', 580, 343], ['p', 600, 343], ['p', 620, 343], ['p', 640, 343], ['+ 31', 660, 343]], [['s 66', 120, 363], ['w', 140, 363], ['w', 160, 363], ['w', 180, 363], ['w', 200, 363], ['s 67', 220, 363], ['p', 240, 363], ['s 68', 260, 363], ['S 69', 280, 363], ['.', 300, 363], ['w', 320, 363], ['.', 340, 363], ['.', 360, 363], ['.', 380, 363], ['.', 400, 363], ['.', 420, 363], ['.', 440, 363], ['w', 460, 363], ['.', 480, 363], ['s 70', 500, 363], ['S 71', 520, 363], ['p', 540, 363], ['s 72', 560, 363], ['w', 580, 363], ['w', 600, 363], ['w', 620, 363], ['w', 640, 363], ['s 73', 660, 363]], [['.', 120, 383], ['.', 140, 383], ['.', 160, 383], ['.', 180, 383], ['.', 200, 383], ['w', 220, 383], ['p', 240, 383], ['w', 260, 383], ['w', 280, 383], ['.', 300, 383], ['s 74', 320, 383], ['w', 340, 383], ['w', 360, 383], ['w', 380, 383], ['w', 400, 383], ['w', 420, 383], ['w', 440, 383], ['s 75', 460, 383], ['.', 480, 383], ['w', 500, 383], ['w', 520, 383], ['p', 540, 383], ['w', 560, 383], ['.', 580, 383], ['.', 600, 383], ['.', 620, 383], ['.', 640, 383], ['.', 660, 383]], [['.', 120, 403], ['.', 140, 403], ['.', 160, 403], ['.', 180, 403], ['.', 200, 403], ['w', 220, 403], ['p', 240, 403], ['w', 260, 403], ['w', 280, 403], ['+ 32', 300, 403], ['.', 320, 403], ['.', 340, 403], ['.', 360, 403], ['.', 380, 403], ['.', 400, 403], ['.', 420, 403], ['.', 440, 403], ['.', 460, 403], ['+ 33', 480, 403], ['w', 500, 403], ['w', 520, 403], ['p', 540, 403], ['w', 560, 403], ['.', 580, 403], ['.', 600, 403], ['.', 620, 403], ['.', 640, 403], ['.', 660, 403]], [['.', 120, 423], ['.', 140, 423], ['.', 160, 423], ['.', 180, 423], ['.', 200, 423], ['w', 220, 423], ['p', 240, 423], ['w', 260, 423], ['w', 280, 423], ['.', 300, 423], ['s 76', 320, 423], ['w', 340, 423], ['w', 360, 423], ['w', 380, 423], ['w', 400, 423], ['w', 420, 423], ['w', 440, 423], ['s 77', 460, 423], ['.', 480, 423], ['w', 500, 423], ['w', 520, 423], ['p', 540, 423], ['w', 560, 423], ['.', 580, 423], ['.', 600, 423], ['.', 620, 423], ['.', 640, 423], ['.', 660, 423]], [['s 78', 120, 443], ['w', 140, 443], ['w', 160, 443], ['w', 180, 443], ['w', 200, 443], ['s 79', 220, 443], ['p', 240, 443], ['s 80', 260, 443], ['S 81', 280, 443], ['.', 300, 443], ['S 82', 320, 443], ['w', 340, 443], ['w', 360, 443], ['s 83', 380, 443], ['s 84', 400, 443], ['w', 420, 443], ['w', 440, 443], ['S 85', 460, 443], ['.', 480, 443], ['s 86', 500, 443], ['S 87', 520, 443], ['p', 540, 443], ['s 88', 560, 443], ['w', 580, 443], ['w', 600, 443], ['w', 620, 443], ['w', 640, 443], ['s 89', 660, 443]], [['w', 120, 463], ['+ 34', 140, 463], ['p', 160, 463], ['p', 180, 463], ['p', 200, 463], ['p', 220, 463], ['+ 35', 240, 463], ['p', 260, 463], ['p', 280, 463], ['+ 36', 300, 463], ['p', 320, 463], ['p', 340, 463], ['+ 37', 360, 463], ['w', 380, 463], ['w', 400, 463], ['+ 38', 420, 463], ['p', 440, 463], ['p', 460, 463], ['+ 39', 480, 463], ['p', 500, 463], ['p', 520, 463], ['+ 40', 540, 463], ['p', 560, 463], ['p', 580, 463], ['p', 600, 463], ['p', 620, 463], ['+ 41', 640, 463], ['w', 660, 463]], [['w', 120, 483], ['p', 140, 483], ['s 90', 160, 483], ['w', 180, 483], ['w', 200, 483], ['s 91', 220, 483], ['p', 240, 483], ['s 92', 260, 483], ['w', 280, 483], ['w', 300, 483], ['w', 320, 483], ['s 93', 340, 483], ['p', 360, 483], ['w', 380, 483], ['w', 400, 483], ['p', 420, 483], ['s 94', 440, 483], ['w', 460, 483], ['w', 480, 483], ['w', 500, 483], ['s 95', 520, 483], ['p', 540, 483], ['s 96', 560, 483], ['w', 580, 483], ['w', 600, 483], ['s 97', 620, 483], ['p', 640, 483], ['w', 660, 483]], [['w', 120, 503], ['p', 140, 503], ['S 98', 160, 503], ['w', 180, 503], ['s 99', 200, 503], ['w', 220, 503], ['p', 240, 503], ['S 100', 260, 503], ['w', 280, 503], ['w', 300, 503], ['w', 320, 503], ['S 101', 340, 503], ['p', 360, 503], ['s 102', 380, 503], ['S 103', 400, 503], ['p', 420, 503], ['S 104', 440, 503], ['w', 460, 503], ['w', 480, 503], ['w', 500, 503], ['S 105', 520, 503], ['p', 540, 503], ['w', 560, 503], ['s 106', 580, 503], ['w', 600, 503], ['S 107', 620, 503], ['p', 640, 503], ['w', 660, 503]], [['w', 120, 523], ['+ 42', 140, 523], ['p', 160, 523], ['+ 43', 180, 523], ['w', 200, 523], ['w', 220, 523], ['+ 44', 240, 523], ['p', 260, 523], ['p', 280, 523], ['+ 45', 300, 523], ['p', 320, 523], ['p', 340, 523], ['+ 46', 360, 523], ['p', 380, 523], ['p', 400, 523], ['+ 47', 420, 523], ['p', 440, 523], ['p', 460, 523], ['+ 48', 480, 523], ['p', 500, 523], ['p', 520, 523], ['+ 49', 540, 523], ['w', 560, 523], ['w', 580, 523], ['+ 50', 600, 523], ['p', 620, 523], ['+ 51', 640, 523], ['w', 660, 523]], [['s 108', 120, 543], ['w', 140, 543], ['s 109', 160, 543], ['p', 180, 543], ['w', 200, 543], ['w', 220, 543], ['p', 240, 543], ['s 110', 260, 543], ['S 111', 280, 543], ['p', 300, 543], ['s 112', 320, 543], ['w', 340, 543], ['w', 360, 543], ['w', 380, 543], ['w', 400, 543], ['w', 420, 543], ['w', 440, 543], ['s 113', 460, 543], ['p', 480, 543], ['s 114', 500, 543], ['S 115', 520, 543], ['p', 540, 543], ['w', 560, 543], ['w', 580, 543], ['p', 600, 543], ['s 116', 620, 543], ['w', 640, 543], ['s 117', 660, 543]], [['s 118', 120, 563], ['w', 140, 563], ['S 119', 160, 563], ['p', 180, 563], ['s 120', 200, 563], ['S 121', 220, 563], ['p', 240, 563], ['w', 260, 563], ['w', 280, 563], ['p', 300, 563], ['S 122', 320, 563], ['w', 340, 563], ['w', 360, 563], ['s 123', 380, 563], ['s 124', 400, 563], ['w', 420, 563], ['w', 440, 563], ['S 125', 460, 563], ['p', 480, 563], ['w', 500, 563], ['w', 520, 563], ['p', 540, 563], ['s 126', 560, 563], ['S 127', 580, 563], ['p', 600, 563], ['S 128', 620, 563], ['w', 640, 563], ['s 129', 660, 563]], [['w', 120, 583], ['+ 52', 140, 583], ['p', 160, 583], ['+ 53', 180, 583], ['p', 200, 583], ['p', 220, 583], ['+ 54', 240, 583], ['w', 260, 583], ['w', 280, 583], ['+ 55', 300, 583], ['p', 320, 583], ['p', 340, 583], ['+ 56', 360, 583], ['w', 380, 583], ['w', 400, 583], ['+ 57', 420, 583], ['p', 440, 583], ['p', 460, 583], ['+ 58', 480, 583], ['w', 500, 583], ['w', 520, 583], ['+ 59', 540, 583], ['p', 560, 583], ['p', 580, 583], ['+ 60', 600, 583], ['p', 620, 583], ['+ 61', 640, 583], ['w', 660, 583]], [['w', 120, 603], ['p', 140, 603], ['s 130', 160, 603], ['w', 180, 603], ['w', 200, 603], ['w', 220, 603], ['w', 240, 603], ['s 131', 260, 603], ['s 132', 280, 603], ['w', 300, 603], ['w', 320, 603], ['s 133', 340, 603], ['p', 360, 603], ['w', 380, 603], ['w', 400, 603], ['p', 420, 603], ['s 134', 440, 603], ['w', 460, 603], ['w', 480, 603], ['s 135', 500, 603], ['s 136', 520, 603], ['w', 540, 603], ['w', 560, 603], ['w', 580, 603], ['w', 600, 603], ['s 137', 620, 603], ['p', 640, 603], ['w', 660, 603]], [['w', 120, 623], ['p', 140, 623], ['S 138', 160, 623], ['w', 180, 623], ['w', 200, 623], ['w', 220, 623], ['w', 240, 623], ['w', 260, 623], ['w', 280, 623], ['w', 300, 623], ['w', 320, 623], ['S 139', 340, 623], ['p', 360, 623], ['s 140', 380, 623], ['S 141', 400, 623], ['p', 420, 623], ['S 142', 440, 623], ['w', 460, 623], ['w', 480, 623], ['w', 500, 623], ['w', 520, 623], ['w', 540, 623], ['w', 560, 623], ['w', 580, 623], ['w', 600, 623], ['S 143', 620, 623], ['p', 640, 623], ['w', 660, 623]], [['w', 120, 643], ['+ 62', 140, 643], ['p', 160, 643], ['p', 180, 643], ['p', 200, 643], ['p', 220, 643], ['p', 240, 643], ['p', 260, 643], ['p', 280, 643], ['p', 300, 643], ['p', 320, 643], ['p', 340, 643], ['+ 63', 360, 643], ['p', 380, 643], ['p', 400, 643], ['+ 64', 420, 643], ['p', 440, 643], ['p', 460, 643], ['p', 480, 643], ['p', 500, 643], ['p', 520, 643], ['p', 540, 643], ['p', 560, 643], ['p', 580, 643], ['p', 600, 643], ['p', 620, 643], ['+ 65', 640, 643], ['w', 660, 643]], [['s 144', 120, 663], ['w', 140, 663], ['w', 160, 663], ['w', 180, 663], ['w', 200, 663], ['w', 220, 663], ['w', 240, 663], ['w', 260, 663], ['w', 280, 663], ['w', 300, 663], ['w', 320, 663], ['w', 340, 663], ['w', 360, 663], ['w', 380, 663], ['w', 400, 663], ['w', 420, 663], ['w', 440, 663], ['w', 460, 663], ['w', 480, 663], ['w', 500, 663], ['w', 520, 663], ['w', 540, 663], ['w', 560, 663], ['w', 580, 663], ['w', 600, 663], ['w', 620, 663], ['w', 640, 663], ['s 145', 660, 663]], [['.', 120, 683], ['.', 140, 683], ['.', 160, 683], ['.', 180, 683], ['.', 200, 683], ['.', 220, 683], ['.', 240, 683], ['.', 260, 683], ['.', 280, 683], ['.', 300, 683], ['.', 320, 683], ['.', 340, 683], ['.', 360, 683], ['.', 380, 683], ['.', 400, 683], ['.', 420, 683], ['.', 440, 683], ['.', 460, 683], ['.', 480, 683], ['.', 500, 683], ['.', 520, 683], ['.', 540, 683], ['.', 560, 683], ['.', 580, 683], ['.', 600, 683], ['.', 620, 683], ['.', 640, 683], ['.', 660, 683]], [['.', 120, 703], ['.', 140, 703], ['.', 160, 703], ['.', 180, 703], ['.', 200, 703], ['.', 220, 703], ['.', 240, 703], ['.', 260, 703], ['.', 280, 703], ['.', 300, 703], ['.', 320, 703], ['.', 340, 703], ['.', 360, 703], ['.', 380, 703], ['.', 400, 703], ['.', 420, 703], ['.', 440, 703], ['.', 460, 703], ['.', 480, 703], ['.', 500, 703], ['.', 520, 703], ['.', 540, 703], ['.', 560, 703], ['.', 580, 703], ['.', 600, 703], ['.', 620, 703], ['.', 640, 703], ['.', 660, 703]]]
node_graph = {'+ 0': {'(x, y)': [140, 83], 'Up': [], 'Down': ['+ 6', 80.0], 'Left': [], 'Right': ['+ 1', 100.0]}, '+ 1': {'(x, y)': [240, 83], 'Up': [], 'Down': ['+ 7', 80.0], 'Left': ['+ 0', 100.0], 'Right': ['+ 2', 120.0]}, '+ 2': {'(x, y)': [360, 83], 'Up': [], 'Down': ['+ 9', 80.0], 'Left': ['+ 1', 120.0], 'Right': []}, '+ 3': {'(x, y)': [420, 83], 'Up': [], 'Down': ['+ 10', 80.0], 'Left': [], 'Right': ['+ 4', 120.0]}, '+ 4': {'(x, y)': [540, 83], 'Up': [], 'Down': ['+ 12', 80.0], 'Left': ['+ 3', 120.0], 'Right': ['+ 5', 100.0]}, '+ 5': {'(x, y)': [640, 83], 'Up': [], 'Down': ['+ 13', 80.0], 'Left': ['+ 4', 100.0], 'Right': []}, '+ 6': {'(x, y)': [140, 163], 'Up': ['+ 0', 80.0], 'Down': ['+ 14', 60.0], 'Left': [], 'Right': ['+ 7', 100.0]}, '+ 7': {'(x, y)': [240, 163], 'Up': ['+ 1', 80.0], 'Down': ['+ 15', 60.0], 'Left': ['+ 6', 100.0], 'Right': ['+ 8', 60.0]}, '+ 8': {'(x, y)': [300, 163], 'Up': [], 'Down': ['+ 16', 60.0], 'Left': ['+ 7', 60.0], 'Right': ['+ 9', 60.0]}, '+ 9': {'(x, y)': [360, 163], 'Up': ['+ 2', 80.0], 'Down': [], 'Left': ['+ 8', 60.0], 'Right': ['+ 10', 60.0]}, '+ 10': {'(x, y)': [420, 163], 'Up': ['+ 3', 80.0], 'Down': [], 'Left': ['+ 9', 60.0], 'Right': ['+ 11', 60.0]}, '+ 11': {'(x, y)': [480, 163], 'Up': [], 'Down': ['+ 19', 60.0], 'Left': ['+ 10', 60.0], 'Right': ['+ 12', 60.0]}, '+ 12': {'(x, y)': [540, 163], 'Up': ['+ 4', 80.0], 'Down': ['+ 20', 60.0], 'Left': ['+ 11', 60.0], 'Right': ['+ 13', 100.0]}, '+ 13': {'(x, y)': [640, 163], 'Up': ['+ 5', 80.0], 'Down': ['+ 21', 60.0], 'Left': ['+ 12', 100.0], 'Right': []}, '+ 14': {'(x, y)': [140, 223], 'Up': ['+ 6', 60.0], 'Down': [], 'Left': [], 'Right': ['+ 15', 100.0]}, '+ 15': {'(x, y)': [240, 223], 'Up': ['+ 7', 60.0], 'Down': ['+ 27', 120.0], 'Left': ['+ 14', 100.0], 'Right': []}, '+ 16': {'(x, y)': [300, 223], 'Up': ['+ 8', 60.0], 'Down': [], 'Left': [], 'Right': ['+ 17', 60.0]}, '+ 17': {'(x, y)': [360, 223], 'Up': [], 'Down': ['+ 23', 60.0], 'Left': ['+ 16', 60.0], 'Right': []}, '+ 18': {'(x, y)': [420, 223], 'Up': [], 'Down': ['+ 24', 60.0], 'Left': [], 'Right': ['+ 19', 60.0]}, '+ 19': {'(x, y)': [480, 223], 'Up': ['+ 11', 60.0], 'Down': [], 'Left': ['+ 18', 60.0], 'Right': []}, '+ 20': {'(x, y)': [540, 223], 'Up': ['+ 12', 60.0], 'Down': ['+ 30', 120.0], 'Left': [], 'Right': ['+ 21', 100.0]}, '+ 21': {'(x, y)': [640, 223], 'Up': ['+ 13', 60.0], 'Down': [], 'Left': ['+ 20', 100.0], 'Right': []}, '+ 22': {'(x, y)': [300, 283], 'Up': [], 'Down': ['+ 28', 60.0], 'Left': [], 'Right': ['+ 23', 60.0]}, '+ 23': {'(x, y)': [360, 283], 'Up': ['+ 17', 60.0], 'Down': [], 'Left': ['+ 22', 60.0], 'Right': ['+ 24', 60.0]}, '+ 24': {'(x, y)': [420, 283], 'Up': ['+ 18', 60.0], 'Down': [], 'Left': ['+ 23', 60.0], 'Right': ['+ 25', 60.0]}, '+ 25': {'(x, y)': [480, 283], 'Up': [], 'Down': ['+ 29', 60.0], 'Left': ['+ 24', 60.0], 'Right': []}, '+ 26': {'(x, y)': [120, 343], 'Up': [], 'Down': [], 'Left': [], 'Right': ['+ 27', 120.0]}, '+ 27': {'(x, y)': [240, 343], 'Up': ['+ 15', 120.0], 'Down': ['+ 35', 120.0], 'Left': ['+ 26', 120.0], 'Right': ['+ 28', 60.0]}, '+ 28': {'(x, y)': [300, 343], 'Up': ['+ 22', 60.0], 'Down': ['+ 32', 60.0], 'Left': ['+ 27', 60.0], 'Right': []}, '+ 29': {'(x, y)': [480, 343], 'Up': ['+ 25', 60.0], 'Down': ['+ 33', 60.0], 'Left': [], 'Right': ['+ 30', 60.0]}, '+ 30': {'(x, y)': [540, 343], 'Up': ['+ 20', 120.0], 'Down': ['+ 40', 120.0], 'Left': ['+ 29', 60.0], 'Right': ['+ 31', 120.0]}, '+ 31': {'(x, y)': [660, 343], 'Up': [], 'Down': [], 'Left': ['+ 30', 120.0], 'Right': []}, '+ 32': {'(x, y)': [300, 403], 'Up': ['+ 28', 60.0], 'Down': ['+ 36', 60.0], 'Left': [], 'Right': ['+ 33', 180.0]}, '+ 33': {'(x, y)': [480, 403], 'Up': ['+ 29', 60.0], 'Down': ['+ 39', 60.0], 'Left': ['+ 32', 180.0], 'Right': []}, '+ 34': {'(x, y)': [140, 463], 'Up': [], 'Down': ['+ 42', 60.0], 'Left': [], 'Right': ['+ 35', 100.0]}, '+ 35': {'(x, y)': [240, 463], 'Up': ['+ 27', 120.0], 'Down': ['+ 44', 60.0], 'Left': ['+ 34', 100.0], 'Right': ['+ 36', 60.0]}, '+ 36': {'(x, y)': [300, 463], 'Up': ['+ 32', 60.0], 'Down': [], 'Left': ['+ 35', 60.0], 'Right': ['+ 37', 60.0]}, '+ 37': {'(x, y)': [360, 463], 'Up': [], 'Down': ['+ 46', 60.0], 'Left': ['+ 36', 60.0], 'Right': []}, '+ 38': {'(x, y)': [420, 463], 'Up': [], 'Down': ['+ 47', 60.0], 'Left': [], 'Right': ['+ 39', 60.0]}, '+ 39': {'(x, y)': [480, 463], 'Up': ['+ 33', 60.0], 'Down': [], 'Left': ['+ 38', 60.0], 'Right': ['+ 40', 60.0]}, '+ 40': {'(x, y)': [540, 463], 'Up': ['+ 30', 120.0], 'Down': ['+ 49', 60.0], 'Left': ['+ 39', 60.0], 'Right': ['+ 41', 100.0]}, '+ 41': {'(x, y)': [640, 463], 'Up': [], 'Down': ['+ 51', 60.0], 'Left': ['+ 40', 100.0], 'Right': []}, '+ 42': {'(x, y)': [140, 523], 'Up': ['+ 34', 60.0], 'Down': [], 'Left': [], 'Right': ['+ 43', 40.0]}, '+ 43': {'(x, y)': [180, 523], 'Up': [], 'Down': ['+ 53', 60.0], 'Left': ['+ 42', 40.0], 'Right': []}, '+ 44': {'(x, y)': [240, 523], 'Up': ['+ 35', 60.0], 'Down': ['+ 54', 60.0], 'Left': [], 'Right': ['+ 45', 60.0]}, '+ 45': {'(x, y)': [300, 523], 'Up': [], 'Down': ['+ 55', 60.0], 'Left': ['+ 44', 60.0], 'Right': ['+ 46', 60.0]}, '+ 46': {'(x, y)': [360, 523], 'Up': ['+ 37', 60.0], 'Down': [], 'Left': ['+ 45', 60.0], 'Right': ['+ 47', 60.0]}, '+ 47': {'(x, y)': [420, 523], 'Up': ['+ 38', 60.0], 'Down': [], 'Left': ['+ 46', 60.0], 'Right': ['+ 48', 60.0]}, '+ 48': {'(x, y)': [480, 523], 'Up': [], 'Down': ['+ 58', 60.0], 'Left': ['+ 47', 60.0], 'Right': ['+ 49', 60.0]}, '+ 49': {'(x, y)': [540, 523], 'Up': ['+ 40', 60.0], 'Down': ['+ 59', 60.0], 'Left': ['+ 48', 60.0], 'Right': []}, '+ 50': {'(x, y)': [600, 523], 'Up': [], 'Down': ['+ 60', 60.0], 'Left': [], 'Right': ['+ 51', 40.0]}, '+ 51': {'(x, y)': [640, 523], 'Up': ['+ 41', 60.0], 'Down': [], 'Left': ['+ 50', 40.0], 'Right': []}, '+ 52': {'(x, y)': [140, 583], 'Up': [], 'Down': ['+ 62', 60.0], 'Left': [], 'Right': ['+ 53', 40.0]}, '+ 53': {'(x, y)': [180, 583], 'Up': ['+ 43', 60.0], 'Down': [], 'Left': ['+ 52', 40.0], 'Right': ['+ 54', 60.0]}, '+ 54': {'(x, y)': [240, 583], 'Up': ['+ 44', 60.0], 'Down': [], 'Left': ['+ 53', 60.0], 'Right': []}, '+ 55': {'(x, y)': [300, 583], 'Up': ['+ 45', 60.0], 'Down': [], 'Left': [], 'Right': ['+ 56', 60.0]}, '+ 56': {'(x, y)': [360, 583], 'Up': [], 'Down': ['+ 63', 60.0], 'Left': ['+ 55', 60.0], 'Right': []}, '+ 57': {'(x, y)': [420, 583], 'Up': [], 'Down': ['+ 64', 60.0], 'Left': [], 'Right': ['+ 58', 60.0]}, '+ 58': {'(x, y)': [480, 583], 'Up': ['+ 48', 60.0], 'Down': [], 'Left': ['+ 57', 60.0], 'Right': []}, '+ 59': {'(x, y)': [540, 583], 'Up': ['+ 49', 60.0], 'Down': [], 'Left': [], 'Right': ['+ 60', 60.0]}, '+ 60': {'(x, y)': [600, 583], 'Up': ['+ 50', 60.0], 'Down': [], 'Left': ['+ 59', 60.0], 'Right': ['+ 61', 40.0]}, '+ 61': {'(x, y)': [640, 583], 'Up': [], 'Down': ['+ 65', 60.0], 'Left': ['+ 60', 40.0], 'Right': []}, '+ 62': {'(x, y)': [140, 643], 'Up': ['+ 52', 60.0], 'Down': [], 'Left': [], 'Right': ['+ 63', 220.0]}, '+ 63': {'(x, y)': [360, 643], 'Up': ['+ 56', 60.0], 'Down': [], 'Left': ['+ 62', 220.0], 'Right': ['+ 64', 60.0]}, '+ 64': {'(x, y)': [420, 643], 'Up': ['+ 57', 60.0], 'Down': [], 'Left': ['+ 63', 60.0], 'Right': ['+ 65', 220.0]}, '+ 65': {'(x, y)': [640, 643], 'Up': ['+ 61', 60.0], 'Down': [], 'Left': ['+ 64', 220.0], 'Right': []}}

Pacman_right = pygame.image.load("pacman 1.png")
Pacman_left = pygame.image.load("pacman left.png")
Pacman_up = pygame.image.load("pacman up.png")
Pacman_down = pygame.image.load("pacman down.png")
file = Pacman_right
blinky_speed_left = -speed
blinky_speed_right = speed
blinky_speed_up = -speed
blinky_speed_down = speed
blinky_x = node_graph["+ 5"]["(x, y)"][0]
blinky_y = node_graph["+ 5"]["(x, y)"][1]
start_node_blinky = "+ 5"
blinky_path = blinky(node_graph, (x, y), start_node_blinky)
blinky_speed_x = 0
blinky_speed_y = 0



clyde_picture = pygame.image.load("Clyde.png")
clyde_picture = pygame.transform.scale(clyde_picture , (25 , 25))
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

main(x, y, node_graph, speed_right, speed_left, speed_up, speed_down, maze, wall_node_graph, Pacman_right, Pacman_left, Pacman_up, Pacman_down, file, blinky_speed_left, blinky_speed_right, blinky_speed_up, blinky_speed_down, blinky_x, blinky_y, start_node_blinky, blinky_path, blinky_speed_x, blinky_speed_y)
pygame.quit()
quit()

