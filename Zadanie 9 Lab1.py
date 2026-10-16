początek = input("Podaj początek przedziału: ")
koniec = input("Podaj koniec przedziału: ")
parzyste = 0
for i in range(int(początek), int(koniec) + 1):
    if i % 2 == 0:
        print(str(i) + " - Parzysta")
        parzyste += 1
    else:
        print(str(i) + " - Nieparzysta")

print("Liczb parzystych jest: " + str(parzyste))
    
