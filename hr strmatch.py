
def count_substring(string, sub_string):
   global c
   c=0
   for i in range(len(string)):
       if string[i]==sub_string[0]:
           new=string[i:i+len(sub_string)]
           
           if new==sub_string:
             
               c+=1
   return c
           
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
#success