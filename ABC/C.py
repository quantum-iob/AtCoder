from itertools import combinations
N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy_comb = list(combinations(xy, 3))
cnt = 0
for i in range(len(xy_comb)):
    p1 = xy_comb[i][0]
    p2 = xy_comb[i][1]
    p3 = xy_comb[i][2]
    if (p2[1]-p1[1])*(p3[0]-p1[0]) != (p3[1]-p1[1])*(p2[0]-p1[0]):
        cnt += 1

print(cnt)