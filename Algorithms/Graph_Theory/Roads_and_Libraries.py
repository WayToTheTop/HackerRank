#https://www.hackerrank.com/challenges/torque-and-development
def dfs(node, connected, flag):
    if flag[node]:
        return 0
    flag[node] = 1
    num = 1
    for a in connected[node]:
        num += dfs(a,connected,flag)
    return num

q = int(input().strip())
for _ in range(q):
    n,m,x,y = map(int,input().strip().split())
    connected = [list() for __ in range(n+1)]
    flag = [0]*(n+1)
    for i in range(m):
        a,b = map(int,input().strip().split())
        connected[a].append(b)
        connected[b].append(a)
    ans = 0
    for i in range(1,n+1):
        if flag[i]:
            continue
        num = dfs(i,connected,flag)
        ans += min(x*num, (num-1)*y + x)
    print (ans)
