import re
if __name__ == '__main__':
    N = int(input())
    arr=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        pattern=r"([\w\.-]+)@gmail([\w\.-]+)com"
        if re.search(pattern,emailID):
            arr.append(firstName)
    arr.sort()
    for i in arr:
        print(i)

