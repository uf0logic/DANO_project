import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def s(d):
    for i in range(2009, 2017):
        for j in range(4):
            k = j - 1
            if k < 0:
                o = i - 1
                k = 3
                if o > 2009:
                    d[i, j] += d[o, k]
            else:
                d[i, j] += d[i, k]

def gen(d):
    d.clear()
    for i in range(2009, 2017):
        for j in range(4):
            d[i, j] = 0

df = pd.read_csv('kickstarter_data.csv', delimiter=',')

genres = ["rpg", "platformer", "shooter", "fighting", "survival", "horror", "strategy", "arcade", "simulator", "mmo", "indie", "action", "quest", "adventure"]
xi, yi = [], []

dg = dict()

for i in genres:
    gen(dg)
    for j in range(len(df)):
        y, m, dy = map(int, df['date'].iloc[j].split('-'))
        ind = m % 4
        dg[y, ind] += 1
s(dg)
for j in dg:
    xi.append(j[0] + j[1] * 1/4)
    k = j[1] - 1
    if k < 0:
        o = j[0] - 1
        k = 3
        j1 = o, k
        if o > 2009:
            if dg[j1]:
                yi.append((dg[j] / dg[j1]) * 100 - 100)
    else:
        j1 = j[0], k
        if dg[j1]:
            yi.append((dg[j] / dg[j1]) * 100 - 100)
                

yi = [0] * abs(len(yi) - len(xi)) + yi

xy = [xi, yi]

    

