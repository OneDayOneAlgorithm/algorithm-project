def dfs(i):
    visited[i] = 1
    for j in graph[i]:
        if not visited[j]:
            dfs(j)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    for i in range(0,M*2,2):
        graph[arr[i]].append(arr[i+1])
        graph[arr[i+1]].append(arr[i])
    visited = [0] * (N+1)
    cnt = 0
    for i in range(1,N+1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(f'#{tc} {cnt}')