import sys

T = int(sys.stdin.readline())

for _ in range(T):
    count = 1   #서류순위 1위는 무조건 채용
    volunteer = []

    vn = int(sys.stdin.readline())  #각 테스크 케이스에 관한 지원자 수
    for _ in range(vn):
        rank = tuple(map(int,sys.stdin.readline().split()))
        volunteer.append(rank)

    volunteer.sort(key=lambda x:x[0])   #서류순위를 기준으로 정렬
    passV = volunteer[0][1]   #서류순위 1위의 면접 순위를 비교함 서류 순위가 1위인 사람은 무조건 합격이고 그의 면접 순위보다 떨어지면 불합격

    for i in range(1, vn):
        if(volunteer[i][1] < passV):
            passV = volunteer[i][1]
            count += 1
    print(count)
