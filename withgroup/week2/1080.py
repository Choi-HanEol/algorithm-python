import sys

n, m = map(int, sys.stdin.readline().split())

# sys.stdin.readline()은 개행 문자를 삭제시키지 않기 때문에 rstrip로 오른쪽에 있는 개행문자를 삭제시켜줌
list1 = [list(map(int, sys.stdin.readline().rstrip('\n'))) for i in range(n)]
list2 = [list(map(int, sys.stdin.readline().rstrip('\n'))) for i in range(n)]
# list1 = [list(map(int, input())) for i in range(n)]   //input은 입력받은 개행 문자를 삭제시켜 반환
# list2 = [list(map(int, input())) for i in range(n)]   //rstrip할 필요 없음



def reverse(i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            list1[x][y] = 1 - list1[x][y]


cnt = 0
for i in range(n-2):
    for j in range(m-2):
        if list1[i][j] != list2[i][j]:
            reverse(i, j)
            cnt += 1
        if list1 == list2:
            break
    if list1 == list2:
        break
if list1 == list2:
    print(cnt)
else:
    print(-1)
