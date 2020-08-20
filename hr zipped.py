x,y=map(int,input().split())
arr=[]
for i in range(y):
    
 arr.append(list(map(float,input().split())))

for j in range(x):
    su=0
    for k in range(y):
       su+=arr[k][j]
    print(su/y)
    
