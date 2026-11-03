inwestcje = {}
nr = 1
while True: 
    print("\n MOJ BUDRZET")
    print("1.Dodaj Zysk")
    print("2.Dodaj strate")
    print("3.Pokaż Historię")
    print("4.Pokaż stan konta")
    print("5.Podsumowanie finansowe")
    print("6.Wyszukaj operację")
    print("7.Usun operację")
    print("0.Zakończ")
    wybierz = int(input("Co robimy - "))
    if wybierz == 0:
        print("Bez sensu")
        break
    if wybierz == 1:
        rodzaj = input("Opis: ")
        kwota = input("Kwota: ")
        typ = "Dodanie"
        numer = nr
        nr += 1
        inwestycje[numer] = [rodzaj, kwota, typ]
        
    if wybierz == 2:
        rodzaj = input("Opis: ")
        kwota = input("Kwota: ") 
        typ = "Wydatek"
        numer = nr
        nr += 1

    if wybierz == 3: 
        if not inwestycje:
            print("Puste")
                   
        
        