while True:
    print("\nKALKULATOR")
    print("1.Dodawanie")
    print("2.Odejmowanie")
    print("3.Mnozenie")
    print("4.Dzielenie")
    print("5.Potęgowanie")
    print("6.Średnia")
    print("0.Zakończ") 
    wybierz = int(input("Co chcesz zrobić? - "))
    if wybierz == 0:
        print("Zakończyłeś pomyślnie")
        break
    elif wybierz == 1:
        pl = int(input("Pierwsza liczba: "))
        dl =  int(input("Druga liczba: "))
        w =  pl + dl
        print("Wynik: " + str(pl) + "+" + str(dl) + "=" + str(w))
    elif wybierz == 2:
        pl = int(input("Pierwsza liczba: "))
        dl =  int(input("Druga liczba: "))  
        w = pl - dl  
        print("Wynik: " + str(pl) + "-" + str(dl) + "=" + str(w))
    elif wybierz == 3: 
        pl = int(input("Pierwsza liczba: "))
        dl =  int(input("Druga liczba: "))  
        w = pl * dl  
        print("Wynik: " + str(pl) + "*" + str(dl) + "=" + str(w))
    elif wybierz == 4:    
        pl = int(input("Pierwsza liczba: "))
        dl =  int(input("Druga liczba: ")) 
        if dl == 0:
            print("Nie mozna dzielić przez 0")
        else:    
            w = pl / dl  
            print("Wynik: " + str(pl) + "/" + str(dl) + "=" + str(w))
    elif wybierz == 5:
        pl = int(input("Pierwsza liczba: "))
        dl =  int(input("Druga liczba: "))
        wynik = 1
        for i in range(dl):
           wynik = wynik * pl
        print("Wynik: " + str(pl) + " do potęgi " + str(dl) + "=" + str(wynik))  
    elif wybierz == 6:
        ile = int(input("Ile elementów: "))
        wynik = 0
        for i in range(ile):
            liczba = int(input("Liczba " + str(i+1) + ":"))
            wynik = wynik + liczba
        srednia = wynik/ile
        print("Wynik: " + str(srednia))   

