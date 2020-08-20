s1='';s2=''
n=int(input())
for i in range(n):
    s=input()
    for j in range(len(s)):
        if(j%2==0):
            s1=s1+s[j]
        elif (j%2!=0):
            s2=s2+s[j]
    print(s1,s2)
    s1='';s2=''
    
