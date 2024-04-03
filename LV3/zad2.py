import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('mtcars.csv')

potrosnja_po_cilindrima = df.groupby('cyl')['mpg'].mean()
potrosnja_po_cilindrima.plot(kind='bar', rot=0)
plt.title('Potrošnja automobila po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Potrošnja (mpg)')
plt.show()

df[df['cyl'].isin([4, 6, 8])].boxplot(column='wt', by='cyl')
plt.title('Težina automobila po broju cilindara')
plt.xlabel('Broj cilindara')
plt.ylabel('Težina (1000 lbs)')
plt.show()

potrosnja_po_mjenjacu = df.groupby('am')['mpg'].mean()
potrosnja_po_mjenjacu.plot(kind='bar', rot=0)
plt.title('Potrošnja automobila po vrsti mjenjača')
plt.xlabel('Vrsta mjenjača (0 - automatski, 1 - ručni)')
plt.ylabel('Potrošnja (mpg)')
plt.xticks(ticks=[0, 1], labels=['Automatski', 'Ručni'])
plt.show()

ubrzanje = df['qsec']
snaga = df['hp']
mjenjac = df['am']
colors = np.where(mjenjac == 1, 'r', 'b')

plt.scatter(snaga, ubrzanje, c=colors)
plt.title('Odnos ubrzanja i snage automobila')
plt.xlabel('Snaga (hp)')
plt.ylabel('Ubrzanje (1/4 mile)')
plt.legend(['Ručni mjenjač', 'Automatski mjenjač'])
plt.show()