g = int(input().strip())
for a0 in range(g):
    n = int(input().strip())
    seq = list(map(int, input().strip().split(' ')))
    # If Alice wins, print 'Alice' on a new line; otherwise, print 'Bob'
    moves = 0
    for i in range(1,len(seq)-1):
        if seq[i-1:i+2] == [0,1,0]:
            seq[i] = 0
    for i in range(1, len(seq)-1):
        if seq[i-1] == 0 and seq[i+1] == 0:
            moves += 1
    if moves % 2 == 0:
        print ('Bob')
    else:
        print ('Alice')
