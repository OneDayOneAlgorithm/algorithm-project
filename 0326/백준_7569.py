from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
def bfs():  # bfs 함수 시작
    while q:    # q 가 빌 때까지 실행
        cx, cy, cz = q.popleft()        # 현재 cx, cy, cz 에 값을 할당 (c는 current)
        visit[cz][cx][cy] = 1          # 현재 cx, cy, cz 방문 표시
        for dir in range(6):          # 모든 방향으로 이동
            nx = cx + dx[dir]
            ny = cy + dy[dir]
            nz = cz + dz[dir]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and board[nz][nx][ny] == 0 and visit[nz][nx][ny] == 0:   # 범위 안 이거나 안썩은 토마토이거나 방문을 안한 곳일 시
                q.append([nx, ny, nz])     # q에 추가하고
                board[nz][nx][ny] = board[cz][cx][cy] + 1  # 그 전파된 값에 전의 값보다 1을 증가시킨 값을 넣는다.
                visit[nz][nx][ny] = 1   # 그리고 방문표시를 한다.
m, n, h = map(int, input().split())     # 가로, 세로, 높이를 입력을 받는다.
board = [[] for i in range(h)]  # h층으로 이루어진 빈 리스트를 만든다.
visit = [[[0 for i in range(m)] for i in range(n)] for i in range(h)]   # x,y,z 3중 배열인 방문기록을 만든다.
q = deque()  # q를 사용할 것이므로 deque()를 만들어준다.
isTrue = False  # 나중에 이것이 True로 바뀌면 벽으로 갇혀서 썩지 않은 토마토가 생긴다는 의미다. 그때는 결과값으로 -1을 츨력한다.

for i in range(h):  # 매 높이마다
    for j in range(n):  # 매 행마다
        board[i].append(list(map(int, input().split())))    # 입력을 해준다.
for z in range(h):  # 매 높이와
    for x in range(n):  # 매 행과
        for y in range(m):  # 매 열을 순환하여
            if s[z][x][y] == 1: # 토마토를 찾으면
                q.append([x, y, z]) # 그 좌표를 q에 넣는다.
bfs()   # bfs 함수 실행
max_num = 0     # 몇번 만에 토마토가 모두 썩었는지를 세는 변수. 초기값은 0
for z in range(h):  # 매 높이와
    for x in range(n):  # 매 행과
        for y in range(m):  # 매 열을 순환하여
            if s[z][x][y] == 0: # 안썩은 토마토를 발견 시
                isTrue = True   # isTrue를 True로 바꾼다.
            max_num = max(max_num, board[z][x][y])  # 이와는 별개로 일단 몇번만에 토마토가 모두 썩는지 카운트 한다.
if isTrue == True:  # isTrue가 True 일 시
    print(-1)   # -1 출력
else:   # isTrue가 False 일 시


    33

    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3
    3















    
    print(max_num - 1)  # 몇번만에 토마토가 모두 썩었는지 출력