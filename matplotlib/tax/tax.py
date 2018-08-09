# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tax_data.csv')
print(df)

df.loc[:,['縣市別', '綜合所得總額']].plot(kind='bar', stacked=True, x='縣市別', y='綜合所得總額')
plt.show()