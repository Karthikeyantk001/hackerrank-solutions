for i in range(7):
    for j in range(21):
       if (i==0 or i==6) and j==21//2:
           print('|',end='')
       elif (i==0 or i==6) and (j==(21//2)+1 or j==(21//2)-1):
           print(".",end='')
       elif i==0 or i==6:
           print("-",end='')
       else:
           print(" ",end='')
       if i==3 and i not in [
           print

    print()

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))
    
