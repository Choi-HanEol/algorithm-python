import sys
import heapq

n = int(sys.stdin.readline())

heap = []

for i in range(n):
    input_num = tuple(map(int, sys.stdin.readline().split()))

    if input_num[0] == 0:
        if not heap:
            print(0)
        else:
            print((heapq.heappop(heap))[1]) #heapq.heappop(heap)의 type은 int
    else:
        heapq.heappush(heap, input_num)