#On importe nos fonctions puis les bibliothèques 
from Vie import *
from Naissance import *
from Recherche import *
from tkinter import *
from math import *
from random import *
######

#On définit les fonctions pour les cases cochables
def cocheV0():
  if v0.get() == 1 :
    Listev.append(0)
  elif v0.get()==0 :
    Listev.remove(0)
def cocheV1():
   if v1.get()==1 :
    Listev.append(1)    
   elif v1.get()==0 :
    Listev.remove(1)
def cocheV2():
  if v2.get()==1 :
    Listev.append(2)
  elif v2.get()==0 :
    Listev.remove(2)
def cocheV3():
  if v3.get()==1 :
    Listev.append(3)
  elif v3.get()==0 :
    Listev.remove(3)
def cocheV4():
  if v4.get()==1 :
    Listev.append(4)
  elif v4.get()==0 :
    Listev.remove(4)
def cocheV5():
  if v5.get()==1 :
    Listev.append(5)
  elif v5.get()==0 :
    Listev.remove(5)
def cocheV6():
  if v6.get()==1 :
    Listev.append(6)
  elif v6.get()==0 :
    Listev.remove(6)
def cocheV7():
  if v7.get()==1 :
    Listev.append(7)
  elif v7.get()==0 :
    Listev.remove(7)
def cocheV8():
  if v8.get()==1 :
    Listev.append(8)
  elif v8.get()==0 :
    Listev.remove(8)
##############################################################
def cocheN0():
  if n0.get() == 1 :
    Listen.append(0)
  elif n0.get()==0 :
    Listen.remove(0)
def cocheN1():
   if n1.get()==1 :
    Listen.append(1)    
   elif n1.get()==0 :
    Listen.remove(1)
def cocheN2():
  if n2.get()==1 :
    Listen.append(2)
  elif n2.get()==0 :
    Listen.remove(2)
def cocheN3():
  if n3.get()==1 :
    Listen.append(3)
  elif n3.get()==0 :
    Listen.remove(3)
def cocheN4():
  if n4.get()==1 :
    Listen.append(4)
  elif n4.get()==0 :
    Listen.remove(4)
def cocheN5():
  if n5.get()==1 :
    Listen.append(5)
  elif n5.get()==0 :
    Listen.remove(5)
def cocheN6():
  if n6.get()==1 :
    Listen.append(6)
  elif n6.get()==0 :
    Listen.remove(6)
def cocheN7():
  if n7.get()==1 :
    Listen.append(7)
  elif n7.get()==0 :
    Listen.remove(7)
def cocheN8():
  if n8.get()==1 :
    Listen.append(8)
  elif n8.get()==0 :
    Listen.remove(8)
##############################################################
def Tore():
  if T0.get()==1:
    T.append(1)
    if len(T)>1:
      T.remove(0)
  elif T0.get()==0:
    T.append(0)
    if len(T)>1:
      T.remove(1)

     


#On définit différentes fonctions
#################################################################################
def Cycle(): #Fonction permettant de faire passer un cycle
    Lx =[] #On définit les objets Lx et Ly comme étant des listes
    Ly =[]
    for y in range(0,20):
        for x in range(0,20): # Pour chaques cases de la grille
            b = Recherche(x,y,Listex,Listey) # On vérifie si cette cellule est remplie
            if b == 1: # Si oui
                a = Vie(x,y,Listev,Listex,Listey,T[0],19,19) # On vérifie si la cellule survit au prochain cycle
            else : # si non
                a = Naissance(x,y,Listen,Listex,Listey,T[0],19,19)# On vérifie si une cellule va naître ici au prochain cycle
            if a == 1:# Si au prochain cycle la case est rempli
                Lx.append(x) # On enregistre ses coordonnées
                Ly.append(y)
    Listex[:]=[]#On vide les listes (listex et listey) contenants les coordonnées précédentes
    Listey[:]=[]
    for i in range(0,len(Lx)): #On les remplis avec les coordonnées des cellules du cycle suivant
         Listex.append(Lx[i])
         Listey.append(Ly[i])
########################################################################################
def Leave(): # action du bouton "exit"
  if G == 1:
    interf.destroy()
  Menu.destroy()
########################################################################################
def rectangle(Listex,Listey,can1):#Fonction permettant de remplir une case
    n = len(Listex)
    for i in range(0,len(Listex)):#pour toutes les coordonnées enregistré
         x, y = Listex[i]*20,Listey[i]*20    
         can1.create_rectangle(x, y, x+20, y+20, fill='green')# on crée un carré à la position désiré 
def RectangleVert(x,y,can1):
    can1.create_rectangle(x, y, (x+20), (y+20), fill='green')      #on créé le rectangle Vert
def RectangleBlanc(x,y,can1):
    can1.create_rectangle(x, y, (x+20), (y+20), fill='white')      #on créé le rectangle Blanc
    

