def dodawanie(a, b):
    return a + b
def odejmowanie(a, b):
    return a - b
def mnożenie(a, b):
    return a * b
def dzielenie(a, b):
    if b == 0:
        return "Nie można dzielić przez zero!"
    else:
        return a / b
def potęgowanie(a, b):
    return a ** b

def średnia():
    liczby = []
    n = int(input("Podaj ilość liczb do obliczenia średniej: "))
    for i in range(n):
        liczba = float(input(f"Podaj liczbę {i+1}: "))
        liczby.append(liczba)
    return sum(liczby) / n


def wyświetl_menu():
    print("\nWybierz działanie:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Potęgowanie")
    print("6. Średnia")
    print("0. Zakończ")

def main():
    while True:
        wyświetl_menu()
        wybór = input("Wybierz opcję: ")
        if wybór != "6" and wybór != "0":
           a = float(input("Podaj pierwszą liczbę: "))
           b = float(input("Podaj drugą liczbę: "))

        if wybór == "0":
            print("Zakończono program.")
            break

        if wybór == "1":
            wynik = dodawanie(a, b)
            print(f"Wynik dodawania: {wynik}")
        elif wybór == "2":
            wynik = odejmowanie(a, b)
            print(f"Wynik odejmowania: {wynik}")
        elif wybór == "3":
            wynik = mnożenie(a, b)
            print(f"Wynik mnożenia: {wynik}")
        elif wybór == "4":
            wynik = dzielenie(a, b)
            print(f"Wynik dzielenia: {wynik}")
        elif wybór == "5":
            wynik = potęgowanie(a, b)
            print(f"Wynik potęgowania: {wynik}")
        elif(wybór == "6"):
            wynik = średnia()
            print(f"Średnia: {wynik}")    
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")

if __name__ == "__main__":
    main()            


