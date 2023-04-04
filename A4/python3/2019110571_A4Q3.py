import csv
from plotly.graph_objs import Layout, Bar
from plotly import offline

file_name = './midterm.csv'


def get_grades(file_name):
    mid_term = []
    with open(file_name, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header_row = next(reader)
        for index, value in enumerate(reader):
            mid_term.append(float(value[1]))
    return mid_term


mid_term = get_grades(file_name)

midterm_A = [x for x in mid_term if x >= 90 and x <= 100]
midterm_B = [x for x in mid_term if x >= 80 and x < 90]
midterm_C = [x for x in mid_term if x >= 70 and x < 80]
midterm_D = [x for x in mid_term if x >= 60 and x < 70]
midterm_F = [x for x in mid_term if x < 60]

y = [len(i) for i in [midterm_A, midterm_B, midterm_C, midterm_D, midterm_F]]
x = [1, 2, 3, 4, 5]

data = [Bar(x=x, y=y)]
x_axis_config = {'title': 'class'}
y_axis_config = {'title': 'count'}
my_layout = Layout(title='mid_term grades classification',
                   xaxis=dict(
                       tickmode='array',
                       tickvals=[1, 2, 3, 4, 5],
                       ticktext=['A', 'B', 'C', 'D', 'F']
                   ),
                   yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='myhist.html')
