T = int(input())

for i in range(1, T + 1):
    A, B = input().split()

    cnt = 0
    idx1 = 0
    idx2 = 0

    while idx1 < len(A):        # idx1이 텍스트길이보다 짧을 때 반복

        if idx2 == len(B):      # 문자열이 들어있으면
            cnt += 1            # 카운트 1
            idx2 = 0            # idx2를 0로 초기화

        if A[idx1] != B[idx2]:  # A와 B가 다르면
            idx1 += 1           # A
            idx2 = 0            # idx2 초기화
            cnt += 1            # cnt
        else:                   # A와 B가 같으면
            idx1 += 1           # 인덱스들 증가
            idx2 += 1

    if B not in A:
        idx2 = 0

    if idx2 == len(B):
        cnt += 1

    elif idx2 > 0:
        cnt += idx2
    else:
        cnt = len(A)

    print(f'#{i} {cnt}')