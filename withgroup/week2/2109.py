import sys
import heapq

n = int(sys.stdin.readline())
list_d_and_p = [tuple(map(int, sys.stdin.readline().split()))
                for _ in range(n)]

# list_d_and_p.sort(key=lambda x: x[0], reverse=True)   heap의 head에는 가장 낮은 금액이 들어있기 때문에 금액 기준 정렬은 필요없다
list_d_and_p.sort(key=lambda x: x[1])

# print(list_d_and_p)
heap = []
result = 0

# heap의 길이를 하루라고 생각하자 예를 들어 heap의 길이가 4이면, 강사는 4일 강연을 한다.
for i in list_d_and_p:
    heapq.heappush(heap, i[0])
    if len(heap) > i[1]:
        heapq.heappop(heap)
for i in range(len(heap)):
    result += heap[i]

print(result)

