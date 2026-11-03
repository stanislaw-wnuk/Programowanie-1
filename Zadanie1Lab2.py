lista = []
ilość = input("Ile produktów dodać? ")
for i in range(int(ilość)):
    produkt = input("Produkt" + str(i+1) + ":")
    lista.append(produkt)
print("Lista produktów: ", lista)   
trash = input("Podaj produkt do usunięcia: ")
if trash in lista:
    lista.remove(trash)
    print("Nowa lista: ", lista)
else:
    print("Produkt nie znajduje się na liście.")
