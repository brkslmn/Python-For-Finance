import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')

df = pd.read_csv("..")


intersection = []

def stochastics( dataframe, low, high, close, k, d ):

    df = dataframe.copy()

  
    low_min  = df[low].rolling( window = k ).min()
    high_max = df[high].rolling( window = k ).max()

  
    df['k_fast'] = 100 * (df[close] - low_min)/(high_max - low_min)
    df['d_fast'] = df['k_fast'].rolling(window = d).mean()

  
    df['k_slow'] = df["d_fast"]
    df['d_slow'] = df['k_slow'].rolling(window = d).mean()

    return df


stochs = stochastics(df, 'Low', 'High', 'Close', 14, 3 )
slow_k = stochs['k_slow'].values
fast_k = stochs['k_fast'].values



fig, ax= plt.subplots()
ax.plot(df['Date'], slow_k, 'g')
ax.plot(df['Date'], fast_k, 'b')



plt.show()
