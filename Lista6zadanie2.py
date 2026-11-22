import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("klienci.csv", encoding="utf-8-sig")
# 1 zadanie
print("Ilość klientów: " + str(df['klient'].count()))

# 2 zadanie
pkt2 = df[['klient', 'miasto', 'wojewodztwo', 'zamowienia']]

# 3 zadanie
posortowane = pkt2.sort_values(by='zamowienia', ascending=False)

# 4 zadanie
print("TOP 5 goatów: ")
pkt4 = posortowane[['klient','miasto', 'zamowienia']]
print(pkt4.head(5))

# 5 zadanie
print("Łączna liczba zamówień: " + str(pkt2['zamowienia'].sum()))

# 6 zadanie
pkt2['udział_klienta'] = pkt2['zamowienia'] / pkt2['zamowienia'].sum() * 100 
print(pkt2)

# 7 zadanie
posortowane2 = pkt2.sort_values(by='zamowienia', ascending=False)
print(posortowane2.head(5))

# 8 zadanie
pkt8 = posortowane2[['klient', 'zamowienia']].head(10)
plt.bar(pkt8['klient'].astype(str), pkt8['zamowienia'])
plt.xlabel("Klient")
plt.ylabel("Ilość zamówień")
plt.show() 

# 9 zadanie
pkt9 = posortowane2['zamowienia'].iloc[:10].sum()
pkt9l = posortowane2['zamowienia'].iloc[10:].sum()
plt.pie([pkt9,pkt9l], labels=["Top 10", "Pozostali"], autopct='%1.1f%%')
plt.show()





