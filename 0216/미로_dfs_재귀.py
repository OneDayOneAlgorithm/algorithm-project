arr = [
[1,1,1,0,0],
[0,0,1,0,0],
[1,1,1,1,1],
[0,0,1,0,1],
[2,1,1,1,1],
]
N = 5

dr = [-1,1,0,0]
dc = [0,0,-1,1]
#재귀를 활용하기 때문에 현재 위치를 인자로 받아온다.
#방문한 노드를 재방문하지 않기 위해서 visited를 이전 단계에서 받아옴
def dfs(r,c,visited):
    # 만약 현재 위치가 도착지점이라면 결과 반환
    if arr[r][c] == 2:
        return 1
    #재귀는 스택을 사용하지 않음 >>> 어차피 스택메모리에 저장됨
    visited[r][c] = 1
    # 현재 위치에서 에서 갈수 있는 모든 경로 탐색
        #top에서 이동할 수 있는 모든 경로 살펴보기
        # for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
    for d in range(4):
        nr = r+dr[d]
        nc = c+dc[d]
        if 0<= nr < N and 0<= nc < N and arr[nr][nc] and not visited[nr][nc]: #갈 수있음!
            # 방문할 수 있는 위치를 찾았으니 방문
            if dfs(nr,nc,visited):  # 다음 경로에서 목적지에 도착가능하다면
                # 도착할 수 있음을 반환
                return 1

    # for문에서 경로를 찾지 못했다면, 현재 위치에서는 목적지로 갈 수 없음
    return 0
visited = [[0] * N for _ in range(N)]
print(dfs(0,0,visited))










