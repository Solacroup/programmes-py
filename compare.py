from cs50 import get_int

# recueillir les entiers
a = get_int("entier a : \n")
b = get_int("entier b : \n")
c = get_int("entier c : \n")

# comparer les entiers entre eux
if a > b and a > c:
    # afficher le résultat
    print("a est le plus grand")
elif b > a and b > c:
    print("b est le plus grand")
elif c > a and c > b:
    print("c est le plus grand")
else:
    print("il y a une égalité")
