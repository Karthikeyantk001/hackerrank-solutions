cube = lambda x: x**3

def fibonacci(n):
    if n==0:
        arr=[]
    if n==1:
        arr=[0]
    elif n>=2:
        arr=[0,1]
    for i in range(2,n):
        arr.append(arr[i-2]+arr[i-1])
    return arr
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
