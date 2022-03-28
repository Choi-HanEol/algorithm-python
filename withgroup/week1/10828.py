import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n):
    input_str = sys.stdin.readline().split()

    if input_str[0] == 'push':
        stack.append(int(input_str[1]))
    elif input_str[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])    #-1은 뒤를 기준으로 첫 번째
    elif input_str[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())  #맨 마지막 요소를 반환하고 삭제
    elif input_str[0] == 'size':
        print(int(len(stack)))
    elif input_str[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)