czas = input("Ile godzin parkowałeś samochód na parkingu? ")
if int(czas) <= 0:
    print("Nieprawidłowe dane")
elif int(czas) <= 1:
    cena = 5
elif int(czas) <= 3:
    cena = 12
elif int(czas) <= 6:
    cena = 20
else:
    cena = 30
print("Czas parkowania: " + str(czas) + " godziny")
print("Cena do zapłaty: " + str(cena) + " zł")            