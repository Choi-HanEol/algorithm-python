list = []; reminder_list = []
count = 0
for i in range(10):
    s = int(input())
    reminder_list.append(s%42)
for i in range(10):
    for j in range(i+1, 10):
        if reminder_list[i] == -1:
            continue
        elif reminder_list[i] == reminder_list[j]:
            list[j] = -1
for i in list:
    if i != -1:
        count += 1
print(count)

