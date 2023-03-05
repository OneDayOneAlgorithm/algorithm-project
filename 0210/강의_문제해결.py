# # 빈칸에 글자 넣기
# def count(arr):
#     ans = 0
#     for lst in arr:
#         cnt = 0
#         for n in lst:
#             if n == 1:  # 단어를 넣을 수 있는 공백
#                 cnt += 1
#             else:       # 칸 없음!
#                 if cnt == K:
#                     ans += 1
#                 cnt= 0
#     return ans
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N, K = map(int, input().split())
#
#     # arr와 arr_t 로 각각 개수를 계산
#     arr = [list(map(int, input().split())) + [0] for _ in range(N)] + [[0]*(N+1)]
#     arr_t = list(zip(*arr)) # 튜플형태를 리스트 형태로 만든다
#     print(f'#{test_case} {ans}')

# 스도쿠 검증

# def solve(arr):
#     for lst in arr:             # 행을 체크
#         if len(set(lst))!=9:    # 스토쿠 실패
#             return 0
#     arr_t = list(zip(*arr))
#     for lst in arr_t:           # 열을 체크
#         if len(set(lst))!=9:    # 스토쿠 실패
#             return 0
#     for i in (0,3,6):
#         for j in (0,3,6):       # 3*3 격자
#             lst = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+1][j:j+3]
#             if len(set(lst))!=9:
#                 return 0
#     return 1


# 숫자 배열 회전
# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = [input().split() for _ in range(N)]
#     a1 = [[0] * N for _ in range(N)]    # 90도
#     a2 = [[0] * N for _ in range(N)]
#     a3 = [[0] * N for _ in range(N)]
#
#
#     # # [1]회전각도에 따른 위치값을 저장
#     for i in range(N):
#         for j in range(N):
#             a1[i][j] = arr[N-1-j][i]
#             a2[i][j] = arr[N-1-i][N-1-j]
#             a3[i][j] = arr[j][N-1-i]
#     print(f'#{tc} {arr}')
#     for a,b,c in zip(a1,a2,a3):
#         print(f'{"".join(a)} {"".join(b)} {"".join(c)}')


# 사다리타기
# T = 10
# for tc in range(1, T + 1):
#     _ = int(input())
#     arr = [[0] + list(map(int,input().split()))]
#     mn = 100*100
#     for sj in range(1,101):
#         si, cnt, dj = 0,0,0
#         if
#     print(f'#{tc}')


# 회문2
for tc in range(1,11):
    M = int(input())
    N = 8
    board = [input() for _ in range(8)]
    result = 0
    for i in range(8):      # 행 순회
        for j in range(N - M + 1):  # 열 순회
            # 회문검사 : 회문의 전체 길이의 절반만 검사
            for k in range(M // 2):
                if board[i][j+k] != board[i][j+M-1-k]:
                    break
        else:
            result += 1

    for j in range(8):  # 행 순회
        for i in range(N - M + 1):  # 열 순회
            # 회문검사 : 회문의 전체 길이의 절반만 검사
            for k in range(M // 2):
                if board[i + k][j] != board[i + M - 1 - k][j]:
                    break
        else:
            result += 1
    print(f'#{tc} {result}')















