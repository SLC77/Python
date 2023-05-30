### Exercice 1 : 
###Transformez en fonction le code suivant :

#nb_utilisateur = int(input("Entrez un nombre entier : "))

#if nb_utilisateur % 2 == 0:
#    print("le nombre est pair")
#else:
#    print("Le nombre est impair")

#nb_user = int(input("Please, enter a number : ")) #On entre un chiffre pour chercher si il est pair ou impair

#def pair(nb_user:int):  #On lance la fonction pour vérifier si le chiffre est pair ou impair

#    if nb_user % 2 == 0:    
#        print('Le nombre est pair') #Si le nombre est pair, il affichera cette phrase
#    else:
#        print('Le nombre est impair') #Si le nombre est impair, à la place il affichera cettte phrase

#pair (nb_user) #On termine en appelant la fin de fonction qui affichera le if ou le else


### Exercice 2 :

###Écrire une fonction est_pair(). 
###Cette fonction prend en argument un nombre nb, et renvoie True si nb est pair, False sinon.

#nb = int(input("Entrez un nombre : ")) #On entre un chiffre pour savoir si il est pair ou impair

#def est_pair(nb:int): #on defini la fonction qui va chercher si le nombre est pair ou impair
    
#    if nb % 2 == 0: #On appelle le modulo pour diviser le nombre par 2 afin de savoir si celui-ci est pair ou impair
#        print('True') #On demande d'afficher True si c'est pair
#    else:
#        print('False') #On demande d'afficher False si c'est impair

#est_pair(nb)

### Exercice 3 :

###Écrire une fonction qui prend pour argument 3 nombres, et renvoie le plus petit des trois

#nb1 = int(input('Enter a number :' )) #On demande au user de rentrer un nombre
#nb2 = int(input('Enter a second number :' )) #Un second
#nb3 = int(input('Enter a  third number :' )) #Un troisième

#def petit(nb1, nb2, nb3): #On defini une fonction pour retrouver le plus petit nombre
#    return min(nb1, nb2, nb3) #On utilise min() afin de renvoyer au nombre le plus petit

#plus_petit = petit(nb1, nb2, nb3) #On defini la variable "plus petit" au nombre renvoyer par la fonction "petit"
#print ('Le plus petit nombre est :', plus_petit) 


### Exercice 4 :

###Écrire la docstring de la fonction suivante, et améliorer la qualité du code :

#On defini des variables en nombre
#nb1 = 50
#nb2 = 65

#def entier(nb1, nb2): 
#    if nb1 < 0:
#       nb1 = -nb1
#    if nb2 < 0:
#        nb2 = -nb2
#    return nb1*nb2

#nb_entier = entier(nb1, nb2)
#print ('Le nombre entier est : ', nb_entier)

### Exercice 5 : 

###Écrire une fonction qui prend en paramètres 3 nombres, et renvoie la moyenne des trois.

list_nb = [15, 97, 4]

def average(list_nb):
    return sum(list_nb)/len(list_nb)

moyenne = average(list_nb)
print ('La moyenne de ces trois nombre est de ', round(moyenne))