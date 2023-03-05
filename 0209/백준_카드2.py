from collections import deque
N = int(input())
num = deque([i for i in range(1, N+1)])

while (len(num) > 1):
    num.popleft()
    p = num.popleft()
    num.append(p)
print(num[0])
