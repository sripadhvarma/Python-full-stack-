def printfact(a):
    for i in range(1,int(a**0.5)+1):
        if(a%i==0):
            print(i,end=" ")
            if(i!=a//i):
                print(a//i)
n=int(input())
printfact(n)