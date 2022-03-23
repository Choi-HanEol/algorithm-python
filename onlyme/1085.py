list1 = []
x, y ,w ,h = map(int, input().split())
list1.append(abs(x-w))
list1.append(x)
list1.append(abs(y-h))
list1.append(y)
min_num = min(list1)
print(min_num)