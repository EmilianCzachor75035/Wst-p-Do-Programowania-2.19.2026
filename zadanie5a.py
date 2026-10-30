#zadanie5a

#Odczytaj podany plik notwania_gieldowe.txt zawierający dane dotyczące notowań kilku spółek. Wydrukuj każdą linię do konsoli. 

with open("notowania_gieldowe.txt", "r") as plik:
    for linia in plik:
        print(linia)