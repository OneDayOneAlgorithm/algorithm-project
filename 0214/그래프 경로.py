import sys
sys.stdin = open('그래프 경로.txt')

def dfs(start):
    stack = []               # 빈 리스트 생성
    visited = [0] * (V + 1)  # 재방문을 막기 위함
    stack.append(start)      # 스택에 시작지점 푸쉬
    visited[start] = 1       # 방문한 번호에 해당하는 visited 인덱스에 1 푸쉬
    lst.append(start)
    while stack:             # 스택에 값이 있으면 반복문 시행
        current = stack[-1]  # 현재 위치는 스택에 저장된 마지막 값
        # 재 노드에서 연결된 노드를 확인
        for i in range(1,V+1):                      # 모든 노드번호에 대하여
            if board[current][i] and not visited[i]:  # 해당 노드번호와 현재 위치가 이어져 있으면 그리고 방문한 적이 없으면
                stack.append(i)                     # 스택에 해당 노드번호 푸쉬
                visited[i] = 1                      # visited 에도 푸쉬
                lst.append(i)
                break                               # 반복문 종료하고 다시 모든 노드에 대해 반복
        else:                                       # 더이상 어떤 노드와도 연결할 수 없다면
            stack.pop()                             # 스택 마지막부터 팝 (스택이 빌 때까지)
T = int(input())
for tc in range(1,T+1):
    lst = []
    V, E = map(int,input().split()) # V개의 노드를 E개의 간선으로 연결
    board = [[0] * (V+1) for _ in range(V+1)]
    for _ in range(E):
        a,b = map(int,input().split())
        board[a][b] = 1
    start,goal = map(int,input().split())
    dfs(start)
    cnt = 0
    if goal in lst:
        cnt = 1
    if cnt == 1:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')




























