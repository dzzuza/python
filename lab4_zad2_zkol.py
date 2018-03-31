import random
import time

width=11
height=7
waz=[]

for k in range (0,width//2):
    for i in range (0,height):
        wiersz=' '
        for j in range (0, width):
            if(i<=k-1 or j<=k-1 or j>=(width-k) or i>=(height-k)):
                wiersz+=('x  ')
            else:
                wiersz+='o  '
        print(wiersz)
        print('\n')
    print('\n'*3)
print('trututu')
for k in range (0,width//2-1):
    for i in range (0,height):
        wiersz=' '
        for j in range (0, width):
            if(i<=k or j<=k or j>=(width-k-1) or i>=(height-k-1)):
                wiersz+=('o  ')
            else:
                wiersz+='x  '
        print(wiersz)
        print('\n')
    print('\n'*3)
