arr=[];arr1=[]
n,m=map(int,input("Enter dimension: ").split("x"))

while any([n<3,m<3]):
  print("minimum 3x3 needed!")
  n,m=map(int,input("Enter dimension again: ").split("x"))
else:
   print("Enter your {0}x{1} matrix :".format(n,m))
  
for i in range(n):
    arr.append(list(map(int,input().rstrip().split())))
for i in range(n-2):
    for j in range(m-2):
       arr1.append( arr[i][j]+arr[i][j+1]+arr[i][j+2]+
                    arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+
                    arr[i+2][j+2])
       
print(max(arr1))

#success
'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
6 x 6 matrix
'''
