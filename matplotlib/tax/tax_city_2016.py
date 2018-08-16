import matplotlib
import matplotlib.pyplot as plt
from tabula import read_pdf

df = read_pdf('105_6-1.pdf',encoding='big5')


print(df.loc[2:23,'Unnamed: 0'])
#df.loc[:'連江縣','稅後所得'].drop([0,1]).astype(int).plot(kind='bar')
matplotlib.rcParams.update({'font.size': 22})
total = int(df.loc[24,'稅後所得'])
df.loc[2:23,'稅後所得'].astype(int).plot(kind='pie',
                                        autopct=lambda p:'{:.2f}%'.format(p),
                                        labels=df.loc[2:23,'Unnamed: 0'], 
                                        title='105年度綜所稅各縣市申報資料')
plt.show()
