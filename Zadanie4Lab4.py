warsztat_python = []
warsztat_ai = []

while True:
    print("\nMenu: ")
    print("1.Zapisz na Python")
    print("2.Zapisz na AI")
    print("3.Wyświetl uczestników")
    print("4.Uczestnicy obu warsztatów")
    print("5.Unikalni uczestnicy")
    print("0.Zakończ")

    wybór = int(input("Wybierz opcję: "))

    if(wybór == 0):
        print("Zakończono")
        break
    if(wybór == 1):
        imię = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        uczestnik = imię + " " + nazwisko
        warsztat_python.append(uczestnik)

    elif(wybór == 2):
        imię = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        uczestnik = imię + " " + nazwisko
        warsztat_ai.append(uczestnik)   

    elif(wybór == 3):
        print("Uczestnicy warsztatu Python: ")
        for uczestnik in warsztat_python:
            print(uczestnik)
        print("Uczestnicy warsztatu AI: ")
        if(len(warsztat_ai) == 0):
            print("Brak uczestników")
        else:    
            for uczestnik in warsztat_ai:
                print(uczestnik)

    elif(wybór == 4):
        uczestnicy_obu = set(warsztat_python) & set(warsztat_ai)
        print("Uczestnicy obu warsztatów: ")
        for uczestnik in uczestnicy_obu:
            print(uczestnik)   

    elif(wybór == 5):
        unikalni_uczestnicy = set(warsztat_python) | set(warsztat_ai)
        print("Unikalni uczestnicy: ")
        for uczestnik in unikalni_uczestnicy:
            print(uczestnik)

if(wybór < 0 or wybór > 5):
    print("Nieprawidłowy wybór. Spróbuj ponownie.")



    

        



