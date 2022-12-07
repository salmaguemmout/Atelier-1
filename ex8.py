#Exercice 8:Ecrire une fonction qui cherche un élément dans une matrice puis renvoi sa position «i,j».
m=int(input("Entrer le nombre de colonnes: "))
n=int(input("Entrer le nombre de lignes: "))
A=[]    
print('entrer les elements de la matrice:')    
for i in range(n):
    ligne=[]
    for j in range(m):
        print('A[%d,%d]'%(i+1,j+1),end=" ")
        ligne.append(int(input()))
    A.append(ligne)
print(A)
x=int(input("Entrer l element que vous recherchez: "))
def recherche(x):
    for i in range(n):
        for j in range(m):
            if x==A[i][j]:
                print('X[%d,%d]= '%(i+1,j+1),x)
                print('le %d est de position : < %d en lignes > et < %d en colonnes >'%(x,i+1,j+1))
recherche(x)