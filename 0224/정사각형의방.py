def bfs(si, sj):
    q = []  # 큐 생성
    alst = []  # 리스트 생성

    q.append((si, sj))  # 큐에 시작점  삽입
    v[si][sj] = 1  # visited에 등록
    alst.append(arr[si][sj])  # 리스트에 현재 위치의 값 넣기

    while q:  # 큐가 빌때까지 반복(BFS로 실행)
        ci, cj = q.pop(0)  # 큐 에서 값을 빼고 현재값으로 설정

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 방향 설정
            ni, nj = ci + di, cj + dj  # 다음 값 설정
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and abs(arr[ci][cj] - arr[ni][nj] == 1:  # 맵 밖으로 안나가고 방문한적 없고 1차이나면
                q.append((ni, nj))  # 다음값을 q에 추가
                v[ni][nj] = 1  # visited에 다음값 등록
                alst.append(arr[ni][nj])  # 리스트에 다음값의 value를 넣기

    return min(alst), len(alst)  # value 중 가장 작은값, 그리고 리스트의 길이를 출력


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]  # 보드 만들기
    v = [[0] * N for _ in range(N)]  # visited 만들기
    ans, cnt = N * N, 0
    for si in range(N):
        for sj in range(N):
            if v[si][sj] == 0:  # 방문한 적 없는 곳이라면
                t, tcnt = bfs(si, sj)  # 변수에 함수 결과값 할당
                if cnt < tcnt or cnt == tcnt and ans > t:  # 결과값중에 길이가 가장 길거나 길이가 같을때 숫자가 작은값이면
                    ans, cnt = t, tcnt  # 그값을 출력값으로 등록

    print(f'#{test_case} {ans} {cnt}')
