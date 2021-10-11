from cs50 import get_int

# programme principal


def main():
    # recueillir les entiers
    a = get_int("entier a : \n")
    b = get_int("entier b : \n")
    # afficher la valeur des entiers
    print(f"a vaut {a} et b vaut {b} \n")
    # utiliser la fonction swap
    swap(a, b)
    # afficher la valeur des entiers après l'échange
    print(f"a vaut {a} et b vaut {b} \n")

# fonction d'échange


def swap(c, d):
    # utilisation d'une variable temporaire
    tmp = c
    c = d
    d = tmp

# appel de la fonction programme principal


main()

