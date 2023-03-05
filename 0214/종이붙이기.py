20*20 으로 먼저 채운다 == 20*10 2가지 가능
다 채운 후 10*10 하나가 남을경우 20*20 갯수 + 1 만큼 한개짜리를 이동시킨다
20*20 하나 줄일때마다 경우의 수 2개 증가

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return 2 * func((n-2))+func(n-1)

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    result = func(n // 10)
    print(f'#{tc} {result}')


























