#Exercice 9:Ecrire un programme python composé de plusieurs fonctions
List=[]
b=int(input("Entrer la longeur de la liste: "))
for i in range (b):
    x=int(input("Entrer le nombre %d : "%(i+1)))
    List.insert(i,x)
def moyenne(List):
    somme=0
    for i in range (len(List)):     
        somme+=List[i]
        moyenne=somme/len(List)
    print('la moyenne de la liste est: ',moyenne)
def min_max(List):
    print(List) 
    def max(List):
        for i in range (1,len(List)):
            if List[i-1] > List[i]:
                temp=List[i-1]
                List[i-1]=List[i]
                List[i]=temp
        print('le maximum est: ',List[-1])
        return List[-1]
    def min(List):  
        for i in range (1,len(List)):
            if List[i-1] < List[i]:
                temp=List[i-1]
                List[i-1]=List[i]
                List[i]=temp
        print(List)           
        print('le maximum est: ',List[-1])   
        return List[-1]
    print('choix 1 : Calculer le maximum')
    print('choix 2 : Calculer le minimum')
    choix=int(input('Entrer le choix : '))
    if choix==1:
        max(List)             
    elif choix==2:
        min(List)   
def mediane(List):
    for i in range (1,len(List)):
        if List[i-1] > List[i]:
            temp=List[i-1]
            List[i-1]=List[i]
            List[i]=temp
            print(List[i])
    print(List)
    rang=(b+1)/2
    if rang%2==0:
        rang=int((b+1)/2)
        me=List[rang-1]
    else:
        rang=int((b+1)/2)
        me=(List[rang-1]+List[rang])/2
    print('la médiane de la liste est : ',me)    
def mode(List):
    #effectifs corrigés
    print('le mode de la liste est: ',max(List))
print('*********** MENU ***********')
print('1:calculer la moyenne de la série.')
print('2:calculer le minimum ou le maximum de la liste.')
print('3:calculer la médiane de la liste.')
print('4:calculer le mode de la liste.')
menu=int(input("choisir un numéro du menu: "))
if menu==1:
    moyenne(List)
elif menu==2:      
    min_max(List)
elif menu==3: 
    mediane(List)
elif menu==4: 
    mode(List)
else:
    print("le nombre que vous avez choisi n'est pas valide veuillez réessayez." )