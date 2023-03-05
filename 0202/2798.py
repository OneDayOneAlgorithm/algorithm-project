N, M = map(int, input().split())
number = list(map(int, input().split()))
number.sort(reverse=True)  # 카드들을 오름차순으로 정렬
lst = []
for i in range(N):  # N개의 카드
    for j in range(N):
        if j != i:
            for k in range(N):
                if k != i and k != j:
                    sum = number[i] + number[j] + number[k]
                    if sum <= M:
                        lst.append(sum)
print(max(lst))
