n=int(input("n"))
print(n)

for z in range(1,n):
  #choinka=('')
  for y in range(1+z):
    for z in range(1+y):
      print("*",end=" ")
    print("")


for i in range(1,n+1):
  for j in range(0,i+1):
    choinka=''
    for k in range(2*n+1):
      if(k<n-j or k>n+j):
        choinka+=('o')
      else:
        choinka+=('x')      
    print(choinka)
