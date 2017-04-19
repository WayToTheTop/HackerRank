from heapq import heapify, heappush, heappop
from math import gcd

num_vertices, num_edges = [int(x) for x in input.split()]
edge_list = []
for _ in range(num_edges):
    edge_list.append([int(x) for x in input().split()])

last_p, last_q = 1, 100
    
while True:
    p,q = 0,0
    vert_free = [True]*num_vertices
    edges = [list() for x in range(num_vertices)]
    for e in edge_list:
        priority = (e[3] + last_q) / (e[2] + last_p)
        edges[e[0]].append((priority, e[2], e[3], e[1]))
        edges[e[1]].append((priority, e[2], e[3], e[0]))
    
    vert_free[0] = False
    todo = edges[0]
    heapify(edges[0])
    
    while todo:
        e = heappop(todo)
        if vert_free[e[3]]:
            p += e[1]
            q += e[2]
            vert_free[e[3]] = False
            for e2 in edges[e[3]]:
                if vert_free[e2[3]]:
                    heappush(todo,e2)
           
    if p/q == last_p/last_q: 
        cd = gcd(p,q)
        print (str(p//cd) + '/' + str(q//cd))
        break  
    else:
        last_p, last_q = p,q          
