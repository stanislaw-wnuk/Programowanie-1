print("KSIĄŻKA KONTAKTÓW")
print("1.Dodaj Kontakt")
print("2.Wyświetl wszystkie kontakty")
print("3.Wyszukaj kontakt")
print("4.Edytuj kontakt")
print("5.Zakończ Kontakt")
print("0.Zakończ")
książka = {}
while True:
   wybierz = int(input("Wybierz opcję: "))
   if wybierz == 0:
       print("Zakończyłeś Działania")
       break
   if wybierz == 1:
        imie =  input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        telefon = input("podaj telefon: ")
        if telefon in książka:
            print("Kontakt juz istnieje")
        else:
            książka[telefon]=[imie,nazwisko]
            print("dodano")
   elif wybierz == 2:
       if not książka:
           print("Puste")
       else:
           for telefon in książka:
               print(książka[telefon][0],książka[telefon][1],telefon)      
   elif wybierz == 3:
       telefon = input("podaj telefon: ")
       if telefon in książka:
           print(książka[telefon][0],książka[telefon][1], telefon)  
       else:
           print("Brak")
   elif wybierz == 4:
       telefon = input("podaj telefon: ")
       if telefon in książka:
           książka[telefon][0]=input("nowe imie: ")
           książka[telefon][1]=input("nowe nazwisko: ")  
           print("Zmieniono")
       else:
           print("Brak")
   elif wybierz == 5:
       telefon = input("podaj telefon: ")
       if telefon in książka:
           del książka[telefon]
           print("Usunięto")
       else:
           print("Brak")              
                                        