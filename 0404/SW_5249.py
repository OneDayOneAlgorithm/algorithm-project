def prim(start):
    mst = set()  # 노드의 번호가 들어간다.
    weight = [9999999999] * (V + 1)  # 각 노드의 거리 값을 엄청 크게 만들어 놓는다.
    weight[start] = 0  # 시작지점의 거리 값을 0으로 저장한다.
    while len(mst) < V + 1:  # 모든 노드가 mst에 들어가면 종료한다.
        min_v = 999999999   # 곧 검사할 노드의 거리 값과 비교할 min의 값을 엄청 크게 만들어 놓는다.
        for i in range(V + 1):  # 모든 노드를 검사한다.
            if i not in mst and weight[i] < min_v:  # 사용한 적 없는 노드이고 연결이 된 노드이면 (거리값이 9999999999이면 연결이 안된 상태)
                min_v = weight[i]   # 그 거리값을 min_v에 저장하여 이번 반복문에서 사용한다.
                min_idx = i # 그 노드의 번호를 min_idx에 저장하여 이번 반복문에서 사용한다.
        mst.add(min_idx)    # 그 노드를 mst에 추가해서 다음 반복문 부터는 사용하지 않는다.
        for i in range(V + 1):  # 해당 노드와 연결되어 있는 모든 노드를 검사한다.
            if i not in mst and adj[min_idx][i] and weight[i] > adj[min_idx][i]:    # 연결된 노드 중 사용하지 않은 노드이고 거리를 단축시킬 수 있는 노드면
                weight[i] = adj[min_idx][i] # 그 거리 값을 weight에 저장한다.
    return weight   # 최종 적으로 모든 노드들의 거리 값을 출력한다.

T = int(input())
for tc in range(1,T+1):
    V, E = map(int, input().split())    # 노드와 간선의 갯수 입력
    adj = [[0] * (V + 1) for _ in range(V + 1)] # 인접행렬 생성
    for _ in range(E):  # 간선입력
        a, b, w = map(int, input().split()) # 간선을 잇는 두 노드와 간선의 길이 입력
        adj[a][b] = w   # 인접행렬에서 해당 좌표에 간선의 길이 입력
        adj[b][a] = w
    result = prim(0)    # 출발 노드를 0으로 잡고 prim 함수를 시작한다.
    print(f'#{tc} {sum(result)}')   # 결과 값으로는 모든 노드가 연결된 각각의 간선의 길이가 나온다.
