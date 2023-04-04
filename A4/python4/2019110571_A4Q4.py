import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ds = pd.read_json('./data.json')
ds.columns = ('date', 'place', 'expense')
dd = ds[['place', 'expense']]
aa = dd.groupby('place').count()
plt.figure(figsize=(8,5))
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.xticks(np.arange(len(list(aa.index))), list(aa.index), rotation=45, fontsize=8)
plt.title('Frequency to different canteens')
plt.xlabel('Canteen')
plt.ylabel('Frequency')
plt.tight_layout()
plt.bar(aa.index, list(aa['expense']))
plt.show()
