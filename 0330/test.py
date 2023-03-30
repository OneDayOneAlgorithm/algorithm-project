def nqueen(row):
    if row == N:
        return
    # 행 하나에 퀸 놓고나면
    # 다음행에 퀸놓기
    # 퀸놓기 : 모든 열에 퀸을 놓아보기
    for col in range(N):
        if not check_col[col]:
            check_col[col] = 1
            nqueen(row+1)
            check_col[col] = 0


N = int(input())
check_col = [0] * N
nqueen(0)
