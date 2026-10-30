#zadanie1

#Napisz prosty program, który na podstawie podanej przez Studenta liczby zdobytych punktów, poinformuje go o rezultacie egzaminu. 
#Każdy Student, który zdobył powyżej 80 punktów zalicza egzamin w terminie 0 
#Studenci którzy otrzymali liczbę punków z przedziału 50-80,  mogą poprawić jego wynik.   Studenci, którzy zdobyli poniżej 50 punktów, muszą go poprawić.  


x = int(input("wprowadz liczbe punktow uzyskanych na egzaminie"))
if x < 50:
    print("Egzamin nalezy poprawic")
elif x >= 50 and x <= 80:
    print("Egzamin MOZNA poprawic")
else:
    print("Egzamin zostal zdany w terminie 0")