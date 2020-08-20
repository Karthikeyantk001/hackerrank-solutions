from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
c=dict(Counter(arr))
for i in list(c.keys()):
    if c[i]==1:
        print(i)
        
#success
