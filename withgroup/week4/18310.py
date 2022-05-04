import sys
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
print(a[(N-1)//2])