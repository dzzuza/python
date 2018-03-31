import random
import time

w=7
h=5
waz=[]

random.seed()

for i in range(0,h):
    poz=random.randint(0,w-1)
    waz.insert(0,poz)
    print(waz)
    for j in range(0,h):
        wiersz=''
        for k in range(0,w):
##            if(i==j and k==waz[i]):
##                wiersz+='x'
            if(j==0 and k==waz[0]):
                wiersz+='x'
            if(j<=i and j!=0 and k==waz[j]):
                wiersz+='x'
            else:
                wiersz+='o'
        print(wiersz)
        print('\n')
    time.sleep(0.3)
    print('\n' *3)
