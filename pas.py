def pascal(n,k):
    if(k==n or k==0):
        return 1
    else:
        return pascal(n-1,k-1)+pascal(n-1,k)

##print(pascal(5,2))

n=5
for i in range(n):
    wiersz=""
    for j in range (i+1):
        wiersz=wiersz+str(pascal(i,j))+"\t"
    print(wiersz)