#########################################################################################
         
def Grille ():#Fonction ouvrant la fenetre de la grille

    def Pause():
        global p
        p=0
    def Jeu ():
        global p
        if p ==0:
          p=1
          Suivant()
    def change_vit(event): #fonction pour changer la vitesse(l'attente entre chaque cycles)
        global v
        v = int(eval(entree.get()))
        
      
    def Suivant ():#Fonction permettant de mettre à jour la grille
        if p == 1 :
            can1.create_rectangle(0,0,400,400, fill='white')# on efface la grille actuelle
            damier(can1) # On recrée une grille
            Cycle() #On lance la fonction Cycle
            rectangle(Listex,Listey,can1)        
            interf.after(v,Suivant)
            # On remplis les cases qui doivent l'être
    def envoyercoordonnees(event): #Fonction permettant de créer des cellules soit même
        x=int(event.x)
        y=int(event.y)
        x, y=x/20, y/20             #on divise par 20
        x, y=floor(x), floor(y)     #on arrondit à l'unité inférieure
        a = RechercheR(x,y,Listex,Listey)
        if x <20 and y <20 : # sécurité pour éviter des cases qui se constuisent à des endroits non désirés
            if a >=0 :#Si la cellule existe déjà
                del Listex[a]# On la supprime 
                del Listey[a]
                RectangleBlanc(x*20,y*20,can1)
            else : #sinon
                Listex.append(x) #On l'ajoute
                Listey.append(y)
                RectangleVert(x*20,y*20,can1)

    
    def damier(can1):# fonction créant la grille
        c_x=0
        c_y=0
        while c_x!=w:
            can1.create_line(c_x,0,c_x,h,w=1,fill='black') # on crée nos lignes verticales
            c_x+=tc
        while c_y!=h:
            can1.create_line(0,c_y,w,c_y,w=1,fill='black') # on crée nos lignes horizontales
            c_y+=tc
######
    #Variables            
    G = 1
        ##Taille de la grille
    h=400
    w=400
        ##Taille des cellules    
    tc=20
    #fonctions
        
        ##dessin tableau
    global p
    global interf
    global Can1
    global v,V
    p = 0
    v = 100
    interf = Tk()
    interf.geometry("500x500+50+80")
    interf["bg"]=["white"]
    can1 = Canvas(interf,width=w,height=h,bg ='white')
    can1.pack(side =TOP, padx =5, pady =5)
    damier(can1)
    can1.bind("<Button-1>", envoyercoordonnees)
    rectangle(Listex,Listey,can1)
    ########################  Menu avec les boutons
    option= Frame(interf,width=400,height=200)
    option.pack(side=TOP,padx =5,pady=5, )
    Play = Button(option,text="Play",fg="blue",command=Jeu)
    Play.pack(side=LEFT)
    Stop = Button(option,text="Pause",fg="blue",command=Pause)
    Stop.pack(side=LEFT)
    TextV = Label(option)#on crée un text dans option
    TextV.configure(text = "Vitesse(ms):") 
    TextV.pack(side=LEFT)
    entree = Entry(option) # on crée un champ de saisie
    entree.bind("<Return>", change_vit)# quand on appuie sur la touche "entrée", on lance la fonction "change_vit"
    entree.pack(side =LEFT)
    #######################
    can1.mainloop()

    
#####
#On définit les objets suivant comme étant globales.    
global Listen,Listev 
global T,G         
global Listex, Listey
global v0,v1,v2,v3,v4,v5,v6,v7,v8,n0,n1,n2,n3,n4,n5,n6,n7,n8,T0
Listen = [3] #Liste des valeurs pour lesquelles une nouvelle cellule nait.
Listev = [2,3] #Liste des valeurs pour lesquelles une cellule survit.
T = [0] #Monde en Tore ou non        
Listex=[] #Liste de toutes les abscisses des cellules remplies
Listey=[] #Liste de toutes les ordonnées des cellules remplies
G = 0

#####
#Fonction permettant d'avoir des valeurs aléatoires

for i in range (0,120):
  v = 1
  while v==1:
     v = 0
     a = int(random()*10+random()*10)
     b = int(random()*10+random()*10)
     v = Recherche(a,b,Listex,Listey)
     Listex.append(a) 
     Listey.append(b)
     if v ==1:
       Listex.remove(Listex[i])
       Listey.remove(Listey[i])
######
                

