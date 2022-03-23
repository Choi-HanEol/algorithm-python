input_list = [0 for i in range(10)]; reminder_list = [0 for i in range(10)] #길이를 10으로 지정하고 0으로 초기화, 이를 안할 시 인덱스 에러
count = 0
for i in range(10):
    s = int(input())
    reminder_list[i] = s % 42
for i in range(10):
    for j in range(i+1, 10):
        if reminder_list[i] == -1:
            continue
        elif reminder_list[i] == reminder_list[j]:
            input_list[j] = -1
for i in input_list:
    if i != -1:
        count += 1
print(count)

