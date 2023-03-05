N = int(input())
arr = 0
for i in range(N):
    arr += 1
    while '666' not in str(arr):
        arr += 1
print(arr)