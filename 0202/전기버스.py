T = int(input())
for tc in range(T):
    K, N, M = map(int, input().split())  # 이동횟수, 종점, 충전기
    number = list(map(int, input().split()))
    now = 0
    cnt = 0
    back = False
    while now + K < N:
        if back == True:
            break
        for i in range(K, 0, -1):
            if (now + i) not in number:  # 갔는데 충전소가 없으면
                if i == 1:  # 이동거리가 1인데도 충전소가 없으면
                    back = True  # 끝내는 변수에 True할당
                    break
                continue  # 돌아가서 K를 1 줄여라
            else:   # 충전소가 있으면 아래 시행하고 다시 while
                cnt += 1
                now += i
                break
    if back == True:
        print(f'#{tc+1} 0')
    else:
        print(f'#{tc+1} {cnt}')
