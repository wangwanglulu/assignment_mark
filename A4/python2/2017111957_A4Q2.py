import matplotlib.pyplot as plt
n = [[1,1],[2,2],[3,3]]
m = [[1,1],[2,3],[4,2]]
def threepoints(n):
    x1 = n[0][0]
    y1 = n[0][1]
    x2 = n[1][0]
    y2 = n[1][1]
    x3 = n[2][0]
    y3 = n[2][1]     
    a = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    if (a == 0):
        print ("They lie on a straight line.")
    else:
        x_values = [x1,x2]
        y_values = [y1,y2]
        plt.scatter(x_values,y_values,s=1)
        plt.plot(x_values,y_values,color = 'blue')
        x_values = [x2,x3]
        y_values = [y2,y3]
        plt.scatter(x_values,y_values,s=1)
        plt.plot(x_values,y_values,color = 'orange')
        x_values = [x1,x3]
        y_values = [y1,y3]
        plt.scatter(x_values,y_values,s=1)
        plt.plot(x_values,y_values,color = 'green')
        print ("They don't lie on a straight line")  
threepoints(m)
