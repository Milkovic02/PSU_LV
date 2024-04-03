import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')

print("\nPet automobila s najvećom potrošnjom\n",mtcars.sort_values(by=['mpg']).tail(5))

osam_cilindara=mtcars[mtcars.cyl==8]

print("\nTri automobila s 8 cil i najmanjom potrosnjom\n",osam_cilindara.sort_values(by=['mpg']).head(3))

sest_cilindara=mtcars[mtcars.cyl==6]

print("\nSrednja potrosnja automobila sa 6 cil: ",sest_cilindara['mpg'].mean())

cetri_cilindra_masa2000 = mtcars[(mtcars.cyl==4) & ((mtcars.wt>=2) & (mtcars.wt<=2.2))]
print("\nSrednja potrosnja automobila s 4 cil i masom između 2000 i 2200: ",cetri_cilindra_masa2000['mpg'].mean())

am_hp100 = mtcars[(mtcars.am==1) & (mtcars.hp > 100)]
print("\nBroj automobila s automatskim mj i više od 100hp: ",len(am_hp100))

masa = round(mtcars.wt*1000/0.45359237,2)
print("\nMase svih automobila u KG")
print(masa)