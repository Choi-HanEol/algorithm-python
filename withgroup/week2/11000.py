import sys
import heapq

time = []
n = int(sys.stdin.readline())

for _ in range(n):
    input_time = tuple(map(int, sys.stdin.readline().split()))
    time.append(input_time)

time.sort(key=lambda x: x[0])
# time.sort(key=lambda x: x[1]) 다른 강의실에 추가하는 것이기 때문에 안씀(시작시간과 heap[0]을 비교, 시작시간이 작은거부터 비교해야한다.(heap의 head는 가장 작은 값이기 때문에))

heap = []
heapq.heappush(heap, time[0][1])  # 힙 -> 첫번째 인자가 최소값 (강의가 제일 빨리 끝나는 시간)

for j in range(1, n):
    if heap[0] > time[j][0]:  # 강의가 제일 빨리 끝나는 시간보다 시작시간잉 더 이르면 강의실을 하나 추가 배정
        heapq.heappush(heap, time[j][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, time[j][1])


print(len(heap))  # 힙 하나가 한 강의실이라 생각, 힙의 원소 개수는 강의실 개수
