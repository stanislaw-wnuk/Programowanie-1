cena = input("Podaj cenę: ")
procent = input("Podaj wartość procentową rabatu: ")
rabat = (int(cena) * int(procent)) / 100
kwota = (int(cena) - rabat)

print("Początkowa cena: " + str(cena) + " zł")
print("Wartość rabatu: " + str(rabat) + " zł")
print("Cena po rabacie: " + str(kwota) + " zł")
if rabat > 20:
    print("DUŻA PROMOCJA!")
else:
    print("Standardowa promocja.")    