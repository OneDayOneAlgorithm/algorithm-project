T = int(input())  # 테스트 케이스 입력
for tc in range(1, T + 1):  # 테스트 케이스 검사
    N = int(input())  # 몇곱하기 몇행렬인지 검사
    graph = [list(map(int, input().split())) for _ in range(N)]  # 맵 입력
    new_graph = [[999999] * N for _ in range(N)]  # 새로운 맵 입력
    dr = [0, 0, 1, -1]  # 상하
    dc = [1, -1, 0, 0]  # 좌우 이동 커맨드 생성
    q = [(0, 0)]  # q 에 처음 좌표 넣기
    new_graph[0][0] = 0  # 처음 좌표는 0으로 시작한다 (잘 읽어 보면 그럼)
    while q:  # q에 있는 좌표를 다 쓰면 종료. 적은 연료가 나오면 q에 값을 넣는다. 큰 연료가 나오면 q에 값을 안넣는다. 반복하다 보면 q가 비게 된다.
        cr, cc = q.pop(0)  # q 맨앞에 있는 좌표를 사용해서 반복문을 돌린다.
        for dir in range(4):  # 상하좌우로 움직인다.
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if 0 <= nr < N and 0 <= nc < N:  # 맵 안에 있는 좌표라면
                if graph[nr][nc] > graph[cr][cc]:  # 움직인 위치와 움직이기 전 위치를 비교해서 움직인 위치가 높은 지대라면
                    value = 1 + (graph[nr][nc] - graph[cr][cc]) + new_graph[cr][cc]  # 기본 기름값 1 + 높이차이 기름값 + 누적 기름값 을 계산하고
                else:  # 움직인 위치가 낮은 지대라면
                    value = 1 + new_graph[cr][cc]   # 기본 기름값 1 + 누적 기름값 을 계산한다.
                if value < new_graph[nr][nc]:   # 경로마다 이 좌표의 벨류값은 제각각 다르다. 이 계산된 벨류값이 더 효율이 좋다면
                    new_graph[nr][nc] = value   # 이 계산된 벨류값을 넣는다.
                    q.append((nr, nc))          # 그리고 q에도 넣는다.
    print(f'#{tc} {new_graph[N - 1][N - 1]}')   # 최종 좌표에 누적값이 있으므로 이를 출력한다.
