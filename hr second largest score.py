arr=[];arr2=[]

n=int(input())
for i in range(n):
    s=input()
    sc=float(input())
    arr.append([s,sc])
    arr2.append(sc)
    m=max(arr2)

for i in range(len(arr2)):
    try:
       arr2.remove(m)
    except:
        arr2=arr2

x=max(arr2)
for i in range(n):
  if arr[i][1]==x:
      print(arr[i][0])
    
