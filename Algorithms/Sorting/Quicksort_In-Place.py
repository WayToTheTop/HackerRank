#https://www.hackerrank.com/challenges/quicksort3
def LomutoPartition(ar, start, end):
    if len(ar[start:end+1]) == 1 or len(ar[start:end+1]) == 0:
        return ar
    p = ar[end]
    sub_i = start
    for i in range(start,end+1):
        if ar[i] <= p:
            t = ar[i]
            ar[i] = ar[sub_i]
            ar[sub_i] = t 
            sub_i += 1 
    print (' '.join(map(str,ar)))
    LomutoPartition(ar, start, sub_i-2)
    LomutoPartition(ar, sub_i, end)
            
n = int(input())
ar = [int(x) for x in input().split()]
LomutoPartition(ar, 0, n-1)
