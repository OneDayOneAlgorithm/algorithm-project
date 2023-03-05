N = int(input())
A = list(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))
cnt = [0] * N
for i in A:
    cnt[i - 1] += 1
print(cnt)
