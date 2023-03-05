n = int(input())
tree = {}                               # tree를 딕셔너리로 만든다
for _ in range(n-1):                    
    a, b = map(int, input().split())    
    if a not in tree:                   # tree에 해당 번호가 없으면
        tree[a] = []                    # 해당 키를 생성한다
    if b not in tree:                   # 한번 더 반복한다
        tree[b] = []
    tree[a].append(b)                   # 서로서로 넣어준다
    tree[b].append(a)
# 각 노드의 부모 노드를 구하는 함수
def find_parent(node, parent, tree):    # 노드, 부모리스트, 트리 입력
    for child in tree[node]:            # 트리 1번 인덱스 값 두개를 반복
        if child != parent:             # 한번도 언급 안된 숫자라면
            parent_list[child] = node   # 부모리스트에 노드입력
            find_parent(child, node, tree)  # 바뀐 노드와 추가된 부모리스트로 재귀함수
# 부모 노드를 저장할 리스트 초기화
parent_list = [0] * (n+1)                   # 부모리스트를 0으로 초기화

# 루트 노드 1에서부터 각 노드의 부모 노드를 찾음
find_parent(1, 0, tree)                     # 함수시작

# 2번 노드부터 마지막 노드까지 부모 노드 출력
for i in range(2, n+1):                     # 2번노드부터 부모출력
    print(parent_list[i])
