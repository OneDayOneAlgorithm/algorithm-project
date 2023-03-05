def bf(p, t):   # 브루트함수만들기
    N = len(t)
    M = len(p)
    cnt = 0
    i = 0
    while i < N-M+1:            # 전체길이 - 패턴길이 + 1
        for j in range(M):      # 패턴길이
            if t[i+j] != p[j]:  # 전체에서 글자 != 패턴에서 글자 이면
                i += 1          # i 증가시키고
                break
        else:                   # 일치하면
            cnt += 1            # 카운트 증가와
            i += M              # 패턴길이만큼 i 점프
    return cnt


T = int(input())
for tc in range(1, T + 1):
    A, B = input().split()
    cnt1 = bf(B, A)             # A에 B단어가 몇개 있는지 세기
    new_A = A.replace(B, '')    # A에서 B를 제거
    cnt = len(new_A)            # A에서 문자 갯수 세기
    print(f'#{tc} {cnt + cnt1}')  # 이 둘을 더하기
