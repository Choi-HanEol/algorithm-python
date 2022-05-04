def dfs():
    if len(R) == (N//2):
        start.append(R[:])
        link.append(list(set(num) - set(R[:])))
    for i in range(1,N+1):
        if i > R[-1]:
            R.append(i)
            dfs()
            R.pop()

M = []
N = int(input())
for i in range(N):
    M.append(list(map(int, input().split())))
num = [i for i in range(1,N+1)]

# 모든 경우에 팀 안에 1번이 들어있으므로 1번이 들어간 모든 경우의 수를 출력하면 된다.
R = [1]
start = []
link = []
dfs()

# result = 스타트팀과 링크팀 점수차를 저장하는 리스트
result = []

for i in range(len(start)):
    start_sum = 0
    link_sum = 0
    for j in range(N//2):
        for _ in range(N//2):
            start_sum += M[start[i][j]-1][start[i][_]-1] 
            link_sum += M[link[i][j]-1][link[i][_]-1]
    result.append(abs(start_sum -link_sum)) 
print(min(result))