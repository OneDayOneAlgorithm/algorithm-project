# 7 8
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
V, E = map(int,input().split())
adj = [[0]*(V+1) for _ in range(V+1)]
data = list(map(int,input().split()))
for i in range(0,E*2,2):
    a, b = data[i],data[i+1]
    adj[a][b] = 1
    adj[b][a] = 1
for row in adj:
    print(*row)
# for i in range(E):
#     a,b = data[i*2],data[i*2+1]
####################################
# dfs 시작!
# 갈 수 있는 경로를 발견하면 이동하고,
# 길이 없으면 왔던 길을 되돌아감
# 되돌아가기 위해서 방문 경로를 저장할 거에요
def dfs(start):
    # stack을 이용해서 저장하면 편해요!
    stack = []  # 이름만 stack인 리스트를 만들고 스택처럼 활용
    # 재방문을 막기위해서...visited 배열을 사용합니다.
    visited = [0] * (V + 1)  # [0,1,1,0,0,0,0,0]
    stack.append(start)
    visited[start] = 1
    print(start, end=' ')
    while stack:    # 스택이 비어있지 않으면 계속 반복
        current = stack[-1]
        #현재 노드에서 연결된 노드를 확인
        for i in range(1,V+1):
            if adj[current][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                print(i,end=' ')
                break   # 연결된 노드 찾기 중단
        else:   # for문 수행중 경로 발견 못함!
            stack.pop()

#1번 노드부터 dfs 수행
dfs(3)

