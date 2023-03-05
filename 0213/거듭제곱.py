import sys
sys.stdin = open('거듭제곱.txt')
# 이렇게 해도 답이 나올려나
def func(a,b):
    if b == 0:
        return 1
    b -= 1
    return a * func(a,b)
T = 10
for _ in range(1,T+1):
    tc = int(input())
    a,b = map(int,input().split())
    print(f'#{tc} {func(a,b)}')
