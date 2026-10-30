#zadanie2

#apisz program porządkowania trzech liczb x, y i z. Od najmniejszej do największej, bez użycia wbudowanych funkcji 

x = float(input("Wprowadz x"))
y = float(input("Wprowadz y"))
z = float(input("Wprowadz z"))

if x > y:
    x,y = y,x
if x > z:
    x,z = z,x
if y > z:
    y,z = z,y
print(x,y,z)