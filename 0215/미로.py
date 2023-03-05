# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [input() for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == '2':
#                 sr = i
#                 sc = j
#     def dfs(sr,sc):
#         stack = [(sr,sc)]                       # 스택에 출발지점 넣고
#         visited = [[0] * N for _ in range(N)]   # visited 는 모두 0으로 만든다
#         visited[sr][sc] = 1                     # visited 에서 1이면 갔던곳
#         dr = [-1,1,0,0]                         # 상하좌우
#         dc = [0,0,-1,1]
#         while stack:                            # 스택에 값이 있으면
#             cr,cc = stack[-1]                   # 현재 위치에 스택을 넣는다
#             if arr[cr][cc] == '3':                # 현재 위치가 3이면
#                 return 1                        # 1 반환 (성공!)
#             for d in range(4):                  # 4방향 벼경
#                 nr = cr+dr[d]                   # 다음 위치 설정
#                 nc = cc+dc[d]
#                 if 0<= nr < N and 0<= nc < N and (arr[nr][nc] != '1') and not visited[nr][nc]:
#                     stack.append((nr,nc))       # 스택에 다음위치 추가
#                     visited[nr][nc] = 1         # 다음위치는 방문한 걸로 함
#                     break
#             else:                               # 이동할 곳이 없으면
#                 stack.pop()                     # 이전 위치로 이동
#         return 0
#
#     print(f'#{tc} {dfs(sr,sc)}')





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                cr,cc = i,j
    stack = []
    stack.append((cr,cc))
    visited = [[0] * N for _ in range(N)]
    result = 0
    while stack:
        cr,cc = stack[-1]
        if arr[cr][cc] == '3':
            result = 1
            break
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if 0<=nr<N and 0<=nc<N and arr[nr][nc] != '1' and not visited[nr][nc]:
                stack.append((nr,nc))
                visited[nr][nc] = 1
                break
        else:
            stack.pop()
    print(f'#{tc} {result}')































