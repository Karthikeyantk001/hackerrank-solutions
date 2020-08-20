'''n=int(input())
arr=[];arr1=[]
for i in range(n):
    arr.append(input())
arr1=arr.copy()
for i in range(len(arr)):
     arr1.reverse()
     try: 
       if arr1.count(arr[i])>1:
         arr1.remove(arr[i])
     except:
         arr=arr
     arr1.reverse()
        
print(len(arr1))
for i in arr1:
    print(str(arr.count(i))+' ',end='')'''


'''4
bcdef
abcdefg
bcde
bcdef'''
from collections import Counter
n=int(input());arr=[]
for i in range(n):
    arr.append(input())
x=dict(Counter(arr))
print(len(x))
k=list(x.values())
for i in k:
    print(i,end=' ')

#successs!!!!!!!



