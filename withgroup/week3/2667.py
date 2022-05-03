n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input())))
# 배열 입력 추가

arr = []
cnt = 0
dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]


def dfs(x, y):
    global cnt  # cnt를 함수 dfs에서 쓰기 위해서
    if x < 0 or x >= n or y < 0 or y >= n:  # 범위 지정 안하면 인덱스 에러: 지정한 배열의 범위를 벗어나기 때문
        return False

    if array[x][y] == 1:
        cnt += 1
        array[x][y] = 0     #방문한 지점은 0으로 만들어 다시 방문을 안하도록 만듦
        for i in range(4):
            dfs(x + dx[i], y + dy[i])   #재귀함수를 통해 dfs구현
        return True


for i in range(n):
    for j in range(n):  # (0,0)부터 (n,n)까지
        if dfs(i, j) == True:
            arr.append(cnt) #arr에 객 단지의 집의 수, cnt 추가
            cnt = 0

print(len(arr))
arr.sort()  #오름차순으로 정렬
for i in arr:
    print(i)