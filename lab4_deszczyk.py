import random
import time

width=11
height=7
waz=[]


random.seed()



for k in range(0,height):
    a=random.randint(0,width-1)
    waz.insert(0,a)
    print(waz)
    for i in range (0, height):
        wiersz=' '
        for j in range (0,width):
            if(i<=k and j==waz[i]):
                wiersz+='x'
            else:
                wiersz+='o'
        print(wiersz)
    print('\n')
    time.sleep(0.3)
    print('\n' *3)

