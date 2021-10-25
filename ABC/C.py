N, M = map(int, input().split())
A = [list(input()) for _ in range(2*N)]
x = [0]*(2*N)
wins = []
for i in enumerate(x, 0):
    wins.append(list(i))

# print(wins)

for j in range(M):
    for k in range(0, 2*N-1, 2):
        p1 = A[wins[k][0]][j]
        p2 = A[wins[k+1][0]][j]
        if p1 != p2:
            if p1 == 'G':
                if p2 == 'C':
                    wins[k][1] += 1
                else:
                    wins[k+1][1] += 1
            if p1 == 'C':
                if p2 == 'P':
                    wins[k][1] += 1
                else:
                    wins[k+1][1] += 1
            if p1 == 'P':
                if p2 == 'G':
                    wins[k][1] += 1
                else:
                    wins[k+1][1] += 1
    wins = sorted(wins, key=lambda x: x[0])
    wins = sorted(wins, key=lambda x: x[1], reverse=True)
#     print(wins)

# print(wins)           

for l in range(len(wins)):
    print(wins[l][0]+1)




