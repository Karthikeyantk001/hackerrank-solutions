f=0
d1,m1,y1=map(int,input().split())
d,m,y=map(int,input().split())
if y1-y>0 :
    f=10000
    print(f)
elif m1-m>0 and y1>=y:
    f=500*(m1-m)
    print(f)
elif d1-d>0 and m1>=m and y1>=y:
    f=15*(d1-d)
    print(f)
else:
    print(f)


