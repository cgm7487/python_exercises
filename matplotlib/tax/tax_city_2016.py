import matplotlib.pyplot as plt
from tabula import read_pdf

df = read_pdf('105_6-1.pdf')

print(df.loc[2:23,'Unnamed: 0'])
#df.loc[:'連江縣','稅後所得'].drop([0,1]).astype(int).plot(kind='bar')
df.loc[2:23,'稅後所得'].astype(int).plot(kind='pie', labels=df.loc[2:23,'Unnamed: 0'])
plt.show()
