kwota = input("Podaj kwotę: ")
tygodnie = input("Podaj liczbę tygodni: ")
oszczędności = 0
nr = 0
for i in range(int(tygodnie)):
    oszczędności += int(kwota)
    nr += 1
    print("Numer tygodnia: " + str(nr) + ", Kwota oszczędności: " + str(oszczędności) + " zł")

print("Łączna kwota: " + str(oszczędności) + " zł")
