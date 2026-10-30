#zadanie5b

#Odczytaj podany plik notwania_gieldowe.txt zawierający dane dotyczące notowań kilku spółek. Wydrukuj każdą linię do konsoli. 

with open("notowania_gieldowe.txt", "a") as plik:
    plik.write("\nALR, 113")
with open("notowania_gieldowe.txt", "r") as plik2:
    for linia in plik2:
        print(linia)