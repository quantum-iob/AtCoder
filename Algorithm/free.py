import bisect
#ranking with bisect.bisect_left
def ranking(ls: list):
    rank = sorted(list(set(ls)))
    return [bisect.bisect_left(rank, x) for x in ls]

if __name__ == '__main__':
    H, W, N = map(int, input().split())
    As, Bs = [], []
    for i in range(1,N+1):
        A, B = map(int, input().split())
        As.append(A)
        Bs.append(B)
    Arank = ranking(As)
    Brank = ranking(Bs)
    for j in range(N):
        print(Arank[j]+1, Brank[j]+1)
