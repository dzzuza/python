import random
random.seed()


tablica=[]

for i in range(0,10,1):
    losowana = random.randrange(10)
    tablica.append(losowana)

print(tablica)

#for i in range(0,9,1):
    #print('it',i)

#for i in range (0,9,1):
##def minimum(tab):
##    min=10
##    for j in range (0,10,1):
##    #print('min',min)
##        if (min>tab[j]):
##            min=tab[j]
##    return(min)
##print(minimum(tablica))

##for k in range(10):
##        for j in range (i,10,1):
##            if(tablica[i]>tablica[j]):
##                print(i)
##                print(tablica[j])
##                tmp=tablica[j]
##                tablica[j]=tablica[i]
##                tablica[i]=tmp
##                print(tablica)
##                print('\n')
##                break

def insert(lista):
    for index in range(1,len(lista)):
        val=lista[index]
        i=index-1
        while i>=0:
            if val<lista[i]:
                lista[i+1]=lista[i]
                
                lista[i]=val
                i=i-1
            else:
                break
            
insert(tablica)
print(tablica)
