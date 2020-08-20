n=int(input())
num=[]
for i in range(n):
    num.append(str(input()))
i=0
while (i<n):
    if len(num[i])==10:
      f=num[i]
      j=f[0]
      if(j=='9' or j=='8' or j=='7'):
        print("YES")
    else:
        print("NO")
    i+=1
