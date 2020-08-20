for i in range(int(input())):

    x=int(input())
    if x==1:
        print("Not Prime")
    else:
     for j in range(2,x//2+1):
        if x%j==0:
            print("Not prime")
            break
     else:
        print("Prime")
