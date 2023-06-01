#nbUtilisateur = int(input("Entrez un nombre "))

#if nbUtilisateur < 0:
    # code qui s'exécute si nbUtilisateur est plus petit que 0
    #print("Votre nombre est négatif")
#else:
    # sinon, c'est ce code qui s'exécute
    #print("Votre nombre est positif ou nul !")

#nb1 = 9
#nb2 = 8
#nb3 = 7

#if nb1 > nb2 and nb2 > nb3:
    # si nb1 > nb2 et nb2 > nb3 alors on exécute ce code
#    print("Vous avez entrez les nombre par ordre décroissant !")
#elif nb1 < nb2 and nb2 < nb3:
    # sinon, si nb1 < nb2 et nb2 < nb3 alors on exécute ce code
#    print("Vous avez entrez les nombre par ordre croissant !")
#else:
    # sinon, on exécute celui-ci
#    print("Tout est dans le désordre !")

### Exercice 1 : pair ou impair ?

#number = int(input('Entrez un nombre : '))
#if (number % 2) == 0:
#        print('Le chiffre est pair')
#else:
#        print('Le chiffre est impair')

### Exercice 2 : trouver le maximum entre 3 nombres.

num1 = int(input('Please, enter a number : '))
num2 = int(input('Please, enter a second number : '))
num3 = int(input('Please, enter a third number : ')) 

if num1 > num2 and num2 > num3:
    print('Le nombre plus grand est',num1)
elif num1 < num2 and num2 > num3:
    print('Le nombre plus grand est ',num2)
else:
    print('Le nombre plus grand est',num3)

