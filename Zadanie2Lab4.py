ilość = int(input("Podaj ilość produtów: "))
produkty = []
ceny = []
for i in range(ilość):
    produkt = input("Podaj nazwę produktu " + str(i+1) + ": ")
    cena = float(input("Podaj cenę produktu " + str(i+1) + ": "))
    produkty.append(produkt)
    ceny.append(cena)
print("CENNIK")
for numer, produkt in enumerate(produkty, start=1):
    print(str(numer) + ". " + produkt + " - " + str(ceny[numer-1]))   

suma = sum(ceny)
print("Suma cen produktów: " + str(suma)) 

print("Najdroższy produkt: " + produkty[ceny.index(max(ceny))] + " - " + str(max(ceny)))
