import time
start_time=time.time()
#n=int(input("podaj liczbę: "))
def sito_erast(n):
    pierwsze=[]
    wielokrot=[]
    for i in range(2,n+1):
        if i not in wielokrot:
            #print(i)
            pierwsze.append(i)
            for j in range(i,n+1,i):
                wielokrot.append(j)
    print(pierwsze)

sito_erast(100)
print("--- %s seconds ---" % (time.time() - start_time))
