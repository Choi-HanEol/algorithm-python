list = []
for i in range(10):
    s = int(input())
    list.append(s%42)
list1 = set(list)   #set은 중복을 허용하지 않음
print(len(list1))
