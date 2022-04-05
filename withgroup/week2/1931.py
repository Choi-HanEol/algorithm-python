import sys

time = []
n = int(sys.stdin.readline())

for _ in range(n):
    input_time = tuple(map(int, sys.stdin.readline().split()))
    time.append(input_time)

time.sort(key=lambda x: x[0])
time.sort(key=lambda x: x[1])

cnt = 0
end = 0
for i, j in time:

    if i >= end:
        cnt += 1
        end = j
print(cnt)
