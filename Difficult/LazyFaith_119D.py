from bisect import bisect_left

A, B, Q = map(int, input().split())
s = [int(input()) for _ in range(A)]
t = [int(input()) for _ in range(B)]
x = [int(input()) for _ in range(Q)]

nears = []
neart = []

for i in s:
    b_s = bisect_left(t, i)
    if b_s >= len(t)-1:
        nears.append(abs(t[-1]-i))
    else:
        nears.append(min(abs(t[b_s-1]-i), abs(t[b_s]-i)))

for j in t:
    b_t = bisect_left(s, j)
    if b_t >= len(s)-1:
        neart.append(abs(s[-1]-j))
    else:
        neart.append(min(abs(s[b_t-1]-j), abs(s[b_t+1]-j)))


for k in range(Q):
    bt = bisect_left(t, x[k])
    bs = bisect_left(s, x[k])

    # print(bt, bs)

    if bt > len(t)-1:
        bt = len(t)-1
        difft = abs(t[-1]-x[k])
    if bt == 0:
        difft = abs(t[0]-x[k])
    if 1<=bt<=len(t)-1:
        difft = min(abs(t[bt-1]-x[k]), abs(t[bt]-x[k]))
        bt = bt-1 if difft == abs(t[bt-1]-x[k]) else bt
    
    if bs > len(s)-1:
        bs = len(s)-1
        diffs = abs(s[-1]-x[k])
        # print(diffs)
    if bs == 0:
        diffs = abs(s[0]-x[k])
    if 1<=bs<=len(s)-1:
        diffs = min(abs(s[bs-1]-x[k]), abs(s[bs]-x[k]))
        # print(abs(s[bs-1]-x[k]))
        bs = bs-1 if diffs == abs(s[bs-1]-x[k]) else bs
    
    
    # print(difft, diffs)
    # print(neart[bt], nears[bs])
    print(min(difft+neart[bt], diffs+nears[bs]))


# matsueda's answer

from bisect import *
a,b,q  = map(int,input().split())
s = [int(input()) for _ in range (a)]+[10**100]
t = [int(input()) for _ in range (b)]+[10**100]
st = sorted(s+t)
dic = {}
dic[10**100] = 10**100

for i in range (a):
    ind = bisect_left(t,s[i])
    dic[s[i]] = min(abs(t[ind-1]-s[i]),abs(t[ind]-s[i]))

for i in range (b):
    ind = bisect_left(s,t[i])
    dic[t[i]] = min(abs(s[ind-1]-t[i]),abs(s[ind]-t[i]))

for _ in range (q):
    x = int(input())
    ind = bisect_left(st,x)
    print(min(abs(st[ind-1]-x)+dic[st[ind-1]],abs(st[ind]-x)+dic[st[ind]]))