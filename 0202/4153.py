while True:
    T = list(map(int, input().split()))
    T.sort()
    if T == [0, 0, 0]:
        break
    elif T[0] ** 2 + T[1] ** 2 == T[2] ** 2:
        print('right')
    else:
        print('wrong')
