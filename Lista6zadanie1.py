import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
# 1 zadanie
print(df.head())

# 2 zadanie
magazyny_wybrane = df[['magazyn', 'miasto', 'wojewodztwo', 'produkty']]
print(magazyny_wybrane)

# 3 zadanie
print("Ilość magazynów: " + str(df['magazyn'].count()))

# 4 zadanie 
pkt4 = df[['magazyn','produkty']]
posortowane = pkt4.sort_values(by='produkty', ascending=False)
print(posortowane)

# 5 zadanie
pkt5 = df[['magazyn', 'miasto', 'produkty']]
posortowane2 = pkt5.sort_values(by='produkty', ascending=False)
print(posortowane2.head(5))

# 6 zadanie
suma_produktów = df['produkty'].sum()
print("Suma produktów: " + str(suma_produktów))

# 7 zadanie
pkt7 = df[['magazyn', 'produkty']]
posortowane3 = pkt7.sort_values(by='produkty', ascending=True).head(10)
plt.barh(posortowane3['magazyn'].astype(str), posortowane3['produkty'], color='steelblue')
plt.xlabel('Ilość produktów')
plt.ylabel('Magazyn')
plt.show()
