napoje = ["Woda", "Sok", "Cola"]
cena = [3, 5, 6]
print("1. Woda - 3zł")
print("2. Sok - 5zł")
print("3. Cola - 6zł")
print("0. Zakończ")
koszyk = 0
while True:   
   wybór = input("Wybierz napój: ")
   if wybór == "1":
      print("Wybrano wodę - 3zł")
      koszyk += cena[int(wybór) - 1]
   elif wybór == "2":
      print("Wybrano sok - 5zł")
      koszyk += cena[int(wybór) - 1]
   elif wybór == "3":
        print("Wybrano colę - 6zł")
        koszyk += cena[int(wybór) - 1]
   elif wybór == "0":
       print ("Koszt koszyka: ", koszyk, "zł")
       break
   



