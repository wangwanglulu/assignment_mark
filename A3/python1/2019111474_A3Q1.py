import random
screen = []

def fff():
    for i in range(3):
        line = []
        for j in range(3):
            if random.random() > 0.7:
                line.append("#")
            else:
                line.append(" ")
        screen.append(line)
    
    for i in range(3):
        for j in range(3):
            print(screen[i][j]+" ",end="")
        print()
    
fff()
