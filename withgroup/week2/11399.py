import sys

n = int(sys.stdin.readline())
input_list = list(map(int, sys.stdin.readline().split()))

input_list.sort()

result = 0
sum = 0

for i in input_list:
    sum += i
    result += sum

print(result)