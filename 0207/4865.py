
T = int(input())
for tc in range(1, T + 1):
    word = input()
    word2 = input()
    lst = list(set(word))
    cnt = [0] * len(lst)
    for i in range(len(lst)):  # 0
        for j in word2:    # E O G G
            if j == lst[i]:
                cnt[i] += 1

    max_1 = cnt[0]
    for i in cnt:
        if max_1 < i:
            max_1 = i
    print(f'#{tc} {max_1}')
