pomiary = {}
pierwszetrzy = []
ostatnietrzy = []
codrugi = []

Ilość = int(input("Podaj ilość pomiarów: "))
for i in range(Ilość):
    pomiar = input("Podaj pomiar " + str(i+1) + ": ")
    pomiary[i+1] = pomiar
print ("Pierwszy pomiar: " + str(pomiary[1]))
print ("Ostatni pomiar: " + str(pomiary[Ilość]))

if(Ilość < 4):
    wynik2 = list(pomiary.values())
    print ("Wszystkie pomiary: " + str(wynik2))
else:
    wynik1 = list(pomiary.values())
    print ("Pierwsze trzy: " +  str(wynik1[0:3]))
    print ("Ostatnie trzy: " + str(wynik1[-3:]))

for i in range(Ilość//2):
    codrugi.append(pomiary[i*2+1])
print ("Co drugi pomiar: " + str(codrugi))    

odwrócone = list(pomiary.values())
odwrócone.reverse()
print ("Odwrócone pomiary: " + str(odwrócone))

Kopia = pomiary.copy()
Kopia[1] = "0"
print("Oryginał: " + str(list(pomiary.values())))
print("Kopia: " + str(list(Kopia.values())))




