#https://www.hackerrank.com/challenges/fraudulent-activity-notifications
class CountList(object):
    def __init__(self, l):
        self.l = 201 * [0]
        self.n = len(l)
        self.isOdd = self.n % 2 
        for i in l:
            self.l[i] += 1
    
    def getList(self):
        return self.l
    def getLen(self):
        return self.n 
    def median(self):
        m = self.n // 2 + (self.n % 2)
        s = 0
        i = -1
        while s < m:
            i += 1
            s += self.l[i]      
        if self.isOdd:
            return i
        else:
            j = i
            while s < m+1:
                j += 1
                s += self.l[j]
            return (i + j)/2 
    def step(self,old, new):
        self.l[old] -= 1
        self.l[new] += 1
        
def notification_counter(ar,d):
    ans = 0
    countlist = CountList(ar[:d])
    for i in range(d,len(ar)):
        if 2 * countlist.median() <= ar[i]:
            ans += 1
        countlist.step(ar[i-d], ar[i])    
    return ans        
            
n,d = [int(x) for x in input().split()]
ar = [int(x) for x in input().split()]
print (notification_counter(ar,d))
