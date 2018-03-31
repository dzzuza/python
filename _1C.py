#ZADANIE 1
n=7

def fibo_rek(n):
    sum_fib=0
    for i in range(0,n+1,1):
        if(i==0):
            sum_fib=0
        if(i==1):
            sum_fib=1
        else:
            sum_fib= fibo_rek(i-1)+fibo_rek(i-2)
    return sum_fib

#print(fibo_rek(n))

def fibo_it(n):
    sum_fib=0
    i=0
    while(i<=n):
        if(i==0):
            sum_fib=0
            a=sum_fib
            i+=1
        elif(i==1):
            sum_fib=1
            b=sum_fib
            i+=1
        else:
            sum_fib=a+b
            a=b
            b=sum_fib
            i+=1
    return sum_fib

print(fibo_it(n))
        
#ZADANIE 3
days = ["poniedzialek","wtorek","sroda","czwartek","piatek","sobota","niedziela"]
months = ["sty","lut","marz","kwi","maj","czerw","lip","sierp","wrze","paz","lis","gru"]
month1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
month2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
month3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
month4 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
years = [2016,2017,2018,2019,2020,2021,2022,2023,2024,2025]

print("Piatki trzynastego w latach 2016-2025")
#month = "sty"
z = 4
day = days[z]
#year = 2017
print(day)
 
for year in years:
    if(year%4!=0):
        #print(year)
        for month in months:
            if (month=="sty" or month=="marz" or month=="maj" or month=="lip" or month=="sierp" or month =="paz" or month=="gru"):
                #print('m',month)
                for i in month1:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z += 1
                    if (i==13 and day == "piatek"):
                        print(str(year)+str(month))
                
            if (month=="kwi" or month=="czerw" or month=="wrze" or month=="lis"):
                #print('m',month)
                for j in month2:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z += 1
                    if (j==13 and day == "piatek"):
                        print(str(year)+str(month))
            if (month=="lut"):
                #print('m',month)
                for k in month3:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z +=1
                    if (k==13 and day == "piatek"):
                        print(str(year) + str(month))
    #print(day)
    if(year%4==0):
        #print(year)
        for month in months:
            if (month=="sty" or month=="marz" or month=="maj" or month=="lip" or month=="sierp" or month =="paz" or month=="gru"):
                #print('m',month)
                for i in month1:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z += 1
                    
                    if (i==13 and day == "piatek"):
                        print(str(year)+str(month))
                
            if (month=="kwi" or month=="czerw" or month=="wrze" or month=="lis"):
                #print('m',month)
                for j in month2:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z += 1
                    #print(day)
                    if (j==13 and day == "piatek"):
                        print(str(year)+str(month))
            if (month=="lut"):
                #print('m',month)
                for k in month4:
                    day = days[z]
                    if (z == 6):
                        z = 0
                    else:
                        z +=1
                    if (k==13 and day == "piatek"):
                        print(str(year) + str(month))






