def solve(n, sum_v):    # min_v 를 구하는 함수 실행
    global min_v        # 재귀 하면서 사용하기 위해 글로벌에서 min_v 사용
    if n == N:          # n은 행을 의미. 마지막 행일 때
        if sum_v < min_v:   # 생산 비용이 더 싸다면
            min_v = sum_v   # 이 비용을 생산 비용으로 결정
        return              # 열을 바꿔보기위해 재귀를 종료
    if sum_v > min_v:       # 마지막 행은 아닌데 생산비용이 최저생산비용 보다 크다면 바로 재귀를 종료
        return
    for i in range(N):      # 열 순환
        if not used[i]:     # 순환 하지 않을 열일 시
            used[i] = 1     # 그 열을 순환 했다고 표시하고
            solve(n+1, sum_v+arr[n][i])  # 그 열로 출발. 그리고 행을 증가시키고 생산비용을 누적한다.
            used[i] = 0     # 재귀가 끝나고 이전 행으로 돌아오면 사용한 열은 초기화 해준다.


T = int(input())  # 테스트 케이스 입력
for tc in range(1, T+1):    # 테스트 케이스 반복
    N = int(input())    # NxN 행렬에서 N 입력
    arr = [list(map(int, input().split())) for _ in range(N)]
    used = [0] * N      # 방문 기록을 한다. 같은 열을 반복 하지 않기 위함
    min_v = 9999999999  # 최저 생산 비용을 엄청나게 크게 잡는다
    solve(0, 0)         # 최저 생산비용을 구하는 함수 실행(0열, 값 == 0)
    print(f'#{tc} {min_v}')  # 최저 생산비용 출력
