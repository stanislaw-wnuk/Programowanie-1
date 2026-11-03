hasło = "hasło"
licznik = 0
while licznik < 3:
    wpisane = input("Podaj hasło: ")
    if wpisane == hasło:
        print("No i klasa")
        break
    else:
        licznik += 1
        print("Niepoprawne hasło. Pozostało prób: ", 3 - licznik)
        if licznik == 3:
            print("No i klops szefie :( ")
            break
