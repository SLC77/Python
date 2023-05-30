## Exercice 1 :

##Écrire un programme qui affiche un triangle de la taille d'un nombre rentré par l'utilisateur dans la console à l'aide de caractères "#".


#def triangle(num, tag='#'):
#    if num > 0:
#        for x in range(num):
#            print((x+1) * tag)
#    else:
#        num = abs(num)
#        for i in range(num-1, -1, -1):
#            print((i+1) * tag)
#triangle(-15)

## Exercice 2 :
##Écrire une fonction qui prend une liste de nombre en paramètre et qui renvoie la somme de tous les éléments de la liste

#liste = [1, 2, 3, 4]

#def somme(liste):
#    return sum(liste)

#somme_totale = somme(liste)
#print(somme_totale)

## Exercice 3 :

##Écrire une fonction qui prend comme argument une liste de nombre, et qui renvoie la moyenne des nombres de la liste.

#liste = [1, 2, 3, 4, 5]

#def avg(liste):
#    return sum(liste)/len(liste)

#avgliste = avg(liste)

#print (avgliste)

## Exercice 4 :

##Créez un programme qui affiche dans la console tous les nombres de 1 à 100 avec deux exceptions : les nombres divisibles par 3, doivent être remplacés par « Fizz » et ceux divisibles par 5 doivent être remplacés par « Fuzz ».

#for lst in range(1, 101):
#    if lst % 3 == 0:
#        print('Fizz')
#    elif lst % 5 == 0:
#        print('Fuzz')

#print(lst)

## Exercice 5 : 

#Écrire une fonction qui prend comme argument une liste et qui renvoie une liste contenant les mêmes éléments, mais dans l'ordre inverse.

# Les différentes consoles

consoles = ['Nintendo', 'Playstation', 'Xbox']
print('Original list', consoles)

#Reversing list
consoles.reverse()

print('New list', consoles)