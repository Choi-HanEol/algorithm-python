from sys import stdin
t = int(stdin.readline())
d = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

while t > 0:
    n = int(stdin.readline())
    d_l = len(d)    #초기값은 11이 된다 n번째를 맞추려고 d[0]을 0으로 초기화 했음
    if d_l <= n:
        for i in range(d_l, n + 1):
            d.append(d[i-5] + d[i-1])
    print(d[n])
    t -= 1
