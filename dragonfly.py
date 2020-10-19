import pandas as pd 
import numpy as np 
import plotly.graph_objects as go 
from datetime import datetime
import mplfinance as mpf
import matplotlib.pyplot as plt


df = pd.read_csv('THYAO.IS.csv')

def findDragonFly(data):
    
    flies = []

    for i in range(len(data)):
        if data['Open'].values[i] == data['Close'].values[i] and data['Open'].values[i] == data['High'].values[i]:
            flies.append(i) 
    return flies

print(findDragonFly(df))

def findGravestone(data):
    stones = []

    for i in range(len(data)):
        if data['Open'].values[i] == data['Close'].values[i]:
            stones.append(i)
    return stones



fig, ax = plt.subplots()

ax.plot(df['Date'], df['Close'],marker='^',markerfacecolor='r',markevery=findDragonFly(df),label='dragonfly')
ax.legend()
plt.show()



