n=int(input())
arr=[]
for i in range(n):
    command=input().split()
    if len(command)==3:
        for i in range(1,3):
            command[i]=int(command[i])

    if len(command)==2:
        command[1]=int(command[1])
    if command[0]=="insert":
        arr.insert(command[1],command[2])
    elif command[0]=="print":
        print(arr)
    elif command[0]=="remove":
        arr.remove(command[1])
    elif command[0]=="append":
        arr.append(command[1])
    elif command[0]=="sort":
        arr.sort()
    elif command[0]=="pop":
        arr.pop()
    elif command[0]=="reverse":
        arr.reverse()
    
    
    
        
    
    
