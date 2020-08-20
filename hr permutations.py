from itertools import permutations
arr1=input().split()
s=arr1[0];arr2=[]
n=int(arr1[1])
l=list(permutations(s,n))
l.sort()
for i in l:
        s=''
        for j in range(len(i)):
                s+=i[j]
        arr2.append(s)
for item in arr2:
        print(item)
                
                


#success
