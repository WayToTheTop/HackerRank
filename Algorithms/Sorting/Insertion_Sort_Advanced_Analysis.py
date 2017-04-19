#https://www.hackerrank.com/challenges/insertion-sort
def inversion(ar):
    n = len(ar)
    if n < 2:
        return 0
    n1 = int(len(ar)/2)
    n2 = len(ar) - n1
    ar1 = ar[:n1]
    ar2 = ar[n1:]
    ans = inversion(ar1) + inversion(ar2)
    i1 = 0
    i2 = 0
    for i in range(n):
        if i1<n1 and (i2>=n2 or ar1[i1] <=ar2[i2]):
            ar[i] = ar1[i1]
            i1 += 1
            ans += i2
        else:
            ar[i] = ar2[i2]
            i2 += 1
    return ans        
            


T = int(input())
for i in range(T):
    n = input()
    ar = [int(x) for x in input().split()]
    print (inversion(ar))
