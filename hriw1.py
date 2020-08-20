c=0
n=int(input())
arr=input().split()
def pair(arr):
    for i in range(len(arr)):
        arr[i]=int(arr[i])
    for j in range(0,len(arr)):
        for k in range (j,len(arr)):
            if arr[j]==arr[k]:
                global c
                c+=1
                arr.remove(arr[j])
                
pair(arr)
