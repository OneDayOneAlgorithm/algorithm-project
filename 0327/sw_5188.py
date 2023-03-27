T = int(input())

# 길찾기 dfs
def road(x, y, total):
    global result
    # 만약 도착했다면
    if x == N-1 and y == N-1:
        # 마지막 도착점것을 더해주고
        total += arr[y][x]
        # 최소값을 갱신해준다.
        if total < result:
            result = total
            return
    # 시간을 줄이기위해 과정중에 현재 최소값 보다 크면 계산 가치 x
    if total > result:
        return

    dx = [1, 0]
    dy = [0, 1]

    # 모드를 돌아다니면서 검색
    for i in range(2):
        # 다음 좌표 둘러보기
        cx = x + dx[i]
        cy = y + dy[i]
        # 만약 범위 넘어가면 패스
        if x > N-1 or y > N-1:
            continue
        # 방문한 적이 없다면
        if not visited[y][x]:
            # 방문도장 찍고
            visited[y][x] = 1
            # 다음 좌표 보면서 total 값도 같이 넘겨줌
            road(cx, cy, total + arr[y][x])
            # 돌아왔다면 방문도장 지워주기
            visited[y][x] = 0

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split()))for _ in range(N)]
    # 결괏값은 최대값으로 설정
    result = 10 * 2 * N
    # 방문 검사를 위한 배열
    visited = [[0 for _ in range(N)]for _ in range(N)]
    # 길찾아보자 - 함수호출
    road(0, 0, 0)


    print("#{} {}".format(tc, result))