d1=[];d2=[];l=[]

def what(s):    
    lr=list(s)
    l=lr.copy()
    lr.reverse()
    
    for j in range(len(l)):
        l[j]=ord(l[j])
        lr[j]=ord(lr[j])
    print(l)
    print(lr)
    for k in range(1,len(s)):
        d1.append(abs(l[k]-l[k-1]))
        d2.append(abs(lr[k-1]-lr[k]))

    if(d1==d2):
        print("Funny")
    else:
        print("Not Funny")

n=int(input())
for i in range(n):
    s=input()
    what(s)
