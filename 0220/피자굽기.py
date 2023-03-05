T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕 제한갯수, 총 피자갯수
    Data = list(map(int, input().split()))  # 각 피자당 치즈 수량
    Q = []  # 큐 만들기
    for i in range(N):
        Q.append([Data[i], i])  # 큐에 모든 치즈 수량과 그 인덱스를 저장

    i = 0
    while len(Q) != 1:  # Q의 길이가 1이 될 때까지 반복
        Q[0][0] = Q[0][0] // 2  # 맨 앞의 값을 2 나눈다

        if Q[0][0] == 0:  # 맨 앞의 값이 0이라면
            if N + i < M:  # 더 추가할 피자가 있으면
                Q.pop(0)  # 큐 맨 앞의 값을 팝 하고
                Q.append([Data[N + i], N + i])  # 큐에 다음 피자의 치즈갯수와 번호를 추가
                i += 1  # i 1 증가
            elif N + i >= M:  # 더이상 추가할 피자가 없으면
                Q.pop(0)  # 그냥 팝하라
        else:  # 맨 앞의 값이 0이 아니라면
            Q.append(Q.pop(0))  # 큐에 큐를 팝한 값을 추가
    print(f'#{tc} {Q[0][1] + 1}')  # 출력

