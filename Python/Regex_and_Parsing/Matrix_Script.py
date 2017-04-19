import re

n,m = list(map(int,input().split(' ')))
a = ['']*m
for _ in range(n):
    line = list(input())
    for i in range(len(a)):
        a[i] += line[i]
print (re.sub(r'(?<=\w)[!@#$%& ]+(?=\w)', ' ', ''.join(a), flags=re.I))
