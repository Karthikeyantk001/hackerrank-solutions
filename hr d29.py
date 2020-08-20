'''from itertools import combinations
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])
        arr2=[]
        arr=[x for x in range(1,n+1)]
        arr1=list(combinations(arr,2))
        for i in arr1:
            arr2.append(i[0]&i[1])
            arr2.sort()
        for j in range (len(arr2)):
            if arr2[j]>=k:
                print(arr2[j-1])
                break
        else:
            print(arr2[0])'''
if __name__ == '__main__':
    for a in range(int(input())):
      n , k = map(int , input().split())
      print(k-1 if ((k-1) | k) <= n else k-2)
                
                
                
        
        
