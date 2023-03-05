# def bfs(s):
#     # [0] q, v, 필요한 flag 생성
#     q = []
#     v = [0] * 101
#     ans = s
#
#     # [1] q에 초기데이터(들) 삽입, v표시
#     q.append(s)
#     v[s] = 1
#
#     while q:
#         c = q.pop(0)  # [2] q에서 한개 꺼냄 + 필요시 정답처리
#         if v[ans] < v[c] or v[ans] == v[c] and ans < c: # c가 ans보다 더 멀거나 거리는 같은데 c가 클시
#             ans = c
#
#         # [3] 4/8 연결방향 등 반복처리
#         for n in adj[c]:
#             if v[n] == 0:
#                 q.append(n)
#                 v[n] = v[c] + 1
#     return ans
#
#
# T = 10
# for test_case in range(1, T + 1):
#     N, S = map(int, input().split())
#     lst = list(map(int, input().split()))
#     # [1] 인접리스트에 연결 저장
#     adj = [[] for _ in range(101)]
#     for i in range(0, len(lst), 2):
#         s, e = lst[i], lst[i + 1]
#         adj[s].append(e)
#
#     ans = bfs(S)
#     print(f'#{test_case} {ans}')


def bfs(s):
    q = [s]  # q를 만들고 시작점을 넣는다
    visited[s] = 1  # 시작점 visited에 1을 넣는다 visited가 0이라는 건 방문 안했다는 것
    ans = s  # 일단 이 숫자를 정답이라고 치자
    while q:  # q가 빌 때까지 계속 반복
        c = q.pop(0)  # c에 q 처음 값을 넣는다
        if visited[ans] < visited[c] or visited[ans] == visited[c] and ans < c:  # 길이가 가장 길거나 길이가 같은데 숫자가 크면
            ans = c  # 그 숫자를 정답으로한다
        for i in arr[c]:  # c의 인접배열들을 검색한다
            if visited[i] == 0:  # 인접배열중 방문하지 않은 숫자가 있으면
                visited[i] = 1 + visited[c]  # 그 숫자의 visited에 1대신 1을 더 증가한 값을 넣는다 2.. 3..4..5.. 이렇게 들어간다
                q.append(i)  # 이값을 q에 넣어서 다음 반복문을 준비한다
    return ans  # 반복문이 모두 끝나서 ans가 정해졌으면 이를 출력한다


for tc in range(1, 11):
    N, S = map(int, input().split())  # 총 넣을 숫자의 갯수, 시작점
    arr_input = list(map(int, input().split()))
    arr = [[] for _ in range(101)]  # 인접 배열
    visited = [0] * (101)  # 중복 방지배열
    for idx in range(0, N, 2):
        a, b = arr_input[idx], arr_input[idx + 1]
        arr[a].append(b)  # 인접 배열에 값들을 넣어준다

    print(f'#{tc} {bfs(S)}')
