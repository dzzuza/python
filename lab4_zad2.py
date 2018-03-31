import random
import time

width=11
height=7
if height<width:
    a=height//2+1
else:
    a=width//2+1

for k in range (0,a):
    for i in range (0,height):
        wiersz=' '
        for j in range (0, width):
            if((i==height//2-k) and (j>=width//2-k and j<=width//2+k) or i==height//2+k and (j>=width//2-k and j<=width//2+k) or j==width//2+k and (i>=height//2-k and i<=height//2+k)or j==width//2-k and (i>=height//2-k and i<=height//2+k)):
                wiersz+=('x  ')
            else:
                wiersz+='o  '
        print(wiersz)
    print('\n')
##    print('\n'*3)
##print('trututu')
for k in range (a-2,-1,-1):
    for i in range (0,height):
        wiersz=' '
        for j in range (0, width):
            if((i==height//2-k) and (j>=width//2-k
                                     and j<=width//2+k) or i==height//2+k
               and (j>=width//2-k and j<=width//2+k) or j==width//2+k and (i>=height//2-k
                                                                           and i<=height//2+k)or j==width//2-k
               and (i>=height//2-k and i<=height//2+k)):
                wiersz+=('x  ')
            else:
                wiersz+='o  '
        print(wiersz)
    print('\n')
##    print('\n'*3)

