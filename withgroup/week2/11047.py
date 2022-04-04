import sys


def find_max(input_list):
    global n, k
    while True:
        max_num = max(input_list)
        if max_num > k:
            input_list.remove(max_num)
        else:
            if max_num == k:  # max_num과 k원이 같으면 mun_num한장으로 k가 되니 바로 그냥 끝내버리기
                print('1')
                sys.exit()
            else:  # max_num가 k원보다 작으면
                return max_num


money_list = []

n, k = map(int, sys.stdin.readline().split())
remain_money = k
count_money = 0

for _ in range(n):
    money_list.append(int(sys.stdin.readline()))

while True:
    if remain_money == 0:
        break
    max_money = find_max(money_list)
    count_money = count_money + remain_money//max_money
    remain_money = remain_money % max_money
    money_list.remove(max_money)

print(count_money)