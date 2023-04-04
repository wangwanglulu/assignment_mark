import json
filename = 'data.json'
with open(filename,encoding='utf-8') as f:
    btc_data = json.load(f)
    canteens = []
for btc_dict in btc_data:
    date = btc_dict[0]
    canteen = btc_dict[1]
    csp = btc_dict[2]
    canteens.append(canteen)
frequence = {}
for cant in canteens:
    frequence[cant] = frequence.get(cant,0)+1
cants = []
for place in frequence.keys():
    cants.append(place)
frequences = []
for time in frequence.values():
    frequences.append(time)
from plotly.graph_objs import Bar, Layout
from plotly import offline
x_values = cants
data=[Bar(x=x_values,y=frequences)]
x_axis_config={'title': 'canteens'}
y_axis_config={'title': 'frequences'}
my_layout=Layout(title='March',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')
