import sys
n,m =  map(int,sys.stdin.readline().split())
graph = []
temp = [[0]*m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0
#바이러스를 퍼지게 하는 함수
def virus(x,y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny] = 2
                virus(nx,ny)
#현재맵에서 안전영역 크기 계산 메서드
def score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score+=1
    return score


#깊이 우선 탐색(DFS를 이용해 울타리를 설치하면서 안전영역의 크기를 계산)
#count : 울타리 갯수
def dfs(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        result = max(result,score())
        return

    #빈공간에 울타리 설치 
    #DFS 이용해 울타리 설치 가능한 모든경우의 수 탐색
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count+=1
                dfs(count)
                graph[i][j] = 0
                count-=1
                #맵의 상태가  count값이 3이 된 이전과 이후가 계속해서 바뀌기 때문에 
                #모든 울타리 설치 경우의 수를 구할 수 있다.
dfs(0)
print(result)