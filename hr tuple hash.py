if __name__ == '__main__':
    n = int(input())
    arr=(input().split())
    for i in range(n):
        arr[i]=int(arr[i])
    t=tuple(arr)
    print(hash(t))
