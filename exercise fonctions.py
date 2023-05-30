### Exercice 1 : 
#Transformez en fonction le code suivant :

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

#Écrire une fonction est_pair(). 
#Cette fonction prend en argument un nombre nb, et renvoie True si nb est pair, False sinon.

nb = int(input("Entrez un nombre : ")) #On entre un chiffre pour savoir si il est pair ou impair

def est_pair(nb:int): #on defini la fonction qui va chercher si le nombre est pair ou impair
    
    if nb % 2 == 0: #On appelle le modulo pour diviser le nombre par 2 ou voir si il tombe sur un chiffre pair ou impair
        print('True') #On demande d'afficher True si c'est pair
    else:
        print('False') #On demande d'afficher False c'est impair

est_pair(nb)
