import sys
input = sys.stdin.readline

tc = int(input())
for i in range(tc):
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    aIdx = 0
    bIdx = 0
    cnt = 0
    while aIdx < n and bIdx < m:
        if A[aIdx] > B[bIdx]:
            cnt += m - bIdx
            aIdx += 1
        else:
            bIdx += 1
    print(cnt)