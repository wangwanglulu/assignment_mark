import csv
from plotly.graph_objs import Bar, Layout
from plotly import offline
filename='midterm.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    scores=[]
    for row in reader:
        score=float(row[1])
        scores.append(score)
    print(scores)
a=[]
b=[]
c=[]
d=[]
e=[]
for score in scores:
    if 100>=score>=90:
        a.append(score)
    elif 90>score>=80:
        b.append(score)
    elif 80>score>=70:
        c.append(score)
    elif 70>score>=60:
        d.append(score)
    elif 60>score:
        e.append(score)
x_values=['A','B','C','D','F']
frequencies=[len(a),len(b),len(c),len(d),len(e)]
data=[Bar(x=x_values,y=frequencies)]
x_axis_config={'title': 'level'}
y_axis_config={'title': 'frequencies'}
my_layout=Layout(title='Test Level',xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='midterm.html')
