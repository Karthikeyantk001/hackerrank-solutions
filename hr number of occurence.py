from collections import Counter
l=list(input())
d=dict(Counter(l))
j=0;x=0
k=list(d.values())
k.sort()
k.reverse()

it=list(d.items())
for i in range(len(it)):
	for j in range(len(it)):
		if it[i][1]>it[j][1]:
			it[i],it[j]=it[j],it[i]
for i in list(it):
    if x<3:
        print(it[x])
        x+=1
		
