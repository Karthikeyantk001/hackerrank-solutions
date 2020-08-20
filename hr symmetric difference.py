'''a=int(input())
sa=set(map(int,input().split()))
b=int(input())
sb=set(map(int,input().split()))
arr=list( sa.union(sb).difference(sa.intersection(sb)))
arr.sort()
for i in arr:
    print(i)'''
'''s=set()
for i in range(int(input())):
    s.add(input())
print(len(s))'''

'''x=int(input())
arr=set(map(int,input().split()))
c=int(input())
for i in range(c):
    cm=input().split()
    if len(cm)==2:
        s=cm[0]
        x=int(cm[1])
    else:
        s=cm[0]
    if s=="pop":
        arr.pop()
    if s=="remove":
        arr.remove(x)
    if s=="discard":
        arr.discard(x)
print(sum(arr))'''

n=int(input())
arr=set(map(int,input().split()))
for i in range(int(input())):
    w,c=map(str,input().split())
    c=int(c)
    if w=="intersection_update":
        arr.intersection_update(set(map(int,input().split())))
    if w=="update":
        arr.update(set(map(int,input().split())))
    if w=="symmetric_difference_update":
        arr.symmetric_difference_update(set(map(int,input().split())))
    if w=="difference_update":
        arr.difference_update(set(map(int,input().split())))

print(sum(arr))
    

        
