
magazyn = {"Mysz": 5, "Klawiatura": 3, "Monitor": 2}
print("\nMENU MAGAZYNU")
print("1 – Stan magazynu")
print("2 – Przyjęcie towaru")
print("3 – Wydanie towaru")
print("0 – Zakończenie")
while True:
    opcja = input("Wybierz opcję: ")
    if opcja == "0":
        print("Zakończono")
        break
    elif opcja == "1":
        if not magazyn:
            print("Magazyn jest pusty.")
        else:
            for produkt, ilosc in magazyn.items():
                print(f"- {produkt}: {ilosc} szt.")
    elif opcja == "2":
        nazwa = input("Podaj nazwę: ")
        ilosc = int(input("Podaj liczbę przyjętych sztuk: "))
        if nazwa in magazyn:
            magazyn[nazwa] += ilosc
        else:
            magazyn[nazwa] = ilosc
        print("Dodano towar")
    elif opcja == "3":
        nazwa = input("Podaj nazwę: ")
        if nazwa in magazyn:
            ilosc = int(input("Podaj liczbę: "))
            if magazyn[nazwa] >= ilosc:
                magazyn[nazwa] -= ilosc
                print("Wydano")
            else:
                print("Błąd")
        else:
            print("Błąd")


             
