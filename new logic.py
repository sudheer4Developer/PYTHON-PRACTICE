num=int(input("enter the number"))
count=len(str(num))
temp=num
sum=0
while(num!=0):
    rem=num%10
    sum=sum+rem**count
    num=num//10
if temp==sum:
    print("it is amstrong")
else:
    print("it is not an amstrong")
    