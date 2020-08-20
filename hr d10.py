
n=int(input())
b=list(bin(n)[2:])
b.append("_")
arr=[1]

for i in range(len(b)):
    c=1
    if b[i]=="1":
        while (b[i+1]=="1" and i<len(b)):
            c+=1;
            i+=1;

            arr.append(c)
print(max(arr))
#successsssss
