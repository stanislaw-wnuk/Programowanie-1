import numpy as np

pomiary = []
while True:
    ilość = int(input("Podaj ilość pomiarów (>1) : "))
    if ilość <= 1:
        print("Złe dane")
    else:
        for i in range(ilość):
            print("Podaj pomiar nr " + str(i + 1))
            pomiar = float(input())
            pomiary.append(pomiar)
        np.array(pomiary)
        print("Średnia: " + str(np.mean(pomiary)))
        print("Maksimum: " + str(np.max(pomiary)))
        print("Minimum: " + str(np.min(pomiary)))
        print("Rozstęp: " + str(np.ptp(pomiary)))

