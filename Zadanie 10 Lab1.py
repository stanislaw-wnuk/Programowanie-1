liczba_studentów = input("Podaj liczbę studentów: ")
zaliczone = 0
for i in range(int(liczba_studentów)):
    nazwisko = input("Podaj nazwisko studenta: ")
    ilość = input("Podaj ilość punktów: ")
    if int(ilość) < 50:
        ocena = 2
    elif int(ilość) < 60:
        ocena = 3
    elif int(ilość) < 70:
        ocena = 3.5
    elif int(ilość) < 80:
        ocena = 4
    elif int(ilość) < 90:
        ocena = 4.5
    else:
        ocena = 5

    if(int(ilość) > 100 or int(ilość) < 0):
        print("Nieprawidłowe dane")
    if(int(ilość) >= 50):
        zaliczone += 1    
    else: print("Nazwisko: " + str(nazwisko) + " - " + str(ilość) + " - " + str(ocena))
        
print("Liczba studentów, którzy zaliczyli przedmiot: " + str(zaliczone))

