# import imp
# import sys
# import heapq

# n = int(sys.stdin.readline())
# list_d_and_p = [tuple(map(int, sys.stdin.readline().split()))
#                 for _ in range(n)]

# list_d_and_p.sort(key=lambda x: x[0], reverse=True)
# list_d_and_p.sort(key=lambda x: x[1])

# # print(list_d_and_p)
# heap = []
# heapq.heappush(heap, list_d_and_p[n-1])
# # for i in range(1, n):
# #     if list_d_and_p[i-1][1] != list_d_and_p[i][1]:
# #         money += list_d_and_p[i][0]
# for i in range(n-2, -1, -1):
#     if heap[0][0] >= list_d_and_p[i][0]:


# print(money)

import heapq

n = int(input())
lst = []
for i in range(n):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: (x[1]))
p_list = []
for i in lst:
    heapq.heappush(p_list, i[0])
    if (len(p_list) > i[1]):
        heapq.heappop(p_list)

print(sum(p_list))
