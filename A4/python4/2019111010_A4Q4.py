import json
from plotly.graph_objs import Bar, Layout
from plotly import offline
filename = 'data.json'
with open(filename,'r',encoding="utf-8") as f_obj:
    information=json.load(f_obj)
canteens=[]
for i in information:
    canteens.append(i[1])
x_values=[]
y_values=[]
for i in canteens:
    if i not in x_values:
        x_values.append(i)
for i in x_values:
    frequency=canteens.count(i)
    y_values.append(frequency)
data=[Bar(x=x_values,y=y_values)]
x_axis_config={'title': 'canteens'}
y_axis_config={'title': 'frequencies'}
my_layout=Layout(title='my visiting to different canteens',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='canteens.html')
