import sys
n = int(sys.stdin.readline())
push_num = 1
input_list = []
output_list = []
stack = [0 for i in range(n)]   #크기 선언 안하니

for i in range(n):
    input_list.append(int(sys.stdin.readline()))

i = 0
while True:
    if stack[-1] > input_list[i]:  #여기서 index 에러가 떴다
        print('NO')
        sys.exit()  #프로그램 종료
    elif stack[-1] == input_list[i]:
        output_list.append('-')
        stack.pop()
        i += 1
        if i == n:
            break
    else:
        stack.append(push_num)
        push_num += 1
        output_list.append('+')

for i in range(len(output_list)):
    print(output_list[i])
