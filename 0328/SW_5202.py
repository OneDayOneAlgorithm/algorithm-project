T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x: x[1])    # 종료시간이 빠른게 맨 앞에 온다.
    cnt, end = 0, 0  # 몇번 사용했는지 세는 cnt와
    for i in range(N):  # 종료시간 낮은 것부터 확인
        s, e = lst[i]   # 현재 작업시간의 시작시간과 종료시간을 할당
        if end <= s:  # 시작시간이 이전 종료시간보다 크거나 같으면 + 1
            end = e   # 종료시간을 갱신
            cnt += 1
    print(f'#{tc} {cnt}')
