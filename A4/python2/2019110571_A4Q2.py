import math
import matplotlib.pyplot as plt


def threepoints(points):
    point1 = points[0]
    point2 = points[1]
    point3 = points[2]

    distance1 = math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    distance2 = math.sqrt((point1[0] - point3[0]) ** 2 + (point1[1] - point3[1]) ** 2)
    distance3 = math.sqrt((point2[0] - point3[0]) ** 2 + (point2[1] - point3[1]) ** 2)
    dis_list = [distance1, distance2, distance3]
    dis_list.sort()
    if (dis_list[0] + dis_list[1]) == dis_list[2]:
        print('They lie on a straight line.')
    else:
        plt.figure(figsize=(8, 8))
        plt.plot([point1[0], point2[0]], [point1[1], point2[1]])
        plt.plot([point1[0], point3[0]], [point1[1], point3[1]])
        plt.plot([point3[0], point2[0]], [point3[1], point2[1]])
        plt.show()
