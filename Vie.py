#La fonction Vie sert à vérifier si la cellule est vivante ou non.
from Environement import *

def Vie(x,y,Listev,Listex,Listey,T,Xgrille,Ygrille):

    v = 1
    n = len(Listev)
    e = Environement(x,y,T,Listex,Listey,Xgrille,Ygrille) # on cherche le nombre de cellules environnentes
    for i in range(n) : # on va chercher si le nombre de cellule environnentes correspont à l'une des valeurs valides
        if e == Listev[i]: # si oui la cellule vit
            v = 1
            break # break sert à sortir de la boucle instantanement
        else: # Sinon la cellule meurt
            v = 0
    return v #on renvoit si oui ou non la cellule est vivante
    

#Listev=[2,3]
#Listex =[0,4,0,4,2,1]
#Listey =[0,0,4,4,3,2]
#Xgrille = 5
#Ygrille = 5
#n=len(Listev)
#print (Listex)
#print (Listey)

#X=int(input("x = ",))
#Y=int(input("y = ",))

#v = Vie(X,Y,Listev,Listex,Listey,T,Xgrille,Ygrille)
#print v 

