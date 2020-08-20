'''l=input()
n=int(input())

i=0; arr=[];arr2=[]
while i<len(l):
    arr.append(list(set(l[i:i+n])))
    i+=n

for i in range(len(arr)):
    x=arr[i]
    s=''
    for j in x:
        
        s+=j
    print(s)
    '''
    
from collections import Counter
arr2=[]
def merge_the_tools(string, k):
    global n,l,arr,i,x,z
    n=int(k)
    l=string
    i=0; arr=[];
    while i<len(l):
      arr.append(list(l[i:i+n]))
      i+=n
    fun(arr)
def fun(arr):
    for i in arr:
        c=dict(Counter(i))
        arr2.append(list(c.keys()))
    for i in arr2:
        for j in range(len(i)):
            s=''
            s+=i[j]
            print(s,end='')
        print()
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#success
