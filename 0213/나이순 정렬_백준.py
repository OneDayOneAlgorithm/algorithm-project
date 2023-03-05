N = int(input())
dict = {}
for i in range(N):
    arr = list(input().split())
    dict[arr[1]] = arr[0]
print(dict.values())
