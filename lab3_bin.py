binarna=(input('Podaj binarna  '))
wynik=int(binarna[0])

print('liczba binarna: ', binarna)

for i in range (0,len(binarna)-1):
    wynik*=2
    #print(wynik)
    wynik+=int(binarna[i+1])

print ('liczba dziesietna: ',wynik)

binarna=[]
reszta=0
while(wynik>0):
    reszta=wynik%2
    print(reszta)
    binarna.append(reszta)
    wynik=wynik//2
binarna.reverse()
print("\n")
#print('liczba binarna: ',binarna)
print(binarna)
    
