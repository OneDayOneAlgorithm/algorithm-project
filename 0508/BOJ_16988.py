N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
dr = [0,0,-1,1]
dc = [1,-1,0,0]
ans = 0
# 방문기록을 만든다.
visited = [[0]*M for _ in range(N)]
sm = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 2 and not visited[i][j]:
            # 몇수만에 잡을 수 있는지 카운트한다.
            visited[i][j] = -1
            cnt_0 = 0
            # 그 수의 위치를 저장한다.
            p_0 = set()
            # 상대방 돌이 몇개인지 카운트한다.
            cnt_2 = 0
            cnt_2 += 1
            # 얻어걸려서 잡는 상대방 돌을 카운트한다.
            cnt_2_lotto = 0
            q = [(i,j)]
            while q:
                cr,cc = q.pop(0)
                for dir in range(4):
                    nr = cr + dr[dir]
                    nc = cc + dc[dir]
                    if 0<=nr<N and 0<=nc<M and board[nr][nc] != 1 and not visited[nr][nc]:
                        # 빈 땅이고 방문하지 않은 곳이라면
                        if not board[nr][nc]:
                            visited[nr][nc] = -1
                            cnt_0 += 1
                            p_0.add((nr,nc))
                        # 또 상대방 돌이라면
                        else:
                            visited[nr][nc] = -1
                            q.append((nr,nc))
                            cnt_2 += 1
            # 두 수 안에 상대 돌을 잡을 수 있다면
            if cnt_0<=2:
                while p_0:
                    cr,cc = p_0.pop()
                    for dir in range(4):
                        nr = cr + dr[dir]
                        nc = cc + dc[dir]
                        # 상대방을 잡는 위치 상하좌우로 상대방 돌 탐색.
                        # 추가로 얻어걸려서 잡는 경우도 생각한다.
                        if 0<=nr<N and 0<=nc<M and board[nr][nc] == 2 and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            q = [(nr,nc)]
                            while q:
                                cr1,cc1=q.pop(0)
                                for dir in range(4):
                                    nr1 = cr1 + dr[dir]
                                    nc1 = cc1 + dc[dir]
                                    if 0<=nr1<N and 0<=nc1<M and board[nr1][nc1] == 2 and not visited[nr1][nc1]:
                                        visited[nr1][nc1] = 1   
                                        q.append((nr1,nc1))
                                        cnt_2_lotto += 1

                sm = cnt_2 + cnt_2_lotto
        if ans < sm:
            ans = sm
print(ans)
                            