import random
random.seed()


tablica=[]

for i in range(0,10,1):
    losowana = random.randrange(10)
    tablica.append(losowana)
print(tablica)


def minimum(tab,a):
    m=10
    start=a
    for j in range (start,10,1):
        if (m>tab[j]):
            m=tab[j]
            mind=j
    return(m,mind)

def select(tablica):
    n=len(tablica)
    for i in range(0,9,1):
        m, x=minimum(tablica,i)
        if x!=i:
            temp=[]
            temp=tablica[i:x]
            tablica[i]=m
            tablica[i+1:x+1]=temp
    

select(tablica)
print(tablica)
    
