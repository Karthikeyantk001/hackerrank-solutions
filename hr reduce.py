n,m=map(int,input().split())
arr=set(map(int,input().split()))
a=set(map(int,input().split()))
b=set(map(int,input().split()))
love=len(arr.intersection(a))
hate=len(arr.intersection(b))
print(love-hate)


