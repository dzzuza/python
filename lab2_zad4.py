import time
start_time=time.time()
n=100
multi=[]
for i in range (2,n+1):
	if i not in multi:
		print(i)
		for j in range (i*i,n):
			if (j%i==0):
				multi.append(j)
print("--- %s seconds ---" % (time.time() - start_time))
