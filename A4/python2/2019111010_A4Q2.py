import matplotlib.pyplot as plt
def threepoints(n):
    a=[]
    b=[]
    for i in n:
        a.append(i[0])
        b.append(i[1])
        
    if (b[1]-b[0])*(a[2]-a[1])==(b[2]-b[1])*(a[1]-a[0]):
            print('They lie on a straight line.')
    else:
             X = [a[0], a[1], a[2], a[0]]
             Y = [b[0], b[1], b[2], b[0]]
             plt.plot(X, Y)
             plt.show()
