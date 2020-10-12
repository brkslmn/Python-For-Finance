import pandas as pd
import datetime
import matplotlib.pyplot as plt
import matplotlib.path as mpath
import matplotlib.patches as mpatches
import numpy as np

df = pd.read_csv("TEKTU.IS.csv")
close = df['Close']

rsi_period = 14 
chg = close.diff(1)

gain = chg.mask(chg<0,0)
loss = chg.mask(chg>0,0)

avg_gain = gain.ewm(com = rsi_period - 1, min_periods = rsi_period).mean()
avg_loss = loss.ewm(com = rsi_period - 1, min_periods = rsi_period).mean()

rs = abs(avg_gain/avg_loss)
rsi = 100-(100/(1+rs))


fig, ax= plt.subplots()

ax.plot(df['Date'], rsi, 'purple', label = "RSI")
plt.axhline(y=70, linewidth=1, color='green')
plt.axhline(y=30, linewidth=1, color='red')
ax.legend()

plt.show()

