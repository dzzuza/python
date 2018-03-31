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
def build_heap(lista):
        for start in range(math.floor((len(lista)-2)/2),-1,-1):
                heapify(lista,start,len(lista)-1)
                print(lista)
                print('\n')
        return lista
def heap_sort(lista):
        build_heap(lista)
        for i in range(len(lista)-1,0,-1):
                lista[i],lista[0]=lista[0],lista[i]
                heapify(lista,0,i-1)
                print(lista)
        return lista
print(lista)
print('---')
print(build_heap(lista))
print('---')
heap_sort(lista)
print('---')
