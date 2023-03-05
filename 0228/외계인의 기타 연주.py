import sys
N, P = map(int, sys.stdin.readline().split())
arr = [[0] * (P + 1) for _ in range(7)] # 7개의 행과 프렛개의 열
stack = [[] for _ in range(7)]
cnt = 0
for i in range(N):  # 음의 수만큼 반복
    a, b = map(int, sys.stdin.readline().split())    # 줄의번호, 프렛번호
    while stack[a] and stack[a][-1] > b:
        stack[a].pop()
        cnt += 1
    if not stack[a] or stack[a][-1] != b:
        stack[a].append(b)
        cnt += 1
print(cnt)
