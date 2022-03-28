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
            print((heapq.heappop(heap))[1]) #heapq.heappop(heap)의 type은 int
    else:
        heapq.heappush(heap, (abs(input_num), input_num))

#테스트 결과 튜플로 힙을 넣으면 첫째 요소를 기준으로 정렬
#하지만 첫째 요소가 같으면 그 다음인 두번째 요소 기준으로 정렬

#즉 (2,5) (2,-5) 입력하면 (2,-5) (2,5) 순으로 정렬