Menu=Tk()
Menu.geometry("300x248+500+200")
Menu["bg"]=["blue"]
Menu.title("ZeLife!")
menu= Frame(Menu,width=100,height=200)#on crée dans notre fenêtre une "sous-fenetre" ayant des attributs différents de la fenêtre principale
menu.pack(side=LEFT)
Go=Button(menu, text="GO!", fg="Black", bg="Green", command=Grille)
Go.pack(side=LEFT)
Exit=Button(menu, text="Exit", fg="Black", bg="brown", command=Leave)
Exit.pack(side=LEFT)
T0= IntVar()
Tore0 = Checkbutton(menu, text = "TORE ?", variable = T0,command=Tore,bg="Green",fg="black")
Tore0.pack(side=LEFT,padx =1, pady =0)
#Menu avec les règles
RegleNaissance = Frame(Menu, width=100, height=200,bg="green")
RegleNaissance.pack(side=RIGHT)
RegleVie = Frame(Menu, width=100, height=200,bg="green")
RegleVie.pack(side=RIGHT)
####
TitreV=Label(RegleVie,text="   VIE   ",bg="red")
TitreV.pack(side=TOP)
####
v0= IntVar() # on définie cette valeur comme une variable
Vie0 = Checkbutton(RegleVie, text = "0", variable = v0,command=cocheV0,bg="green") # on dit que la variable v0 correspond à l'état de la case Vie0
Vie0.pack(side=TOP,padx =1, pady =0) # on colle Vie0 en haut de la frame "RegleVie"
#####
v1= IntVar()
Vie1 = Checkbutton(RegleVie, text = "1", variable = v1,command=cocheV1,bg="green")
Vie1.pack(side=TOP)
#####
v2= IntVar()
Vie2 = Checkbutton(RegleVie, text = "2", variable = v2,command=cocheV2,bg="green")
Vie2.pack(side=TOP)
Vie2.select()
#####
v3= IntVar()
Vie3 = Checkbutton(RegleVie, text = "3", variable = v3,command=cocheV3,bg="green")
Vie3.pack(side=TOP)
Vie3.select()
#####
v4= IntVar()
Vie4 = Checkbutton(RegleVie, text = "4", variable = v4,command=cocheV4,bg="green")
Vie4.pack(side=TOP)
#####
v5= IntVar()
Vie5 = Checkbutton(RegleVie, text = "5", variable = v5,command=cocheV5,bg="green")
Vie5.pack(side=TOP)
#####
v6= IntVar()
Vie6 = Checkbutton(RegleVie, text = "6", variable = v6,command=cocheV6,bg="green")
Vie6.pack(side=TOP)
#####
v7= IntVar()
Vie7 = Checkbutton(RegleVie, text = "7", variable = v7,command=cocheV7,bg="green")
Vie7.pack(side=TOP)
#####
v8= IntVar()
Vie8 = Checkbutton(RegleVie, text = "8", variable = v8,command=cocheV8,bg="green")
Vie8.pack(side=TOP)
##########################################################
TitreN=Label(RegleNaissance,text="NAISSANCE",bg="red")
TitreN.pack(side=TOP)
#####
n0= IntVar()
Naissance0 = Checkbutton(RegleNaissance, text = "0", variable = n0,command=cocheN0,bg="green")
Naissance0.pack(side=TOP,padx =1, pady =0)
#####
n1= IntVar()
Naissance1 = Checkbutton(RegleNaissance, text = "1", variable = n1,command=cocheN1,bg="green")
Naissance1.pack(side=TOP,padx =1, pady =0)
#####
n2= IntVar()
Naissance2 = Checkbutton(RegleNaissance, text = "2", variable = n2,command=cocheN2,bg="green")
Naissance2.pack(side=TOP,padx =1, pady =0)
#####
n3= IntVar()
Naissance3 = Checkbutton(RegleNaissance, text = "3", variable = n3,command=cocheN3,bg="green")
Naissance3.pack(side=TOP,padx =1, pady =0)
Naissance3.select()
#####
n4= IntVar()
Naissance4 = Checkbutton(RegleNaissance, text = "4", variable = n4,command=cocheN4,bg="green")
Naissance4.pack(side=TOP,padx =1, pady =0)
#####
n5= IntVar()
Naissance5 = Checkbutton(RegleNaissance, text = "5", variable = n5,command=cocheN5,bg="green")
Naissance5.pack(side=TOP,padx =1, pady =0)
#####
n6= IntVar()
Naissance6 = Checkbutton(RegleNaissance, text = "6", variable = n6,command=cocheN6,bg="green")
Naissance6.pack(side=TOP,padx =1, pady =0)
#####
n7= IntVar()
Naissance7 = Checkbutton(RegleNaissance, text = "7", variable = n7,command=cocheN7,bg="green")
Naissance7.pack(side=TOP,padx =1, pady =0)
#####
n8= IntVar()
Naissance8 = Checkbutton(RegleNaissance, text = "8", variable = n8,command=cocheN8,bg="green")
Naissance8.pack(side=TOP,padx =1, pady =0)
#####
Menu.mainloop()

#Diffusion de copies interdites, réservé à l'usage personnel, modification non-autorisé, tout droits réservés à L.Devillers et J.Desquaires


