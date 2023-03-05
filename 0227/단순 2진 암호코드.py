T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6,
            '0111011': 7, '0110111': 8, '0001011': 9}
    for i in range(N):  # 매 행을 반복
        sum_v = 0
        lst = []
        q = 0
        p = 0
        for l in range(M-1,-1,-1):  # 뒤에서 부터검색
            if arr[i][l] == '1':  # 1을 만나면
                for j in range(l-55, l+1, 7):  # 7의 배수로 짜른다 즉 8번 반복
                    lst.append(dict[str(arr[i][j:j+ 7])])  # 암호 숫자를 lst에 담는다
                    if len(lst) == 8:  # 암호숫자가 8개 찰 시
                        for k in range(8):  # 8번 반복해서
                            if k % 2:  # 홀수는
                                q += lst[k]  # 그냥 더하고
                            else:  # 짝수도
                                p += lst[k]  # 그냥 더한후
                        if (p * 3 + q) % 10 == 0:  # 여기서 짝수를 3배한다. 그리고 두 수의 합이 10의 배수이면
                            sum_v = sum(lst)
                            break  # 끝낸다
                        else:
                            sum_v = -1
                            break
            if sum_v != 0:  # sum_v가 정해졌으면
                break  # 끝낸다
        if sum_v != 0:  # sum_v가 정해졌으면
            break  # 끝낸다
    if sum_v == -1:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {sum_v}')
