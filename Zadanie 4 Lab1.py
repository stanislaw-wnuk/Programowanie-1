wiek = input("Podaj swój wiek: ")
if int(wiek) < 13:
    print("Nie możesz wypożyczyć roweru")
elif int(wiek) < 18:
    zgoda = input("Czy masz zgodę opiekuna? ")
    dokument = input("Czy masz dokument tożsamości? ")
    if zgoda == "tak" and dokument == "tak":
        print("Możesz wypożyczyć rower")
                 
else:
    dokument = input("Czy masz dokument tożsamości? ")
    if dokument == "tak":
        print("Możesz wypożyczyć rower")            