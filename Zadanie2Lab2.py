liczba_studentów = int(input("Podaj liczbę studentów: "))
punkty = []
for i in range(liczba_studentów):
    punkt = input("Podaj punkty studenta " + str(i+1) + ": ")
    punkty.append(int(punkt))
średnia = sum(punkty) / len(punkty)
maks = max(punkty)
minimum = min(punkty)
print("Średnia punktów: ", średnia)
print("Maksymalna liczba punktów: ", maks)
print("Minimalna liczba punktów: ", minimum)
print("Wyniki rosnąco: ", sorted(punkty))

