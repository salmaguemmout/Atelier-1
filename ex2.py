
#Exercice 2 : Ecrire une fonction python qui calcul la factorielle d’un nombre donné
nombre =int(input("Entrer un nombre: "))
def factorielle (nombre):
    j=1
    for i in range (1,nombre+1):
        j=i*j
    return j           
print('le factoriel du nombre %d est: '%nombre,factorielle(nombre))