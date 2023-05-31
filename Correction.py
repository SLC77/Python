# Exercice 1 :

input_user = input("Please enter your distance (miles) : ")
try:
    input_user = int(input_user)
    print(f"Your distance is {input_user * 1.6} km")
except ValueError:
    print("I ask for a number ...")

# Exercice 2 :

var1 = "Je dois être en seconde position"
var2 = "Je dois être en première position"

## Ajouter le code de l'exercice ici ##

var1, var2 = var2, var1

print(var1 + " | " + var2) 
# après avoir complété l'exercice, doit afficher :
# Je dois être en première position | Je dois être en seconde position


# Exercice 1 :

user_input = int(input("Please enter a number : "))

if user_input % 2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")
    
# Exercice 2

nb1 = int(input("Entrez un nombre : "))
nb2 = int(input("Entrez un deuxième nombre : "))
nb3 = int(input("Entrez un troisième nombre : "))

if nb1 >= nb2 and nb1 >= nb3:
    print(nb1)
elif nb2 >= nb1 and nb2 >= nb3:
    print(nb2)
else:
    print(nb3)


# Exercice 1 :

def est_pair(nb:int) -> None:
    """Fonction qui affiche dans le terminal si le nombre est pair

    Args:
        nb (int): Le nombre à tester
    """
    if nb % 2 == 0:
        print("le nombre est pair")
    else:
        print("Le nombre est impair")

nb_utilisateur = int(input("Entrez un nombre entier : "))
est_pair(nb_utilisateur)


# Exercice 2 :

def est_pair(nb:int) -> bool:
    """Fonction qui vérifie si un nombre est pair

    Args:
        nb (int): Le nombre à tester

    Returns:
        bool: True si le nombre est pair, False sinon
    """
    if nb % 2 == 0:
        return True
    else:
        return False
    
# exercice 3

def renvoyer_minimum(nb1:int, nb2:int, nb3:int) -> int:
    """Fonction qui renvoie le plus petit de ses paramètres

    Args:
        nb1 (int): Un premier nombre à tester
        nb2 (int): Un deuxième nombre à tester
        nb3 (int): Un troisième nombre à tester

    Returns:
        int: Le plus petit des trois paramètres
    """
    if nb1 <= nb2 and nb1 <= nb3:
        return nb1
    elif nb2 <= nb1 and nb2 <= nb3:
        return nb2
    else:
        return nb3

# exercice 4 :

def produit_des_valeurs_absolues(nombre1:int, nombre2:int) -> int:
    """Fonction qui renvoie le produit des valeurs absolues de ses arguments

    Args:
        nombre1 (int): Un nombre
        nombre2 (int): Un deuxième nombre

    Returns:
        int: Le produit des valeurs absolues de nombre1 et nombre2
    """
    if nombre1 < 0:
        nombre1 = -nombre1
    if nombre2 < 0:
        nombre2 = -nombre2
    return nombre1 * nombre2

# Exercice 5

def calculer_moyenne(nb1:float, nb2:float, nb3:float) -> float:
    """Fonction qui calcule la moyenne des 3 arguments

    Args:
        nb1 (float): Un premier nombre
        nb2 (float): Un deucième nombre
        nb3 (float): Un troisième nombre

    Returns:
        float: La moyenne des trois nombres
    """
    return (nb1 + nb2 + nb3) / 3


# Exercice 1

input_user = int(input("Entrez un nombre"))

for i in range(1, input_user + 1):
    print("#" * i)
    
# Exercice 2

def calculer_somme(liste:list) -> float:
    """Fonction qui renvoie la somme des elements de la liste

    Args:
        liste (list): Une liste de nombre

    Returns:
        float: La somme des nombres de la liste
    """
    resultat = 0.
    for nb in liste:
        resultat += nb
    return resultat

# Exercice 3

def calculer_moyenne(liste:list) -> float:
    """Fonction qui renvoie la moyenne des éléments de la liste

    Args:
        liste (list): Une liste de nombres

    Returns:
        float: La moyenne des éléments de la liste
    """
    return calculer_somme(liste) / len(liste)

# Exercice 4

# V1
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Fuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Fuzz")
    else:
        print(i)

# V2     
for i in range(1, 101):
    print(i, end=" : ")
    if i % 3 == 0:
        print("Fizz", end=" ")
    if i % 5 == 0:
        print("Fuzz", end="")
    print()
    
# Exercice 5

liste = [1, "test", 0.9867, "Python, c'est génial !"]

def renverser_liste(liste:list) -> list:
    """Fonction qui inverse l'ordre de la liste

    Args:
        liste (list): La liste à renverser

    Returns:
        list: La liste renversée
    """
    liste2 = liste.copy()
    for i in range(0, len(liste)//2):
        liste2[i], liste2[-1 - i] = liste2[-1 - i], liste2[i]
    return liste2

print(renverser_liste(liste))
print(liste)

# Exercice 6

dico = {
    "Python" : "Le meilleur langage de programmation du monde entier d'après Antoine",
    "Pi" : 3.14,
    "ma_liste" : ["Bonjour", "ceci", "est", 1, "liste"]
}

dico["mx5"] = "Voiture sympa"
dico["mx5"] = "Voiture très sympa"

input_user = input("Cherchez vous un mot ?")
if dico.get(input_user) != None:
    print(dico.get(input_user))
else:
    print("Nous ne connaissons pas ce mot")
    
# Exercice 7

from random import randint

liste = []
for _ in range(1000):
    liste.append(randint(1, 100))
print(liste)

liste = [randint(1, 100) for _ in range(1000)]

# Exercice 8

# Methode classique
liste_inf_10 = []
for elt in liste:
    if elt < 10:
        liste_inf_10.append(elt)
print(liste_inf_10)

# Methode par compréhension
liste_inf_10 = [elt for elt in liste if elt < 10]
print(liste_inf_10)

