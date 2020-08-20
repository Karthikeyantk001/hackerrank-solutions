a1=set(input().split())
c=0
n=int(input())
for i in range(n):
    a2=set(input().split())
    if len(a1)>len(a2):
        if a2.union(a1)==a1:
            c+=1
if c==n:
    print(True)


else:
   print(False)
