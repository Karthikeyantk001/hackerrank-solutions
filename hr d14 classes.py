class Difference:
    def __init__(self, a):
        self.__elements = a
    global diff,maximumDifference
    diff=[]
    def computeDifference(self):
        for i in range(len(a)):
            for j in range(len(a)):
                
               diff.append(abs(a[i]-a[j]))
    
        self.maximumDifference= int(max(diff))
         
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

#success
