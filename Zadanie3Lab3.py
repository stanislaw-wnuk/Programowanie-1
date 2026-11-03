książki = {}
nr = 1
while True:
    print("\nBIBLIOTEKA")
    print("1.Dodaj Książkę")
    print("2.Wyświetl wszystkie książki")
    print("3.WYpozycz książkę")
    print("4.Zwróć ksiązkę")
    print("5.Usuń książkę")
    print("0.Zakończ")
    wybierz =  int(input("Wybierz opcję: "))
    if wybierz == 0:
        print("Zakończono")
        break
    elif wybierz == 1:
        autor = input("Podaj Autora: ")
        tytuł = input("Podaj tytuł: ")
        dostępność = True
        numer = nr
        nr += 1
        książki[numer]=[autor,tytuł,dostępność]
        print("Dodano")
    elif wybierz == 2:
         if not książki:
             print("Puste") 
         else:
            for numer in książki:
                print(książki[numer][0],książki[numer][1],numer,książki[numer][2]) 
    elif wybierz == 3:
        numer = int(input("Podaj numer: "))
        if książki[numer][True]:
            książki[numer][2] = False
            print("Wypożyczono")
        else: 
            print("Nie można wypożyczyć") 
    elif wybierz == 4:             
        numer = int(input("Podaj numer: "))
        if książki[numer][False]:
            książki[numer][2] = True
            print("Zwrócono")
        else:
            print("Błąd, książka jest na stanie")
    elif wybierz == 5:
        numer = int(input("Podaj numer: "))
        if numer in książki:
            del książki[numer]
            print("Usunięto")
        else:
            print("Nie ma takiej książki")            


