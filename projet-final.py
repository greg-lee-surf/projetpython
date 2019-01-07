## projet : Multiplication modulaire

from tkinter import *
from math import sin,cos,pi


root = Tk()  # initialisation d'une fenetre graphique

## Construction du cercle

canvas = Canvas(root, width = 510, height = 510) 
canvas.grid(row=5,column=1) 


Xmax = 505
Xmin = 5
Ymax = 505
Ymin = 5

circle = canvas.create_oval(Xmin,Ymin,Xmax,Ymax)

## On definit les variables necessaire a placer les points du cercle

R = (Xmax - Xmin)/2 # rayon du cercle

a = (Xmax + Xmin)/2 # milieu des abcisses
b = (Ymax + Ymin)/2 # milieu des ordonnees

## points autour du cercle
    
def points():
    
    """Fonction qui place les points autour du cercle."""
    
    circle = canvas.create_oval(Xmin,Ymin,Xmax,Ymax) # re-creation du cercle
    
    global lst_points_x
    global lst_points_y
    p = int(case_2.get()) # le modulo
    arc = 2*pi/p # longueur d'un arc de cercle
    
    lst_points_x = [] # creation d'une liste qui va contenir les coordonnees des points de Ox
    lst_points_y = [] # creation d'une liste qui va contenir les coordonnees des points de Oy

    for i in range(p):
    
        x = a + R*cos(i*arc-pi/2) 
        y = b + R*sin(i*arc-pi/2)

        lst_points_x.append(x) # on ajoute x a la liste 
        lst_points_y.append(y) # on ajoute y a la liste 
        
        M = canvas.create_oval(x,y,x,y,width=0.001) # coordonnes des points tout autour du cercle
        
    return lst_points_x, lst_points_y

## Traits du cercle


def traits(m,i):
    
    """Fonction qui va tracer les traits entre les differents points du cercle."""
    global lst_points_x
    global lst_points_y
    x_1 = lst_points_x[i] 
    y_1 = lst_points_y[i]  
    x_2 = lst_points_x[m] 
    y_2 = lst_points_y[m] 
    trait = canvas.create_line(x_1,y_1,x_2,y_2)

def mult_mod(n,p):
    
    """Fonction qui effectue le calcul de la multiplication modulaire et rejoint 
        les differnts points."""
    
    for i in range(p):  
        m = n*i
        if m >= p :
            while m >= p :
                m = m-p
        traits(m,i) # fonction qui trace les traits

    
def modulo():
    
    """Fonction qui calcule la table de a de 0 a n modulo p. Cette fonction 
        fait appel aux fonctions 'traits' et 'points'. """
    
    canvas.delete("all") # On nettoie la fenetre
    
    n = int(case_1.get()) # la table
    p = int(case_2.get()) # le modulo
    
    points() # place les points 
    
    mult_mod(n,p) # rejoint les points
    
    return n,p
    
    
def Transition(n,p):
    """Fonction qui permet la transition entre les differentes valeurs selctionnees. """
    
    n_1 = int(case_1.get())
    p_1 = int(case_2.get())
    
    d_n = abs(n_1 - n) # difference entre la table choisit et la precedente
    d_p = abs(p_1 - p) # differrence entre le modulo choisit et le precedent
    
    for i in range(d_n):
        if n <= n_1:
            while n <= n_1:
                n = n+i
                mult_mod(n,p)
    
    
## Creation des cases pour choisir les differentes valeurs
texte_1 = Label(root, text="table de : ")
texte_2 = Label(root, text="modulo : ")
case_1 = Entry(root)
case_2 = Entry(root)
boutton = Button(root, text="cliquez pour valider", command=modulo) #en cliquant sur ce bouton on appel la fonction trait


texte_1.grid(row=0,column=0)
texte_2.grid(row=0,column=2)
case_1.grid(row=0,column=1)
case_2.grid(row=0,column=3)
boutton.grid(row=0,column=4)
root.mainloop() # affiche la fenetre graphique
