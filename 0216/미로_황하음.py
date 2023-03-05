def dfs(sr, sc):
    stack = [(sr, sc)]
    # 우리가 탐색하려는 노드들이 2차원 배열이기 때문에 방문 표시도 2차원 배열로
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    # stack 의 top 에서 갈 수 있는 모든 경로 탐색
    # 갈 수있는 경로를 발견하면 즉시 이동
    # 없으면 stack pop
    # 위를 계속 반복 >> stack 이 비어있지 않으면

    while stack:
        # 현재 위치
        cr, cc = stack[-1]
        if arr[cr][cc] == '3':  # 도착!
            return 1
        # top 에서 이동할 수 있는 모든 경로 살펴보기
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != '1' and not visited[nr][nc]:  # 갈 수 있음
                stack.append((nr, nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()

    return 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(N)]
    # 2 - 출발, 3 - 도착. 0 - 통로. 1- 벽
    for i in range(N):  # 출발점 찾기
        for j in range(N):
            if arr[i][j] == '2':
                sr = i
                sc = j

    print(f'#{tc} {dfs(sr, sc)}')