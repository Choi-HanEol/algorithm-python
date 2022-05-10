from collections import deque

N, M = map(int, input().split())
miro = []   # 미로

# 미로를 입력
for _ in range(N):
    miro.append(list(map(int, input())))

# 방향을 나타냄 좌, 상, 우, 하
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

visited = [[0] * M for _ in range(N)]

q = deque([(0, 0)])
# 첫 번째 위치가 문제에 주어져 있으므로 1로 변경
visited[0][0] = 1

while q:
    x, y = q.popleft()

    # 미로의 끝에 도달 했을 때 해당 미로의 값을 호출
    if x == N-1 and y == M-1:
        print(visited[x][y])
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if visited[nx][ny] == 0 and miro[nx][ny] == 1:      #방문하지 않았고, 길이 있으면
                visited[nx][ny] = visited[x][y] + 1     
                q.append((nx, ny))