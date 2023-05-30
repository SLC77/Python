import turtle

turtle.speed(25) # set the speed

# Ceci est un commentaire, les commentaires sont ignorés par l'ordinateur.
# Ils sont ici pour permettre aux développeur de garder leur code compréhensible 
# (pour eux même ou pour les autres)

#turtle.speed(8) # permet de régler la vitesse d'animation de la tortue (1 étant le plus lent, 10 le plus rapide)

# Début des instructions permettant de dessiner : insérer votre code ici !

#turtle.begin_fill() # permet d'indiquer à la tortue que l'on souhaite remplir la forme dessinée.
#turtle.forward(200) # Ici une instruction permettant d'avancer de 200px
#turtle.circle(30) # Ici une instruction permettant de dessiner un cercle de rayon 30px
#turtle.end_fill() # permet d'indiquer à la tortue que nous n'avons plus besoin de remplir les nouvelles formes
#turtle.circle(90)

# fin des instruction permettant de dessiner.

#turtle.done() # permet d'indiquer à la tortue que nous avons fini le dessin

#This to make turtle object
tess=turtle.Turtle()

# self defined function to print coordinate
def buttonclick(x,y):
	print("You clicked at this coordinate({0},{1})".format(x,y))


#onscreen function to send coordinate
turtle.onscreenclick(buttonclick,1)
turtle.listen() # listen to incoming connections
turtle.pensize(2)

#Dessin du carré

turtle.penup()
turtle.left(180)
turtle.forward(200)
turtle.pendown()
turtle.forward(100) #la tortue avance de 100 pixels.
turtle.right(90)     #la tortue se tourne de 90° à gauche.
turtle.forward(100) #la tortue avance de 100 pixels.
turtle.right(90)     #la tortue se tourne de 90° à gauche.
turtle.forward(100) #la tortue avance de 100 pixels.
turtle.right(90)     #la tortue se tourne de 90° à gauche.
turtle.forward(100) #la tortue avance de 100 pixels.
turtle.right(90)     #la tortue se tourne de 90° à gauche.

#Dessin du pentagone 

turtle.penup()
turtle.left(180)
turtle.forward(50)
turtle.pendown()
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)

#Dessin du bateau

turtle.penup()
turtle.left(72)
turtle.forward(180)
turtle.pendown()
turtle.forward(75)
turtle.left(35)
turtle.forward(25)
turtle.left(180)
turtle.penup()
turtle.forward(25)
turtle.right(35)
turtle.forward(75)
turtle.right(35)
turtle.pendown()
turtle.forward(25)
turtle.right(145)
turtle.forward(115)
turtle.penup()
turtle.goto(10.0,17.0)
turtle.pendown()
turtle.forward(115)
turtle.backward(57.5)
turtle.left(90)
turtle.forward(100)
turtle.backward(100)
turtle.left(90)
turtle.forward(57.5)
turtle.right(90)
turtle.right(30)
turtle.forward(115)
turtle.right(120)
turtle.forward(115)
turtle.done() # hold the screen



