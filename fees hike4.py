start=int(input(start number))#5
end=int(input(end number))#10
for n in range(start,end+1):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break;
        else:
            print(n)