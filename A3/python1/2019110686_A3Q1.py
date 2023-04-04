import random
def fff():
    for i in range(3):
        for j in range(3):
            if random.random() >0.5:
                print('#',end="")
            else :
                print(" ",end=" ")
        print()
fff()
