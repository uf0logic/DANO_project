import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from generationgenres import xyi, genres
from percentfull import xy

for i in genres:
    ym = xy[1]
    yg = xyi[i][1]
    ya = []
    for j in range (len(ym)):
        ya.append(ym[j] - yg[j])
        
    xi = np.arange(2012.0, 2017.0, 1/4)

    for k in xi:
        plt.axvline(k, 0, 100, ls='--', c='#bdbdbd', linewidth='0.5')
    xi = np.arange(2012.125, 2017.0, 1/4)
    c = []
    for j in ya:
        if j > 0:
            c.append('red')
        elif j == 0:
            c.append('gray')
        else:
            c.append('blue')
    plt.bar(xi, ya[12:], color=c[12:], label=i, width=0.25, edgecolor='white')  
    plt.legend()
    plt.show()
    ya.clear()
    c.clear()
        
