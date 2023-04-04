TC = int(input())
for tc in range(1, TC+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    for i in range(E):
        s, e, value = map(int, input().split())
        adj[s].append([e, value])

    distance = [9999999] * (V+1)
    selected = [0] * (V+1)

    distance[0] = 0
    cnt = 0
    while cnt < V:
        min = 9999999
        for i in range(V+1):
            if not selected[i] and distance[i] < min:   # 인접해 있는 노드라면
                min = distance[i]           # 너로 정했다
                u = i                       # v에 정한 노드 할당
        # 이제 시작 노드를 결정했다
        selected[u] = 1  # 방문기록을 한다.
        cnt += 1            # 방문 노드 갯수 카운트
        # 간선완화
        for w, cost in adj[u]:  # 도착정점, 가중치
            if distance[w] > distance[u] + cost:
                distance[w] = distance[u] + cost
    print(f'#{tc} {distance[V]}')