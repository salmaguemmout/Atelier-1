#Exercice 6:Ecrire une fonction en Python pour compter les chiffres d'un nombre donné.
b=input("Entrer un nombre: ")
def chifffre(b):
    j=0
    for i in range (len(b)):
        j+=1
    return j
print('le chiffre du nombre ',b,' est:',chifffre(b))