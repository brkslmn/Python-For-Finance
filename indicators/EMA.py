import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = pd.read_csv("..")
df = df.dropna()

closes = df["Close"]

emaresultslow = closes.ewm(span = 26, adjust=False).mean()
emaresultfast = closes.ewm(span = 12, adjust=False).mean()

fig, ax= plt.subplots()

plt.xlabel("Date")
ax.plot(df['Date'], closes, 'r')
ax.plot(df['Date'], emaresultslow, 'b', label = "EMA SLOW")
ax.plot(df['Date'], emaresultfast, 'orange', label = "EMA FAST")
ax.legend()



plt.show()

