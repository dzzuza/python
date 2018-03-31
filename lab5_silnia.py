import time

def silniarek(n):
    suma=0
    for i in range(0,n+1):
        if(i==0):
            suma=1
        else:
            suma=silniarek(i-1)*i
    return suma

def silniait(n):
    suma=0
    x=0
   
    while(x<=n):
        if(x==0):
            suma=1
            x+=1
        else:
            suma=suma*x
            x+=1
    return suma

poczatek=time.time();
#silniarek(5)
print(silniarek(0))
print(' --- %s second ---' % (time.time()-poczatek))

poczatek=time.time();
#silniait(5)
print(silniait(3))
print(' --- %s second ---' % (time.time()-poczatek))
