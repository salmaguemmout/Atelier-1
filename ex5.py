#Exercice 5:Ecrire une fonction en Python pour calculer la somme des nombres de 1 à n
var=int(input("Entrer un nombre: "))
def somme(var):
    j=0
    for i in range (var+1):
        j+=i
    return j

print('la somme des nombres de 1 à %d est: '%var,somme(var))