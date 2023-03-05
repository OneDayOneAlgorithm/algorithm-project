T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    number = list(map(int,input().split()))
    cnt = 0
    lst = []
    # 이전 원소보다 1 크지 않으면 초기화 후 다시 카운트
    for i in range(0,N):
        if i > 0: # 아웃 오브 레인지 오류 때문에 넣음
            if number[i] - number[i - 1] != 1:
                cnt = 0
        cnt += 1
        lst.append(cnt)
    # max 함수 대신
    max = lst[0]
    for i in lst:
        if max < i:
            max = i
    print(f'#{tc} {max}')