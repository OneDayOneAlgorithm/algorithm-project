import sys
sys.stdin = open('길찾기.txt')

def dfs(start):
    stack = []
    visited = [0] * 100
    stack.append(start)
    visited[start] = 1
    # print(start, end=' ')
    while stack:    # 스택이 비어있지 않으면 계속 반복
        current = stack[-1]
        #현재 노드에서 연결된 노드를 확인
        for i in range(1,100):
            if 99 in stack:
                return 1
            if adj[current][i] and not visited[i]:
                stack.append(i)
                visited[i] = 1
                # print(i,end=' ')
                break   # 연결된 노드 찾기 중단
        else:   # for문 수행중 경로 발견 못함!
            stack.pop()
for _ in range(10):
    tc, E = map(int,input().split()) # 테스트케이스, 길의 총갯수
    adj = [[0]*(100) for _ in range(100)]
    data = list(map(int,input().split()))
    for i in range(0,E*2,2):
        a, b = data[i],data[i+1]
        adj[a][b] = 1
    if dfs(0) == 1:
        print(f'#{tc} {1}')
    else:
        print(f'#{tc} {0}')

