
osoby = []
punkty = []
oceny = []
zal = 0
ilość = int(input("Podaj liczbę studentów: "))
for i in range(ilość):
    nazwisko = input("Podaj nazwisko studenta " + str(i+1) + ": ")
    wynik = int(input("Podaj wynik studenta " + str(i+1) + ": "))
    osoby.append(nazwisko)
    punkty.append(wynik)
    if int(wynik) < 50:
        ocena = 2
    elif int(wynik) < 60:
        ocena = 3
        zal =+ 1
    elif int(wynik) < 70:
        ocena = 3.5
        zal =+ 1
    elif int(wynik) < 80:
        ocena = 4
        zal =+ 1
    elif int(wynik) < 90:
        ocena = 4.5
        zal =+ 1
    else:
        ocena = 5
        zal =+ 1
    oceny.append(ocena)

for i in range(ilość):
    print("Student: " + osoby[i] + ", Punkty: " + str(punkty[i]) + ", Ocena: " + str(oceny[i]))

print("Średnia ocen: " + str(sum(oceny)/len(oceny)))
print("Liczba zaliczeń: " + str(zal))

import matplotlib.pyplot as plt
plt.bar(osoby, oceny)
plt.title("Wyniki egzaminu")
plt.xlabel("Student")
plt.ylabel("Ocena")
plt.ylim(0, 5.5)
plt.show()
