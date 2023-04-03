from collections import deque
def bfs():
    visited = [0] * 10000000
    q = deque()
    q.append(N)

    cnt = 0
    while q:
        for i in range(len(q)):
            c = q.popleft()
            if c == M:
                return cnt
            dc = [1, -1, -10]
            for dir in range(3):
                nc = c + dc[dir]
                if visited[nc] or nc<=0 or nc > 1000000:
                    continue
                q.append(nc)
                visited[nc] = 1
            nc = c * 2
            if visited[nc] or nc<=0 or nc > 1000000:
                continue
            q.append(nc)
            visited[nc] = 1
        cnt += 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs()}')
