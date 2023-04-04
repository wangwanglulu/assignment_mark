import matplotlib.pyplot as plt
import json
from itertools import groupby
from datetime import datetime
filename = 'data.json'
with open(filename,"r",encoding="utf-8") as f_obj:
    information = json.load(f_obj)
consumptions=[]
dates=[]
for i in information:
    consumptions.append(i[2])
    date=datetime.strptime(i[0], "%m/%d/%Y")
    dates.append(date)
xy_map=[]  
for x, y in groupby(sorted(zip(dates, consumptions)), lambda w: w[0]):
    y_list = []
    for first, second in y:
        y_list.append(float(second))
    xy_map.append([x, sum(y_list)])
X , Y = zip(*xy_map)
input_values =date
plt.plot(X, Y, linewidth=0.5)
plt.xticks(X[::1],rotation=45,fontsize=10)
plt.scatter(X, Y, s=5)
plt.title('每日消费金额',fontsize=10)
plt.tight_layout()
plt.show()
