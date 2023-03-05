# def bfs(si, sj):
#     q = []  # [0] 생성
#     alst = []
#
#     q.append((si, sj))  # [1] 초기데이터 삽입
#     v[si][sj] = 1
#     alst.append(arr[si][sj])
#
#     while q:
#         ci, cj = q.pop(0)
#
#         # 4방향, 미방문, 조건 맞으면!! (1차이)
#         for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#             ni, nj = ci + di, cj + dj
#             if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and \
#                     abs(arr[ci][cj] - arr[ni][nj]) == 1:
#                 q.append((ni, nj))
#                 v[ni][nj] = 1
#                 alst.append(arr[ni][nj])
#
#     return min(alst), len(alst)
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     v = [[0] * N for _ in range(N)]
#     ans, cnt = N * N, 0
#     for si in range(N):
#         for sj in range(N):
#             if v[si][sj] == 0:
#                 t, tcnt = bfs(si, sj)
#                 if cnt < tcnt or cnt == tcnt and ans > t:
#                     ans, cnt = t, tcnt
#
#     print(f'#{test_case} {ans} {cnt}')


def func(arr):
    global max_v
    dr, dc = [1, -1, 0, 0], [0, 0, -1, 1]
    for r in range(N):
        for c in range(N):
            cr, cc = r, c  # 현재 위치를 정해주고
            cnt = 1  # 카운트를 0으로 초기화 한다
            while True:
                for dir in range(4):  # 4방향으로 이동하고
                    nr, nc = cr + dr[dir], cc + dc[dir]  # 이동 될 위치를 미리 예상한다
                    if 0 <= nc < N and 0 <= nr < N and abs(arr[cr][cc] - arr[nr][nc]) == 1:  # 예상되는 위치가 적합할 때
                        cr, cc = nr, nc  # 그 위치로 이동하고
                        cnt += 1  # 카운트를 센다
                        if max_v < cnt:  # 카운트가 최대값보다 커지면
                            max_v = cnt  # 최대값을 카운트로 설정하고
                            ans = arr[r][c]  # 처음 출발했던 위치의 값을 답으로 설정한다
                        break  # 한번 방향을 이동하면 4 방향을 다시 반복하러간다
                else:
                    break  # 아무 방향으로도 못갔으면 while 반복문을 종료하고 다음 위치에서 시작한다
    return ans,max_v


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    print(f'#{tc}',*func(arr))
