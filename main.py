import random 
import time
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREY = (46, 49, 49, 1)

Width, Height = 1680, 1050

pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Maze generator")
win = pygame.display.set_mode((Width, Height))
win.fill(WHITE)
pygame.display.update()
Fps = 30
clock = pygame.time.Clock()



cell_width = 40
x = 0
y = 0

grid = [] 
stack_list = []
closed_list = []

path = {}
time.sleep(2)
def build_grid(x, y, cell_width=cell_width):
    for n in range(20):
        x = 40
        y = y + 40
        for m in range(20):
            pygame.draw.line(win, BLACK, [x + cell_width, y], [x + cell_width, y + cell_width], 2) # East wall
            pygame.draw.line(win, BLACK, [x , y], [x, y + cell_width], 2) # West wall
            pygame.draw.line(win, BLACK, [x, y], [x + cell_width, y], 2) # North wall
            pygame.draw.line(win, BLACK, [x, y + cell_width], [x + cell_width, y + cell_width], 2) # South wall

            grid.append((x,y))
            x = x + 40
            pygame.display.update()

def Knockdown_East_Wall(x, y):
    pygame.draw.rect(win, YELLOW, (x + 1, y + 1, 79, 39), 0)
    pygame.display.update()
def Knockdown_West_Wall(x, y):
    pygame.draw.rect(win, YELLOW, (x - cell_width  + 1, y + 1, 79, 39), 0)
    pygame.display.update()
   
def Knockdown_North_Wall(x, y):
    pygame.draw.rect(win, YELLOW, (x + 1, y - cell_width + 1, 39, 79), 0)   
    pygame.display.update()
   
def Knockdown_South_Wall(x, y):
    pygame.draw.rect(win, YELLOW, (x + 1, y + 1, 39, 79), 0)
    pygame.display.update()

def Single_Cell(x, y):
    pygame.draw.rect(win, BLUE, (x + 1, y + 1, 38, 38), 0)
    pygame.display.update()

def backtracking_cell(x, y):
    pygame.draw.rect(win, YELLOW, (x + 1, y+1, 38, 38), 0)
    pygame.display.update()

def Path_tracker(x, y):
    pygame.draw.rect(win, GREEN, (x + 8, y + 8, 10, 10),0)
    pygame.display.update()

def Maze(x, y):
    Single_Cell(x, y)
    stack_list.append((x,y))
    closed_list.append((x,y))
    

    while len(stack_list) > 0:
        time.sleep(0.07)
        cell = []

        if(x + cell_width, y) not in closed_list and (x + cell_width, y) in grid:
            cell.append("East")

        if (x - cell_width, y) not in closed_list and (x - cell_width, y) in grid:
            cell.append("West")

        if (x , y + cell_width) not in closed_list and (x , y + cell_width) in grid:
            cell.append("South")

        if (x, y - cell_width) not in closed_list and (x , y - cell_width) in grid:
            cell.append("North") 

        if len(cell) > 0:
            current_cell = (random.choice(cell))

            if current_cell == "East":
                Knockdown_East_Wall(x,y)
                path[(x + cell_width, y)] = x, y
                x = x + cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "West":
                Knockdown_West_Wall(x, y)
                path[(x - cell_width, y)] = x, y
                x = x - cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "North":
                Knockdown_North_Wall(x, y)
                path[(x , y - cell_width)] = x, y
                y = y - cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

            elif current_cell == "South":
                Knockdown_South_Wall(x, y)
                path[(x , y + cell_width)] = x, y
                y = y + cell_width
                closed_list.append((x, y))
                stack_list.append((x, y))

        else:
            x, y = stack_list.pop()
            Single_Cell(x, y)
            time.sleep(0.05)
            backtracking_cell(x, y)

def path_tracer(x, y):
    Path_tracker(x,y)
    while (x, y) != (40, 40 ):
        x, y = path[x, y]
        Path_tracker(x,y)
        time.sleep(0.1)

x, y = 40, 40
build_grid(40, 0, 40)
Maze(x, y)
path_tracer(400, 400)

RUN = True
while RUN:
    clock.tick(Fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False
