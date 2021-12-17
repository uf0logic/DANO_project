import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('multiTimeline.csv', delimiter=',', skiprows=2)
xi = []
yi = []

d = dict()

for i in range(2009, 2017):
    for j in range(4):
        d[i, j] = []

for i in range(len(df)):
    y, m = map(int, df['Месяц'].iloc[i].split('-'))
    k = int(df['Kickstarter, Inc.: (По всему миру)'].iloc[i])
    if y >= 2009 and y <= 2016:
        ind = m % 4
        d[y, ind].append(k)

for i in d:
    xi.append(float(i[0]) + 1/4 * i[1])
    yi.append(sum(d[i]) / 3)
    
xy = np.arange(2009.0, 2017.0, 1/4)

for i in xy:
    plt.axvline(i, 0, 100, ls='--', c='#bdbdbd', linewidth='0.5')
    
plt.scatter(xi, yi, c='#000000')
plt.axhline(y=sum(yi)/32, color='red')
plt.xlabel('Кварталы по годам')
plt.ylabel('Соотношение, %')
plt.show()

