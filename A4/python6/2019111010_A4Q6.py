#选用第五、第六两列数据并生成BMI指数对运动员身材健康程度进行分析
#得出结论：奥运运动员的BMI呈整体分布，绝大多数在18-24之间，处于健康状态
import csv
from plotly.graph_objs import Bar, Layout
from plotly import offline
filename = ’athlete_events.csv'
with open(filename) as f:
    reader = csv.reader(f) 
    header_row = next(reader)
    BMIs=[]
    for row in reader:
        if row[4]=='NA'or row[5]=='NA':
            pass
        else:
            height=(float(row[4])*0.01)
            weight=float(row[5])
            BMI=(weight/(height**2))//1
            BMIs.append(BMI)
X=[]
Y=[]
for i in BMIs:
    if i not in X:
        X.append(i)
for j in X:
    f=BMIs.count(j)
    Y.append(f)
data=[Bar(x=X,y=Y)]
x_axis_config={'title': 'BMIs'}
y_axis_config={'title': 'frequencies'}
my_layout=Layout(title='BMIs',
xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='athlete BMIs.html')