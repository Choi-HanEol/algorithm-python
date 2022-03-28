import sys
import heapq

n = int(sys.stdin.readline())

heap = []

for i in range(n):
    input_num = int(sys.stdin.readline())
    if input_num == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)) #heapq.heappop(heap)의 type은 int
    else:
        heapq.heappush(heap, input_num)