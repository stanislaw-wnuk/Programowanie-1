temperatury = []
for i in range(7):
    temp = input("Podaj temperaturę dnia " + str(i+1) + ": ")
    temperatury.append(float(temp))
średnia = sum(temperatury) / len(temperatury)
maks = max(temperatury)
minimum = min(temperatury)
powyżej = [] 
liczba = 0
for temp in temperatury:
    if temp > średnia:
        powyżej.append(temp)
        liczba += 1
print("Średnia temperatura: ", średnia)
print("Maksymalna temperatura: ", maks)
print("Minimalna temperatura: ", minimum)
print("Temperatury powyżej średniej: ", powyżej)
print("Liczba dni: ", liczba)
        