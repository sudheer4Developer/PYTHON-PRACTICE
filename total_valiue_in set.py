str=input("enter the string: ")
acount=0
dcount=0
scount=0
for ch in str:
    if ch>"a" and ch<="z" or ch>="A" and ch<="Z":
        acount=acount+1
    elif ch>="0" and ch<="9":
        dcount=dcount+1
    elif ch!=" ":
        scount=scount+1
print("number of alphabets: ",acount)
print("number of digits: ",dcount)
print("number of spacial characters: ",scount)
    
    
    