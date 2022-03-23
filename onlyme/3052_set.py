input_list = []
for i in range(10):
    s = int(input())
    input_list.append(s%42)
list1 = set(input_list)   #set은 중복을 허용하지 않음
print(len(list1))
