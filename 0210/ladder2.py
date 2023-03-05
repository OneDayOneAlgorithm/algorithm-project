import sys
sys.stdin = open('ladder2.txt')
for tc in range(10):
    T = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    di = [1, 0, 0]  # 하 좌 우
    dj = [0, -1, 1]
    cnt = 9999999
    number = 0
    for j in range(100):
        first_j = j                 # j가 계속 바뀔 예정이니 처음 j 값 저장
        if data[0][j] == 1:         # 출발 지점 설정
            i = 0                   # 행은 0에서 시작
            instance_cnt = 0        # 시작
            while i < 99:           # 출발 후 끝날 때 까지 반복
                if j > 0 and data[i + di[1]][j + dj[1]]:  # 왼쪽 길이 있으면
                    i += di[1]                            # 왼쪽으로 한칸 이동하고
                    j += dj[1]
                    instance_cnt += 1
                    while data[i + 1][j] != 1:            # 아래 길이 나올때까지 왼쪽으로
                        i += di[1]
                        j += dj[1]
                        instance_cnt += 1
                elif j < 99 and data[i + di[2]][j + dj[2]]:  # 오른쪽 길이 있으면
                    i += di[2]                               # 오른쪽으로 한칸 이동하고
                    j += dj[2]
                    instance_cnt += 1
                    while data[i + 1][j] != 1:               # 아래 길이 나올때까지 오른쪽으로
                        i += di[2]
                        j += dj[2]
                        instance_cnt += 1
                i += di[0]                                   # 아래로 한칸이동
                j += dj[0]
                instance_cnt += 1
            if cnt > instance_cnt:                           # 거리가 더 짧을 때
                cnt = instance_cnt                           # cnt에 값을 저장
                number = first_j
    print(f'#{tc+1} {number}')
