def func(N,M,result):
    if M == 0:
        return result
    M -= 1
    result *= N
    return func(N,M,result)

for tc in range(1,11):
    T = int(input())
    N,M = map(int,input().split())  # 2 5
    print(f'#{tc} {func(N,M,1)}')

