import urllib.request as ur
import pandas as pd
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# URL koji sadrži XML datoteku s mjerenjima
url = 'https://iszz.azo.hr/iskzl/rs/podatak/export/xml?postaja=299&polutant=5&tipPodatka=18&vrijemeOd=01.01.2017.&vrijemeDo=31.12.2017'

# Dohvaćanje podataka u XML formatu
airQualityHR = ur.urlopen(url).read()
root = ET.fromstring(airQualityHR)

# Inicijalizacija DataFrame-a
df = pd.DataFrame(columns=('mjerenje', 'vrijeme'))

# Iteriranje kroz XML i pohranjivanje podataka u DataFrame
i = 0
while True:
    try:
        obj = root[i]
    except:
        break

    row = dict(zip(['mjerenje', 'vrijeme'], [obj[0].text, obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df._append(row_s)
    df.mjerenje[i] = float(df.mjerenje[i])
    i = i + 1

if df.empty:
    print("Nema podataka u DataFrame-u.")
else:
  df['mjerenje'] = df['mjerenje'].astype(float)
  df['vrijeme'] = pd.to_datetime(df['vrijeme'], utc=True)

  df['month'] = df['vrijeme'].dt.month
  df['dayOfWeek'] = df['vrijeme'].dt.dayofweek

  df_osijek = df[df['mjerenje'].notna()]
  df_osijek_2017 = df_osijek[(df_osijek['vrijeme'].dt.year == 2017)]
  df_osijek_pm10 = df_osijek_2017[(df_osijek_2017['mjerenje'] > 0)]
  print("Mjerenja dnevne koncentracije PM10 čestica za 2017. godinu u gradu Osijeku:")
  print(df_osijek_pm10)

  top3_dates = df_osijek.sort_values('mjerenje', ascending=False).head(3)['vrijeme']
  print("Tri datuma s najvećom koncentracijom PM10 čestica u Osijeku:")
  print(top3_dates)

  missing_values_monthly = df[df['mjerenje'].isnull()].groupby(df['vrijeme'].dt.month)['mjerenje'].count()
  if missing_values_monthly.empty:
    print("Nema nedostajućih vrijednosti mjerenja PM10 čestica.")
  else:
    missing_values_monthly.plot(kind='bar', rot=0, legend=False)
    plt.xlabel('Mjesec')
    plt.ylabel('Broj nedostajućih vrijednosti')
    plt.title('Broj nedostajućih vrijednosti mjerenja PM10 čestica po mjesecima')
    plt.show()

  winter_month = 1
  summer_month = 8
  winter_df = df[df['vrijeme'].dt.month == winter_month]
  summer_df = df[df['vrijeme'].dt.month == summer_month]
  comparison_df = pd.concat([winter_df, summer_df])

  plt.figure(figsize=(10, 6))
  plt.boxplot([winter_df['mjerenje'], summer_df['mjerenje']], labels=['Zimski mjesec', 'Ljetni mjesec'])
  plt.xlabel('Mjesec')
  plt.ylabel('PM10 koncentracija (µg/m³)')
  plt.title('Usporedba PM10 koncentracije između zimskog i ljetnog mjeseca')
  plt.show()

  weekday_df = df[df['dayOfWeek'] < 5]
  weekend_df = df[df['dayOfWeek'] >= 5]

  plt.figure(figsize=(10, 6))
  plt.hist([weekday_df['mjerenje'], weekend_df['mjerenje']], bins=20, label=['Radni dani', 'Vikend'])
  plt.xlabel('PM10 koncentracija')
  plt.ylabel('Broj uzoraka')
  plt.title('Distribucija PM10 čestica tijekom radnih dana i vikenda')
  plt.legend()
  plt.show()