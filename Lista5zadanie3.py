import pandas as pd

df = pd.DataFrame({
    'Produkt': ['Mleko', 'Chleb', 'Masło', 'Jajka', 'Ser'],
    'Cena': [2.5, 3.0, 4.5, 5.0, 6.0],
    'Ilosc': [10, 20, 15, 30, 25]
})

df['Wartosc'] = df['Cena'] * df['Ilosc']

print(pd.DataFrame(df))
print("Powyżej 4 zł: " + str(df['Produkt'][df['Cena'] > 4.0].tolist()))
print("Łączna wartość produktów: " + str(df['Wartosc'].sum()))
print("Średnia cena produktów: " + str(df['Cena'].mean()))


