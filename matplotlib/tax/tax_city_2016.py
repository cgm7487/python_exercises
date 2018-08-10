import matplotlib.pyplot as plt
from tabula import read_pdf

df = read_pdf('105_6-1.pdf')
df.loc[:,'稅後所得'].drop([0,1]).astype(int).plot(kind='bar', stacked=True, x=df.iloc[:,0].drop([0,1]))
plt.show()
