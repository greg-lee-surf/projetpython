# # projet : Multiplication modulaire

from tkinter import *
from math import sin, cos, pi
import time

root = Tk()  # initialisation d'une fenetre graphique

# # Construction du cercle

canvas = Canvas(root, width=600, height=600) 
canvas.grid(row=3, column=1) 

Xmax = 525
Xmin = 25
Ymax = 525
Ymin = 25

circle = canvas.create_oval(Xmin, Ymin, Xmax, Ymax)

# # On definit les variables necessaire a placer les points du cercle

R = (Xmax - Xmin) / 2  # rayon du cercle

a = (Xmax + Xmin) / 2  # milieu des abcisses
b = (Ymax + Ymin) / 2  # milieu des ordonnees

# # Liste pour  remplis

# # points autour du cercle
n_1 = 1 
p_1 = 1

    
def points(modulo):
    
    """Fonction qui place les points autour du cercle."""
    
    circle = canvas.create_oval(Xmin, Ymin, Xmax, Ymax)  # re-creation du cercle
    
    global lst_points_x
    global lst_points_y
    p = int(modulo)  # le modulo
    arc = 2 * pi / p  # longueur d'un arc de cercle
    
    lst_points_x = []  # creation d'une liste qui va contenir les coordonnees des points de Ox
    lst_points_y = []  # creation d'une liste qui va contenir les coordonnees des points de Oy

    for i in range(p):
    
        x = a + R * cos(i * arc - pi / 2) 
        y = b + R * sin(i * arc - pi / 2)

        lst_points_x.append(x)  # on ajoute x a la liste 
        lst_points_y.append(y)  # on ajoute y a la liste 
        
        M = canvas.create_oval(x, y, x, y, fill ='red')  # coordonnes des points tout autour du cercle

        x_text = a + (R + 10) * cos(i * arc - pi / 2) 
        y_text = b + (R + 10) * sin(i * arc - pi / 2)

        canvas.create_text(x_text, y_text, text=i, fill ='red')
    return lst_points_x, lst_points_y

# # Traits du cercle


def traits(m, i):
    
    """Fonction qui va tracer les traits entre les differents points du cercle."""
    global lst_points_x
    global lst_points_y
    x_1 = lst_points_x[i] 
    y_1 = lst_points_y[i]  
    x_2 = lst_points_x[m] 
    y_2 = lst_points_y[m] 
    trait = canvas.create_line(x_1, y_1, x_2, y_2)


def mult_mod(n, p):
    
    """Fonction qui effectue le calcul de la multiplication modulaire et rejoint 
        les differents points."""
    
    for i in range(p):  
        m = n * i
        if m >= p :
            while m >= p :
                m = m - p
        traits(m, i)  # fonction qui trace les traits


def modulo():
    
    """Fonction qui calcule la table de a de 0 a n modulo p. Cette fonction 
        fait appel aux fonctions 'traits' et 'points'. """
        
    espaces = ' ' * 55
    Label(root, text=espaces).grid(row=0, column=2)
    Label(root, text=espaces).grid(row=1, column=2)
    
    generation_possible = True
    
    if not re.match("([0-9 ])", case_1.get()):
       label_table_non_entier = Label(root, text="la table doit etre un entier", bg="red", fg="white")
       label_table_non_entier.grid(row=0, column=2)
       generation_possible = False
    
    if not re.match("([0-9 ])", case_2.get()):
       label_modulo_non_entier = Label(root, text="le modulo doit etre un entier", bg="red", fg="white")
       label_modulo_non_entier.grid(row=1, column=2)
       generation_possible = False
       
    if generation_possible :
        n = int(case_1.get())  # la table
        p = int(case_2.get())   # le modulo
        global n_1 
        global p_1 
        
        if p>=p_1 :
            for mod in range(p_1, p + 1):
                canvas.delete("all")
                points(mod)  # place les points 
                mult_mod(n, mod)  # rejoint les points
                canvas.update()
                time.sleep(0.01)
        else: 
            diff = p_1 - p # La difference des deux modules
            for mod in range(1, diff+1):
                canvas.delete("all")
                points(p_1 -mod)  # place les points 
                mult_mod(n, p_1 - mod)  # rejoint les points
                canvas.update()
                time.sleep(0.01)
            
    
        n_1 = int(case_1.get())
        p_1 = int(case_2.get())

        return n, p



# # Creation des cases pour choisir les differentes valeurs
texte_1 = Label(root, text="table de : ")
texte_1.grid(row=0, column=0)

case_1 = Entry(root)
case_1.insert(END, "2")
case_1.grid(row=0, column=1)

texte_2 = Label(root, text="modulo : ")
texte_2.grid(row=1, column=0)

case_2 = Entry(root)
case_2.insert(END, "100")
case_2.grid(row=1, column=1)

boutton = Button(root, text="cliquez pour valider", command=modulo)  # en cliquant sur ce bouton on appele la fonction trait
boutton.grid(row=2, column=0)

root.mainloop()  # affiche la fenetre graphique'
