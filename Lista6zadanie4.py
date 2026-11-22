import pandas as pd
import matplotlib.pyplot as plt
# 1 zadanie
df = pd.read_csv("magazyny.csv", encoding="utf-8-sig")
df2 = pd.read_csv("klienci.csv", encoding="utf-8-sig")

# 2 zadanie
df = df[['magazyn' , 'miasto', 'wojewodztwo', 'produkty']]
# print(df.head())

# 3 zadanie
woje = input("Podaj województwo: ")
minpro =  int(input("Podaj minimalną liczbę produktów: "))

# 4 zadanie
wynik = df[(df['wojewodztwo'] == woje) & (df['produkty'] >= minpro)]

# 8 zadanie
if len(wynik) == 0:
    print("Nie znaleziono")

# 5 zadanie    
else:    
    wynik = wynik.sort_values(by='produkty', ascending=False)
    print(wynik[['magazyn', 'miasto', 'produkty']])

    # 6 zadanie
    print('Liczba magazynów:', len(wynik))
    print('Suma produktów:', wynik['produkty'].sum())

  # 7 zadanie
    top5 = wynik.head(5)
    plt.barh(top5['magazyn'], top5['produkty'])
    plt.title('Największe magazyny')
    plt.xlabel('Liczba produktów')
    plt.ylabel('Magazyn')
    plt.show()


