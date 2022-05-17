t = int(input())

for _ in range(t):
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    n = int(input())
    if n > 1:
        for i in range(2, n+1): #시작은 fib(2)부터 range(2,2)라면 반복문 수행이 안됨
            cnt_0.append(cnt_0[i-2] + cnt_0[i-1])
            cnt_1.append(cnt_1[i - 2] + cnt_1[i - 1])
    print(cnt_0[n], cnt_1[n])

# 규칙성
#   fib       0   1   2(0+1)   3(2+1)   4(3 + 2)   5(4+3)
# 0(출력)      1   0   1        1        2          3
# 1(출력)      0   1   1        2        3          5
# 즉 전꺼 더하기 전전꺼