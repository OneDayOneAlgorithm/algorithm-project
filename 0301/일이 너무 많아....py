import sys

N = int(sys.stdin.readline())
eleven = list(map(int, ['1' * i for i in range(2, 18)]))
cnt = 0
for i in range(1, N + 1):
    for j in eleven:
        if i % j == 0:
            cnt += 1
            break
print(cnt)
