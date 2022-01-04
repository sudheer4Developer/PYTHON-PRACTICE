str=("english=78 science=83 math=68 history=65")
st=str.split()
sum=0
for i in range(4):
    print(st[i])
    sub=st[i]
    sum=sum+int(sub[-2:])
print("sum: ",sum)
print("avg: ",sum/4)