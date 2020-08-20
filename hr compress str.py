n=list(map(int,input()))
from collections import Counter
d=dict(Counter(n))
for i in d.keys():
    print("(%d, %d) "%(d[i],i),end="")
