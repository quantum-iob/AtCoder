import math
from collections import Counter
N = int(input())
total_comb = math.comb(N, 3)
points = [list(map(int, input().split())) for _ in range(N)]

a = []

for i in range(N):
    for j in range(i+1,N):
        if points[j][0]-points[i][0] == 0:
            a.append(10**10)
        else:
            a.append((points[j][1]-points[i][1])/(points[j][0]-points[i][0]))


cnt = Counter(a)
print(a)


linear = 0
for k in cnt.values():
    if k >= 2:
        linear += 1

print(total_comb-linear)
