from collections import Counter
total=0
n= int(input())
l=list(input().split())
d=dict(Counter(l))
x=int(input())
keys=list(map(int,list(d.keys())))

for i in range(x):
  a,b=map(int,input().split())
  if a in keys:
      total+=b
      
      z=d[str(a)]-1
      d[str(a)]=z
      if d[str(a)]==0:
          d.pop(str(a))
      keys=list(map(int,list(d.keys())))

    

print(total)

#success!!!!!!!!!!!!1
