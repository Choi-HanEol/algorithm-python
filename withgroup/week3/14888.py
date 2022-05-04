import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
add, sub, mul, div = map(int,input().split())
answer = []
def BT(add, sub, mul, div, res, i):
	# 종료 조건
	if add == 0 and sub == 0 and mul == 0 and div == 0:
		answer.append(res)
		return
	
	# 재귀 호출
	if add:
		BT(add - 1, sub, mul, div, res + A[i], i+1)
	if sub:
		BT(add, sub - 1, mul, div, res - A[i], i+1)
	if mul:
		BT(add, sub, mul - 1, div, res * A[i], i+1)
	if div:
		if res < 0:
			BT(add, sub, mul, div - 1, -(-res // A[i]), i+1)
		else:
			BT(add, sub, mul, div - 1, res // A[i], i+1)
 
BT(add, sub, mul, div, A[0], 1)
print(max(answer))
print(min(answer))