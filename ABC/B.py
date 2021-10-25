N, P = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for x in a:
    if x < P:
        cnt += 1
print(cnt)
