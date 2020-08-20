for i in range(int(input())):
    num=input()
    if num.isdigit() and len(num)==10:
        if int(num[0]) in [9,7,8]:
            print("YES")
        else:
          print("NO")
    else:
          print("NO")
