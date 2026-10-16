ilość = input("Podaj ilość punktów")
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

if int(ilość) > 100:
    print("Nieprawidłowe dane")
else:
    print("Ilość zdobytych punktów: " + str(ilość))
    print("Ocena końcowa: " + str(ocena))
