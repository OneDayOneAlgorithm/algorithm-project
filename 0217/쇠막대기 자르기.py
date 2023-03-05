T = int(input())
for tc in range(1,T+1):
    st = input()
    ans = cnt = 0
    for i in range(len(st)):
        if st[i] == '(':
            cnt += 1
        else:                   # ')' 바로 앞의 기호를 확인해야함
            if st[i-1] == '(':  # 레이저인 경우
                cnt -= 1
                ans += cnt
            else:                # 레이저가 아니라 막대기 끝일 경우
                cnt -= 1
                ans += 1
    print(f'#{tc} {ans}')




























