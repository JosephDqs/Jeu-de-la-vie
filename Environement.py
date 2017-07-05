#Environement est une fonction qui sert à déterminer le nombre de cellules environtes
from Recherche import Recherche
def Environement(x,y,T,Listex,Listey,Xgrille,Ygrille) :
    px=[x-1,x,x+1,x-1,x+1,x-1,x,x+1]# on crée 2 liste avec les coordonnées coorespodants à un rayon de 1 autour de la case 
    py=[y-1,y-1,y-1,y,y,y+1,y+1,y+1]
    if T == 1 : # Si le monde est en Tore
        for i in range(8):# on fait en sorte que si une coordonnée et < 1 alors elle devient égale à la longueur maximale de la liste et vis versa
            if px[i] > Xgrille-1 : 
                px[i] = 0
            if px[i] < 0 :
                px[i] = Xgrille-1
            if py[i] > Ygrille-1 :
                py[i] = 0
            if py[i] < 0 :
                py[i] = Ygrille-1
    #pour chaques cases on cherche si elle est pleine ou pas           
    p0 = int(Recherche(px[0],py[0],Listex,Listey))
    p1 = int(Recherche(px[1],py[1],Listex,Listey))
    p2 = int(Recherche(px[2],py[2],Listex,Listey))
    p3 = int(Recherche(px[3],py[3],Listex,Listey))
    p4 = int(Recherche(px[4],py[4],Listex,Listey))
    p5 = int(Recherche(px[5],py[5],Listex,Listey))
    p6 = int(Recherche(px[6],py[6],Listex,Listey))
    p7 = int(Recherche(px[7],py[7],Listex,Listey))
  
    return (p0+p1+p2+p3+p4+p5+p6+p7) # on renvoit le nombre trouvé

#Listex =[0,4,0,4,2,1]
#Listey =[0,0,4,4,3,2]
#Xgrille = 5
#Ygrille = 5
#print (Listex)
#print (Listey)
#T=int(input("T = ",))
#X=int(input("x = ",))
#Y=int(input("y = ",))

#e = Environement(X,Y,T,Listex,Listey,Xgrille,Ygrille)
#print (e)
