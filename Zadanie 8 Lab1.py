wysokość = input("Podaj wysokość choinki")
for i in range(int(wysokość)):
    print(" " * (int(wysokość) - i - 1) + "*" * (2 * i + 1) + " " * (int(wysokość) - i - 1))
    
    
