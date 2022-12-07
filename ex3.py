#Exercice 3: Ecrire une fonction en Python pour trouver la somme des séries 1! / 1 + 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 en utilisant la fonction.
nombre = int(input("Entrer un nombre: "))
def factorielle (nombre):
    j=1
    for i in range (1,nombre+1):
        j=i*j
    return j           
def somme_serie(nombre):
    j=0
    for i in range (1,nombre+1):
        j+=factorielle(i)/i
    return j
print('la somme de la série est : ',somme_serie(5))    