def printfact(a):
    if(n<=1):
        print("neither prime nor composite")
    count=0
    for i in range(1,int(a**0.5)+1):
        if(a%i==0):
            count+=1
            if(i!=a//i):
                count+=1
    if count==2:
        print("prime")
    if count>2:
        print("not prime")
n=int(input())
printfact(n)