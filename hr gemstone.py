odd=0
n=int(input())
arr=input().split()
for i in range(len(arr)):
    arr[i]=int(arr[i])
for i in arr:
    c=arr.count(i)
    if (c%2!=0):
        odd+=1
print(odd)
    
        