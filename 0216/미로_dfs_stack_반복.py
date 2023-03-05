arr = [
[1,1,1,0,0],
[1,0,1,0,0],
[1,0,1,1,1],
[1,0,1,0,0],
[1,0,0,0,0],
]
N = 5

def dfs(sr,sc):
    stack = [(sr,sc)]
    # 우리가 탐색하려는...노드들이 2차원 배열이기 때문에
    # 방문표시도 2차원 배열로..
    visited = [[0] * N for _ in range(N)]
    visited[sr][sc] = 1

    # stack의 top에서 갈수 있는 모든 경로 탐색
    # 갈수 있는 경로를 발견하면 즉시 이동
    # 없으면 stack pop
    # 위를 계속 반복 >> stack이 비어있지 않으면
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while stack:
        #현재 위치
        cr,cc = stack[-1]
        if arr[cr][cc] == 2:
            return 1
        #top에서 이동할 수 있는 모든 경로 살펴보기
        # for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        for d in range(4):
            nr = cr+dr[d]
            nc = cc+dc[d]
            if 0<= nr < N and 0<= nc < N and arr[nr][nc] and not visited[nr][nc]: #갈 수있음!
                stack.append((nr,nc))
                #방문했음을 표시
                visited[nr][nc] = 1
                break
        else:
            stack.pop()
    return 0

print(dfs(0,0))











