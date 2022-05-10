import sys
input = sys.stdin.readline

n, m = map(int, input().split())

high = list(map(int, input().split()))

start = 0
end = max(high)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    cnt = sum(i - mid if i - mid > 0 else 0 for i in high)
    
    if cnt < m:
        end = mid - 1
    else:
        start = mid + 1

print(end)