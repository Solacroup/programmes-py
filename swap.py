from cs50 import get_int

# recueillir les entiers
a = get_int("entier a : \n")
b = get_int("entier b : \n")
# afficher la valeur des entiers
print(f"a vaut {a} et b vaut {b} \n")
# utiliser la fonction swap
a, b = b, a  # échange
# afficher la valeur des entiers après l'échange
print(f"a vaut {a} et b vaut {b} \n")
