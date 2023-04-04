import csv
filename = 'midterm.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)   
    scores = []
    for row in reader:
        high = float(row[1])
        scores.append(high)
    ranks = []
    for score in scores:
        if score <= 100 and score >=90:
            ranks.append('A')
        if score >=80 and score < 90:
            ranks.append('B')
        if score >= 70 and score < 80:
            ranks.append('C')
        if score < 70 and score >= 60:
            ranks.append('D')
        if score < 60:
            ranks.append('F')
rank = ['A','B','C','D','F']
frequencies = []
for value in rank:
    result = ranks.count(value)
    frequencies.append(result)
print(frequencies)
from plotly.graph_objs import Bar, Layout
from plotly import offline
x_values = rank
data=[Bar(x=x_values,y=frequencies)]
x_axis_config={'title': 'Ranks'}
y_axis_config={'title': 'frequencies'}
my_layout=Layout(title='midterm ranks',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')
