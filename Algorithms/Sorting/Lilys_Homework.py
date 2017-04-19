#https://www.hackerrank.com/challenges/lilys-homework
def mergeSort(ar):
    n = len(ar)
    if len(ar) <2:
        return
    n1 = int(n/2)
    n2 = n - n1
    ar1 = ar[:n1]
    ar2 = ar[n1:]
    mergeSort(ar1)
    mergeSort(ar2)
    i1 = i2 = 0
    for i in range(n):
        if i1<n1 and (i2>=n2 or ar1[i1] <= ar2[i2]):
            ar[i] = ar1[i1]
            i1 += 1
        elif i2 < n2:
            ar[i] = ar2[i2]
            i2 += 1

def lilyshomework(ar):
    m = {}
    for i in range(len(ar)):
        m[ar[i]] = i
    sorted_ar = sorted(ar)
    i = 0
    ans = 0
    for i in range(len(ar)):
        if ar[i] != sorted_ar[i]:
            swap_ind = m[sorted_ar[i]]
            ar[swap_ind] = ar[i]
            m[ar[i]] = m[sorted_ar[i]]
            ans += 1          
    return ans

n = input()
ar = [int(x) for x in input().split()]
asc = lilyshomework(list(ar))
desc = lilyshomework((ar)[::-1])
print (min(asc, desc))
