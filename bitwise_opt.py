n=int(input("enter no.of choices:"))
for i in range(1,11):
    num=int(input("enter value:"))
    if(num==n):
        print("you guessed it right!!")
        break
    else:
        print("try again")
print("Sorry your limit is finished.")