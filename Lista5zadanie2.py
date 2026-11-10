import numpy as np

produkty = {}
ceny = []
nowe_ceny = []


while True:
    ilość = int(input("\nPodaj liczbę produktów (>1): "))
    if ilość <= 1:
        print("Złe dane")
    else:
        for i in range(ilość):
            nazwa = input("Podaj nazwę produktu nr " + str(i + 1) + ": ")
            cena = float(input("Podaj cenę produktu nr " + str(i + 1) + ": "))
            produkty[nazwa] = cena
            ceny.append(cena)
        ceny =np.array(ceny)
        procent = int(input("Podaj rabat procentowy: "))
        nowe_ceny = ceny * (1 - procent / 100)
        print("\nSuma przed rabatem: " + str(np.sum(ceny)))
        print("Suma po rabacie: " + str(np.sum(nowe_ceny)))
        print("Ceny powyżej 100: " + str(nowe_ceny[np.array(nowe_ceny) > 100]))

