n = int(input())
d = [0, 0]  #0인 경우, 1인 경우

for i in range(2, n+1):
    result = d[i-1] + 1
    if i % 2 == 0:
        result = min(result, d[i//2] + 1)
    if i % 3 == 0:
        result = min(result, d[i//3] + 1)
    d.append(result)
print(d[n])
