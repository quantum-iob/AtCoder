from collections import deque

N = int(input())
A = list(map(int, input().split()))
Adeq = deque(A)

div = 998244353

dp = [[0]*10 for _ in range(N)]

x = Adeq.popleft()
y = Adeq.popleft()
F = (x+y)%10
G = (x*y)%10
# print(F,G)
dp[0][F] += 1
dp[0][G] += 1

# print(dp)
for i in range(1,N-1):
    for j in range(10):
        if dp[i-1][j] >= 1:
            dp[i][(j+A[i+1])%10] += dp[i-1][j]%div
            dp[i][(j*A[i+1])%10] += dp[i-1][j]%div
    # print(dp)

for k in dp[-2]:
    print(k%div)