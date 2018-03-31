import random
random.seed()
lista=[]

for i in range(0,10):
        lista.append(random.randrange(100))
print(lista)
print('----')
def insert(lista):
    for i in range (1,10):
        index =i
        value = lista[i]
        while index>0 and lista[index-1]>value:
            lista[index],lista[index-1]=lista[index-1],lista[index]
            index=index-1
insert(lista)
print(lista)
