pomiary = []
ilość = int(input("Podaj ilość pomiarów: "))
for i in range(ilość):
    pomiar = int(input("Podaj pomiar " + str(i+1) + ": "))
    pomiary.append(pomiar)
próg = 50
    
podwojone = [x * 2 for x in pomiary]
wieksze = [x for x in pomiary if x > próg]

print(wieksze)
print(podwojone)
print("Czy wystąpił alarm? " + str(any(x > próg for x in pomiary)))
print("Czy wszystkie pomiary są prawdisłowe? " + str(all(x > próg for x in pomiary)))

