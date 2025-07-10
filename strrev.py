a=[1,2,3,4,5]
i,j=0,len(a)-1
while(i<j):
    a[i],a[j]=a[j],a[i]
    i+=1
    j-=1
print(a)
