import random
random.seed()


tablica=[]

for i in range(0,100,1):
    losowana = random.randrange(100)
    tablica.append(losowana)

print(tablica)

for i in range(99):
    for j in range (99):
        if (tablica[j]>tablica[j+1]):
            tmp=tablica[j]
            tablica[j]=tablica[j+1]
            tablica[j+1]=tmp

print(tablica)
