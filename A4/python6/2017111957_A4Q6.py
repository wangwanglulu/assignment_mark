#I choose row14 an row7 ,to analyze the number of gold Medal which different countries have ever got and rank them.
#I get a historic gold metdal rank.
import csv
filename = 'athlete_events.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    countrys,medals=[],[]
    for row in reader:
        medal = row[14]
        medals.append(medal) 
        country = row[7]
        countrys.append(country)              
    goldcountry = []
    frequencies = []
    for x, y in zip(countrys,medals):
        if y == "Gold":
            goldcountry.append(x)
    dic = {}
    for cont in goldcountry:
        dic[cont] = dic.get(cont,0)+1   
    key = []
    value = []
    x_data = []
    y_data = []
    for cont in dic.keys():
        key.append(cont)
    for unmbers in dic.values():
        value.append(unmbers)
    for x , y in sorted(zip(value,key),reverse=True):
        x_data.append(y)
        y_data.append(x)    
from plotly.graph_objs import Bar, Layout
from plotly import offline
x_values = x_data
data=[Bar(x=x_data,y=y_data)]
x_axis_config={'title': 'Country name'}
y_axis_config={'title': 'Gold got'}
my_layout=Layout(title='Historic gold rank',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')  