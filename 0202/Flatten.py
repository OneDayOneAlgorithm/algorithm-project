for tc in range(10):
    dump = int(input())
    high = list(map(int, input().split()))
    for j in range(dump):  # dump만큼 반복한다
        max = high[0]
        min = high[0]
        for i in range(len(high)):  # 100번 반복해서 max와 min을 찾는다
            if max < high[i]:
                max = high[i]
            if min > high[i]:
                min = high[i]

        for i in range(len(high)):  # 가장 높은 상자에서 1 뺀다
            if high[i] == max:
                high[i] = max - 1
                break
        for i in range(len(high)):  # 가장 낮은 상자에서 1 뺀다
            if high[i] == min:
                high[i] = min + 1
                break
    max = high[0]
    min = high[0]
    for i in range(len(high)):  # 100번 반복해서 max와 min을 찾는다
        if max < high[i]:
            max = high[i]
        if min > high[i]:
            min = high[i]
    print(f'#{tc + 1} {max - min}')
