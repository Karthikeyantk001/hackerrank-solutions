state=0
n=int(input())

for i in range(n):
 x=int(input())
 l=(input().split())
 for i in range(x):
    l[i]=int(l[i])
 while(x!=1):
    left=l[0]
    right=l[(len(l)-1)]
    for i in range(0,len(l)):
        if (left>=right):
            h=left
        else:
            h=right
        for j in range(1,len(l)-1):
            if l[j]<h:
               state='YES'
            else:
               state='NO'
              
       

    l.remove(h)
    x-=1   
 print(state)

   
    

        
    
