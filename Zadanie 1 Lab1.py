cena = input("Podaj cenę produktu")
ilość = input("Podaj ilość produktu")
koszt_dostawy = (int(cena) * int(ilość))
if koszt_dostawy > 100:
    wysyłka = 0
else:
    wysyłka = 20
końcowa_kwota = koszt_dostawy + wysyłka
print("Koszt produktu:" + str(koszt_dostawy))
print("Końcowa kwota:" + str(końcowa_kwota))
