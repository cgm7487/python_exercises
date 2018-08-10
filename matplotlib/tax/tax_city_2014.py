# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('tax_data.csv')
print(df)

df.loc[:,['縣市別', '平均數']].plot(kind='bar', stacked=True, x='縣市別', y='平均數')
plt.show()
