import time

def fibo_rek(n):
    suma=0
    for i in range(0,n+1):
        if(i==0):
            suma=0
        elif(i==1):
            suma=1
        else:
            suma=fibo_rek(i-1)+fibo_rek(i-2)
    return suma


def fibo_it(n):
    suma=0
    i=0
    while(i<=n):
        if(i==0):
            suma=0
            i+=1
            a=suma
        elif(i==1):
            suma=1
            i+=1
            b=suma
        else:
            suma=a+b
            a=b
            b=suma
            i+=1
    return suma

poczatek=time.time();
print(fibo_it(7))
print(' --- %s second ---' % (time.time()-poczatek))

poczatek=time.time();
print(fibo_rek(3))
print(' --- %s second ---' % (time.time()-poczatek))


