def wall(cnt):  # 벽을 3개 놓는 함수 wall()
    if cnt == 3:  # 벽을 3개 놓을 시
        bfs()  # 바이러스를 전파시키고 안전영역을 구하는 함수 bfs() 실행
        return  # 종료하고 다른 위치에 벽 3개 설치
    for i in range(N):  # 지도의 가로 세로를 순환하며
        for j in range(M):  # 지도의 가로 세로를 순환하며
            if arr[i][j] == 0:  # 빈칸에
                arr[i][j] = 1  # 벽을 1개 설치
                wall(cnt + 1)  # 함수 wall()을 사용하여 벽을 총 3개 설치
                arr[i][j] = 0  # 벽을 새로 설치하기 위해 설치한 벽을 제거


def bfs():  # 바이러스를 전파시키고 안전영역을 구하는 함수 bfs()
    global maxv  # maxv의 값을 마음대로 변경시키기 위해 global 명령어 사용
    copy = [[0] * M for _ in range(N)]  # 바이러스를 전파시키고 안전영역을 세기 위해 지도의 복사본을 생성
    for i in range(N):  # 바이러스를 전파시키고 안전영역을 세기 위해 지도의 복사본을 생성
        for j in range(M):  # 바이러스를 전파시키고 안전영역을 세기 위해 지도의 복사본을 생성
            copy[i][j] = arr[i][j]  # 바이러스를 전파시키고 안전영역을 세기 위해 지도의 복사본을 생성
    cnt = 0  # 현재 3개의 벽에 대한 안전영역의 갯수를 저장하는 변수 result
    q = []  # 바이러스들의 좌표를 저장하는 배열 q
    for i in range(N):  # q에 최초 바이러스의 좌표를 저장
        for j in range(M):  # q에 최초 바이러스의 좌표를 저장
            if copy[i][j] == 2:  # q에 최초 바이러스의 좌표를 저장
                q.append((i, j))  # q에 최초 바이러스의 좌표를 저장
    while q:  # queue와 델타기법을 사용해 바이러스를 퍼뜨린다.
        cr, cc = q.pop(0)  # 현재 좌표에 q의 맨 앞에 저장된 값을 할당한다.
        for dir in range(4):  # 현재 좌표에서부터 상하좌우로 한 칸씩 이동한다.
            nr = cr + dr[dir]  # 현재 좌표에서부터 상하좌우로 한 칸씩 이동한다.
            nc = cc + dc[dir]  # 현재 좌표에서부터 상하좌우로 한 칸씩 이동한다.
            if 0 <= nr < N and 0 <= nc < M and not copy[nr][nc]:  # 맵 안이고 빈칸이라는 조건 하에 이동한다.
                copy[nr][nc] = 2  # 이동한 위치에 바이러스를 퍼뜨리고
                q.append([nr, nc])  # 이동한 위치를 q에 저장한다.
    for i in range(N):  # 지도의 가로 세로를 순환하며 빈칸의 갯수를 센다.
        for j in range(M):  # 지도의 가로 세로를 순환하며 빈칸의 갯수를 센다.
            if copy[i][j] == 0:  # 지도의 가로 세로를 순환하며 빈칸의 갯수를 센다.
                cnt += 1  # 지도의 가로 세로를 순환하며 빈칸의 갯수를 센다.
    if maxv < cnt:  # result가 maxv보다 크면
        maxv = cnt  # maxv에 result를 할당한다.


import sys

N, M = map(int, sys.stdin.readline().split())  # 세로크기 N과 가로크기 M
arr = [list(map(int, input().split())) for _ in range(N)]  # 지도의 모양 arr
dr = [0, 0, -1, 1]  # 좌 우 상 하
dc = [-1, 1, 0, 0]  # 좌 우 상 하
maxv = 0  # 안전영역의 최대 크기 maxv
wall(0)  # 벽을 3개 놓는 함수 wall()
print(maxv)  # 안전영역의 최대 크기 maxv 출력
