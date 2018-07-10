#param1=(int(input('Podaj:  ')))
matrix=[]

file =open("file.txt","r")
matrix=[line.split() for line in file]
matrix=[[float(d) for d in i]for i in matrix]

