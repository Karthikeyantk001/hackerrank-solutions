from collections import Counter
l=list(input())
d=dict(Counter(l))
j=0

for i in list(d.keys()) :
    if j<3:
     print("%s %d"%(i,d[i]))
     j+=1
