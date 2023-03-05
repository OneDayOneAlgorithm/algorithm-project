T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())

    # 이진 탐색 함수를 만든다.
    def binary(n, key):
        # 반으로 쪼개는 횟수는 1로 초기화
        cnt = 1
        start = 1
        end = n
        while start <= end:
            mid = int((start + end) // 2)
            # print(mid)
            if mid == key:
                return cnt
            elif mid < key:
                start = mid
                cnt += 1
            else:
                end = mid
                cnt += 1
        return -1

    if binary(P, A) < binary(P, B):
        print(f'#{tc} A')
    elif binary(P, A) > binary(P, B):
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')

