import random
import math
random.seed()
lista=[]

for i in range(0,10):
        lista.append(random.randrange(10))
print(lista)

def quicksort(lista,start,end):
    pivot=lista[(start+end)//2]
    print('piv',pivot)
    left=start
    right=end
    while(left<=right):
        while(lista[left]<pivot):
            left+=1
        while(lista[right]>pivot):
            right-=1
        if(left<=right):
            lista[left],lista[right]=lista[right],lista[left]
            left+=1
            right-=1
    print(lista)
    if(start<right):
        quicksort(lista,start,right)
    if(end>left):
        quicksort(lista,left,end)
quicksort(lista,0,len(lista)-1)
print(lista)
