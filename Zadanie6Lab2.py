ToDoList = []
print("1. Dodaj do listy")
print("2. Usuń z listy")
print("3. Wyświetl listę")
print("4. Wyświetl ilość zadań")
print("0. Zakończ")
while True:
    liczba = 0
    wybór = input("Co robimy? - ")
    if wybór == "1":
        zadanie = input("Jakie plany na dziś szefie? - ")
        ToDoList.append(zadanie)
        liczba += 1
    elif wybór == "2":
        usun = input("Co wywalić? - ")
        if usun in ToDoList:
            ToDoList.remove(usun)
            liczba -= 1
        else: print("Chyba ci się coś pomyliło")
    elif wybór == "3":
        print("O to twoje dzieło na dziś ", ToDoList)
    elif wybór == "4":
        print("Liczba Zadań: ", liczba)
    elif wybór == "0":
        print("Jarvis na ciebie będzie czekał, Adios")
        break





