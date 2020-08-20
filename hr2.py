n=[]
x=int (input())
for i in range (x):
    n.append(input().split())
player=input()
for i in range(x):
    if n[i][0]==player:
         for j in range(1,4):
           n[i][j]=int(n[i][j])
         print((n[i][1]+n[i][2]+n[i][3])/3)
