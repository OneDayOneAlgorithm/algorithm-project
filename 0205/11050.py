N, K = map(int,input().split())
result = 1
div = 1
for i in range(N, N - K, -1):
    result *= i
for i in range(1, K + 1):
    div *= i
print(result // div)