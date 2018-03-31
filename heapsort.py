import random
import math
random.seed()
lista=[]
for i in range(0,10):
        lista.append(random.randrange(10))

def heapify(lista,start,end):
        parent=start
        while True:
                child=parent*2+1
                if child>end:
                        break
                if child+1<=end and lista[child]<lista[child+1]:
                        child=child+1
                if(lista[parent]<lista[child]):
                        lista[parent],lista[child]=lista[child],lista[parent]
                        parent=child
                else:
                        break

def heapSort(lista):
  for i in range(math.floor((len(lista)/2-1)),-1,-1):
    heapify(lista,i,len(lista)-1) #builtheap
  for j in range (len(lista)-1,-1,-1):
    lista[j],lista[0]=lista[0],lista[j]#swaps firstand last node
    heapify(lista,0,j-1)#creates max heap on reduced array
  return lista
print(lista)
heapSort(lista)
print(lista)                
                
