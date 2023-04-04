import random

width = 3
height = 3
screen = []


def Init():
    for i in range(height):
        line = []
        for j in range(width):
            if random.random() > 0.8:
                line.append('#')
            else:
                line.append(' ')
        screen.append(line)


def PrintScreen():
    for i in range(height):
        for j in range(width):
            print(screen[i][j] + ' ', end='')
        print()

def fff():
    Init()
    PrintScreen()
    
fff()
