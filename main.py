from functions import *

greeting1 = greet(name="Karl")
print(greeting1)
greet(name="Susi")

result1 = calculate_sum(num1=10, num2=20)
print(result1)

liste = [1, 5, 3, 9]

print(liste_umsortieren(liste))

#zeichen1 = input("Geben sie was ein")
#zeichen2 = input("Geben sie was ein")
#print(zeichenketten_umkehren(zeichen1, zeichen2))

#distanz = int(input("Welche Distanz sind sie gegangen?"))
#schrittlaenge = int(input("Wie lange sind ihre Schritte"))
#print(schritte(distanz, schrittlaenge))

zeichenkette = input("geben sie etwas ein")
encoded = (encode(zeichenkette))
print(encoded)
decoded= decode(encoded)
print(decoded)