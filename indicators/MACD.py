import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = pd.read_csv("TEKTU.IS.csv")
df = df.dropna()

closes = df["Close"]

emaresultslow = closes.ewm(span = 26, adjust=False).mean()
emaresultfast = closes.ewm(span = 12, adjust=False).mean()

macdline = emaresultfast - emaresultslow
signalline = macdline.ewm(span = 9, adjust=False).mean()
macdhistogram = macdline - signalline

print(macdhistogram[-1:])


fig, (ax,ax2)= plt.subplots(2,1)


ax.plot(df['Date'], closes, 'r', label = "THY Closes Data")
ax.plot(df['Date'], emaresultslow, 'b', label = "26 Days EMA" )
ax.plot(df['Date'], emaresultfast, 'gold', label = "12 Days EMA")
ax.legend()

ax2.plot(df['Date'], macdline, 'g', label = "MACD Line")
ax2.plot(df['Date'], signalline, 'r', label = "Signal Line")
ax2.fill_between(df['Date'], macdhistogram, 0)
ax2.legend()


plt.show()