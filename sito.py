import time
start_time=time.time()
def erasto(n):
	multiples=[]
	prim=[]
	for i in range (2,n+1):
		if i not in multiples:
			#print(i)
			prim.append(i)
			for j in range(i*i,n+1,i):
				multiples.append(j)
	return(prim)

erasto(1000)

print (time.time() - start_time)
