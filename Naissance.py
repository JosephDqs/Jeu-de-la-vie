#Naissance est une fonction qui sert à dire si une cellule nait à un endroit ou non
from Environement import Environement
def Naissance(x,y,Listen,Listex,Listey,T,Xgrille,Ygrille):
    v = 1 
    n = len(Listen)
    e = Environement(x,y,T,Listex,Listey,Xgrille,Ygrille)# on cherche le nombres de cellules environnentes
    for i in range(n) : # on cherche si la valeure correspond à l'une des valeurs pour laquelle la cellule nait
        if e == Listen[i]:# si oui la cellule nait
            v = 1
            break # break et fin à la boucle
        else: # sinon la cellule de nait pas
            v = 0
    return v
    

#Listen=[3]
#Listex =[0,4,0,4,2,1,3,2]
#Listey =[0,0,4,4,3,2,1,2]
#Xgrille = 5
#Ygrille = 5
#n=len(Listev)
#print (Listex)
#print (Listey)
#T=int(input("T = ",))
#X=int(input("x = ",))
#Y=int(input("y = ",))

#N = Naissance(X,Y,Listen,Listex,Listey,T,Xgrille,Ygrille)
#print N 

