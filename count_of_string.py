str1=input("enter the string")
count1=0
count2=0
for i in str1:
    if(i.islower( )):
        count1=count1+1
    elif(i.isupper( )):
        count2=count2+1   
print("the number of lowercase character is: ")
print(count1)
print("the number of uppercase character is: ")
print(count2)
