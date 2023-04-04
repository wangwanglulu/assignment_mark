import json
from datetime import datetime
from matplotlib import pyplot as plt
filename = 'data.json'
with open(filename,encoding='utf-8') as f:
    btc_data = json.load(f)
    dates = [];csps = []
for btc_dict in btc_data:
    date = btc_dict[0]
    canteen = btc_dict[1]
    csp = btc_dict[2]
    csps.append(csp)
    current_date = datetime.strptime(btc_dict[0], "%m/%d/%Y")
    order_date = current_date.strftime('%d/%m/%Y')
    dates.append(order_date)
zipped = zip(dates,csps)
dic = {}
for x, y in sorted(zip(dates,csps)):
    z = float(y)
    dic[x] = dic.get(x,0) + z
print(dic)
ndate = []
ncsp = []
for day in dic.keys():
    ndate.append(day)
for money in dic.values():
    ncsp.append(money)
print(ndate)
print(ncsp)
plt.style.use('seaborn')
fig, ax = plt.subplots()
fig.autofmt_xdate()
ax.plot(ndate, ncsp, c='green')
