import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib import style

style.use('ggplot')

df = pd.read_csv("..")
df = df.dropna()

highs = df["High"].rolling(window = 14).max()
lows = df["Low"].rolling(window = 14).min()

wills = (highs - df["Close"][0:len(df):1]) / (highs-lows) * -100
        

fig, ax = plt.subplots()
plt.xlabel("Date")
ax.plot(df['Date'], wills, 'purple' ,label = "Williams %R (14)")
plt.axhline(y=-20, linewidth=1, color='green',label ="excessive buying")
plt.axhline(y=-80, linewidth=1, color='red', label = "over-selling")
ax.legend()
plt.show()

