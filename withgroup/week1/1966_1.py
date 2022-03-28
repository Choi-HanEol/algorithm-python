test_case = int(input())

for _ in range(test_case):
    cnt = 1
    n, m = map(int, input().split())
    pri_que = list(map(int, input().split()))
    pri_que = list(map(lambda x: [x, 0], pri_que))
    pri_que[m][1] = 1

    while True:
        if pri_que[0][0] == max([i[0] for i in pri_que]):   #열을 대상으로 max값을 찾음
            if pri_que[0][1] == 1:
                print(cnt)
                break
            else:
                del pri_que[0]
                cnt += 1
        else:
            pri_que.append(pri_que[0])
            del pri_que[0]