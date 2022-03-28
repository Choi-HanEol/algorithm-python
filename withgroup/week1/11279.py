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
            print(abs(heapq.heappop(heap))) #heapq.heappop(heap)의 type은 int
    else:
        heapq.heappush(heap, -input_num)

#알아보니 heapq에는 최대 힙이 지원이 안됨
#그러므로 음의 정수를 이용하여 해결
