import random
random.seed()

tablica=[]


for i in range(0,101,1):
    losowana = random.randrange(102)
    tablica.append(losowana)

print(tablica)


def babel(tablica):
    for i in range(100):
        for j in range (100):
            if (tablica[j]>tablica[j+1]):
                tmp=tablica[j]
                tablica[j]=tablica[j+1]
                tablica[j+1]=tmp
    return tablica

babel(tablica)

print(tablica)
