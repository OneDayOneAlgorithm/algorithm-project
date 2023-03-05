# def func(data):
#     global cnt
#     cnt += 1
#     heap[cnt] = data
#     parent = cnt // 2
#     current = cnt
#     while heap[current] < heap[parent]:
#         heap[current],heap[parent] = heap[parent],heap[current]
#         current = parent
#         parent = current // 2
#
# def func2(N):
#     global sum
#     if N == 0:
#         return
#     func2(N // 2)
#     sum += heap[N]
#
#
# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     cnt = 0
#     heap = [0] * (N+1)
#     sum = 0
#     for i in arr:
#         func(i)
#     func2(N//2)
#
#     print(f'#{tc} {sum}')
#

def solve1(n):
    global cnt, sum_v
    cnt += 1
    tree[cnt] = n
    current = cnt
    parent = current // 2
    while tree[current] < tree[parent]:
        tree[current], tree[parent] = tree[parent], tree[current]
        current = parent
        parent = parent // 2


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (N + 1)
    cnt = sum_v = 0
    for i in arr:
        solve1(i)
    num = N
    while num > 0:
        num = num // 2
        sum_v += tree[num]
    print(f'#{tc} {sum_v}')
