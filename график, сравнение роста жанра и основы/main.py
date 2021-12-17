import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from generationgenres import xyi, genres
from percentfull import xy


for i in genres:
    c = xy[0]
    d = xy[1]
    plt.plot(c[12:], d[12:], c='#000000', label='main')

    xi = np.arange(2012.0, 2017.0, 1/4)

    for k in xi:
        plt.axvline(k, 0, 100, ls='--', c='#bdbdbd', linewidth='0.5')
    a = xyi[i][0]
    b = xyi[i][1]
    plt.plot(a[12:], b[12:], c='#ff1100', label=i)
    plt.legend()
    plt.show()
