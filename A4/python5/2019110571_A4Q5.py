import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

ds = pd.read_json('./data.json')
ds.columns = ('date', 'place', 'expense')
date_col = list(ds['date'])


def strtime(a):
    b = datetime.strptime(a, "%m/%d/%Y")
    b = b.strftime("%Y-%m-%d")
    return b


date_col = map(strtime, date_col)
ds['date'] = list(date_col)
_ = ds['expense']
ds['expense'] = -_
dd = ds[['date', 'expense']]
aa = dd.groupby('date').sum()
plt.figure(figsize=(8,5))
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.xticks(np.arange(len(list(aa.index))), list(aa.index), rotation=45, fontsize=6)
plt.tight_layout()
plt.title('Daily consumption in April')
plt.xlabel('Date')
plt.ylabel('Consumption')
plt.plot(aa.index, aa['expense'])
plt.show()
