input_list= []
for i in range(9):
    input_list.append(int(input()))
max_num = max(input_list)
print(max_num)
print(input_list.index(max_num)+1)
