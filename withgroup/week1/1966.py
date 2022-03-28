from queue import Queue

que = Queue()
pri_que = []

test_case = int(input())

for _ in range(test_case):
    cnt = 1
    n, m = map(int, input().split())
    pri_que = list(map(int, input().split()))
    max_pri = max(pri_que)
    for i in pri_que:
        que.put(i)
    while True:
        pop = que.get()

        if pop == max_pri:
            if m == 0:
                print(cnt)
                break
            else:
                pri_que.remove(pop)
                max_pri = max(pri_que)
                cnt += 1
                m -= 1
        else:
            if m == 0:
                m = n - 1
            else:
                m -= 1
            que.put(pop)
