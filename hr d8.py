n=int(input());arr1=[]
for i in range(n):
    arr=input().split()
    arr1.extend(arr)
for i in range(n*2):
    if arr1[i].isdigit():
        arr1[i]=int(arr1[i])
for i in range(n):
    string=input()
    if string in arr1:
        print(string+"="+str(arr1[arr1.index(string)+1]))
    else:
        print("Not found")
        
    
    
        
    
#time out fetch from website 
