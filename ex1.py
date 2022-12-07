#Exercice 1 :Ecrire une fonction qui renvoie la puissance d’un nombre Xn
x=int(input("Entrer un nombre: "))
n=int(input("Entrer la puissance: "))
def puissance(x,n):
    for i in range (1,n):
        x*=x
    return x
print('le résultat du nombre %d à la puissnce %d est: '%(x,n),puissance(x,n))