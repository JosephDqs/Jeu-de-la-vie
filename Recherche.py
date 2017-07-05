#Recherche est une fonction permettant de vérifier si une case est rempli ou pas
def Recherche(X,Y,Listex,Listey) :
    n = len(Listex)
    i = 0  
    #On compare les coordonnées entrées avec chaques coordonnées de nos 2 listes
    while i < n and (X!= Listex[i] or Y!= Listey[i]):  
        i = i + 1 # la boucle s'arrete soit si les coordonnées correspondent à des coordonnées présentent dans les listes
        #soir si on a comparé avec tout les termes de la liste
    if i < n:
      return(1) #si la boucle s'est arrété avant de faire le tour des listes on renvoit 1
    else :
      return (0)#et vis versa
def RechercheR(x,y,Listex,Listey): # Cette fonction va servir pour les clics
    n = len(Listex)
    i = 0  
    #On compare les coordonnées entrées avec chaques coordonnées de nos 2 listes
    while i < n and (x!= Listex[i] or y!= Listey[i]):  
        i = i + 1 # la boucle s'arrete soit si les coordonnées correspondent à des coordonnées présentent dans les listes
        #soir si on a comparé avec tout les termes de la liste
    if i < n:
      return(i) #si la boucle s'est arrété avant de faire le tour des listes on renvoit 1
    else :
      return (-1)#et vis versa
    
#Listex =[]
#Listey =[]

#Listex =[0,4,0,4,2,1]
#Listey =[0,0,4,4,3,2]

#print (Listex)
#print (Listey)
#T=int(input("T = ",))
#X=int(input("x = ",))
#Y=int(input("y = ",))
#g = Recherche(X,Y,Listex,Listey)
#print (g)
