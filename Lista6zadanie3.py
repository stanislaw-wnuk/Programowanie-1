import pandas as pd
import matplotlib.pyplot as plt
# 1 zadanie
df = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
df2 = pd.read_csv("klienci.csv", encoding="utf-8-sig")

# 2 zadanie
magazyny_wybrane = df[['wojewodztwo', 'produkty']].copy()
klienci_wybrane = df2[['wojewodztwo', 'zamowienia']].copy()
# print(magazyny_wybrane.head())
# print(klienci_wybrane.head())

# 3 zadanie
pkt2 = df.groupby('wojewodztwo', as_index=False)['produkty'].sum()
print(pkt2)

# 4 zadanie
pkt3 = df2.groupby('wojewodztwo', as_index=False)['zamowienia'].sum()
print(f"\n{pkt3}")

# 5 zadanie
połączone =  pd.merge(pkt2,pkt3, on="wojewodztwo")
print(f"\n{połączone}")

# 6 zadanie
połączone['roznia'] = połączone['produkty'] - połączone['zamowienia']
print(f"\n{połączone}")

# 7 zadanie
posortowane = połączone.sort_values(by='roznia', ascending=False)
print(f"\n{posortowane[['wojewodztwo', 'roznia']]}")

# 8 zadanie
połączone.plot.bar(
    x='wojewodztwo', 
    y=['produkty', 'zamowienia'], 
    color=['steelblue', 'orange']
)
plt.show()

# 9 zadanie
plt.barh(posortowane['wojewodztwo'].astype(str), posortowane['roznia'], color='green')
plt.show()
