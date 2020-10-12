import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df = pd.read_csv("TEKTU.IS.csv")
df = df.dropna()

closes = df["Close"]

sma = closes.rolling(window=5).mean()

fig, ax = plt.subplots()
ax.plot(df['Date'], closes, 'r')
ax.plot(df['Date'], sma, 'g', label = "SMA")
ax.legend()

plt.show()



    

    