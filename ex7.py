#Exercice 7: Ecrire une fonction Python pour trouver la fréquence d’un caractère dans une chaîne.
List=[]
x=input("Entrer une chaîne de caractères: ")
b=input("Entrer un caractère: ")
def frequence(b):
    A=0
    for i in range (len(x)):     
        List.insert(i,x[i])
    print(List)
    for i in range (len(List)):
        if b==List[i]:   
            A=A+1 
    if A>0:
        print('le caractère %s se répète %d fois dans la chaîne < %s >'%(b,A,x))
    else:
        print('le caractère %s ne se trouve pas dans la chaîne'%b)  
frequence(b)