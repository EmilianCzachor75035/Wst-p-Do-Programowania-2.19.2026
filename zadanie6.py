#zadanie6

#Napisz skrypt w Pythonie, który sprawdza, czy litera wprowadzona przez użytkownika jest duża czy mała

x = input("Wprowadz litere")
if x.isupper():
    print("Litera jest duza")
elif x.islower():
    print("Litera jest mala")
else:
    print("To nie jest litera")