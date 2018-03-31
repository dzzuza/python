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
def minimum(tab):
    min=10
    for j in range (0,10,1):
    #print('min',min)
        if (min>tab[j]):
            min=tab[j]
    return(min)

#print(minimum(tablica))

for i in range(0,9,1):
    k=i
    m=minimum(tablica)
    print('m',m)
    for j in range(i+1,10,1):
        print('t',tablica[i])
        print('i',i,'j',j)
        if(tablica[j]<tablica[i]):
            tmp=tablica[j]
            tablica[j]=tablica[i]
            tablica[i]=tmp
    print(tablica)
    print('\n')
#print(tablica)
    
    
