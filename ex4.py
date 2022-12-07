#Exercice4:Ecrire une fonction en Python pour convertir le nombre décimal en nombre binaire
n = int(input("entrer un nombre :"))
b = 0
ord = 0
while n != 0:
    reste = n % 2 
    p = 10 ** ord 
    b = b + reste * p
    ord = ord +1
    n = n // 2
    
print(b) 
