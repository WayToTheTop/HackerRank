#https://www.hackerrank.com/challenges/journey-to-the-moon
N,P = map(int, input().strip().split(' '))
assert 1 <= N <= 10**5
assert 1 <= P <= 10**6
list_of_sets = []

for _ in range(P):
    a,b = map(int, input().strip().split(' '))
    new_set = set()
    i = 0
    los_len = len(list_of_sets)
    while i < los_len:
        if a in list_of_sets[i] or b in list_of_sets[i]:
            new_set.update(list_of_sets[i])
            del list_of_sets[i]
            los_len -=1
        else:
            i+= 1
    new_set.update([a,b])
    list_of_sets.append(new_set)
   
ans = N * (N-1) / 2   
for s in list_of_sets:
    ans -= len(s) * (len(s)-1) / 2
print (int(ans))
