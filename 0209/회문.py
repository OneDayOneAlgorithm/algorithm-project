# def BruteForce(p, t):       # BruteForce 함수와 파라미터 p, t
#     M = len(p)
#     N = len(t)
#     i = 0
#     j = 0
#     while j < M and i < N:  #
#         if t[i] != p[j]:
#             i = i - j
#             j = -1
#         i = i + 1
#         j = j + 1
#     if j == M:
#         return i - M
#     else:
#         return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    lst = []
    for _ in range(N):              # 전체 길이만큼 반복
        lst.append(input())         # 리스트에 N개의 문자열 추가 (전체 행만큼)
    for i in range(N):              # 전체 행을 반복
        for j in range(N - M + 1):  # 같은 행에서 N - M + 1 만큼 반복
            for k in range(M // 2): # k를 패턴길이의 절반만큼 반복
                if lst[i][j + k] != lst[i][j + M - k - 1]:  # 대칭 글자가 다르면 즉시종료
                    break
            else:   # 대칭 글자가 다른게 없어서 특정 열에서 시작하는 문자가 회문이면
                print(f'#{tc} {lst[i][j:j + M]}')
    for j in range(N):                      # 전체 열 만큼 반복
        for i in range(N - M + 1):          # 패턴 길이에 따라 한 열에서 몇번 반복문 돌릴 것인지 결정
            lst1 = []                       # 열이 같은 행에 있는 문자를 각각 모으기 위해 빈 리스트 만들기  
            for k in range(M):              # k를 패턴 길이만큼 반복
                lst1.append(lst[i+k][j])    # 리스트에 특정 열에서 M길이의 문자열을 담음
            for l in range(M // 2):         # l을 패턴길이의 절반만큼 반복
                if lst1[l] != lst1[M - 1 - l]:  # lst1의 대칭되는 문자가 다르면 반복종료
                    break
            else:
                result = ''.join(lst1)      # 리스트를 문자열로 바꾸기위해 join함수 사용
                print(f'#{tc} {result}')

