T = int(input())
for tc in range(1, T + 1):
    str1 = list(input())
    N = int(len(str1) // 2)  # 절반 나누기
    for i in range(len(str1)):  # 거울형으로 바꾸기
        if str1[i] == 'b':
            str1[i] = 'd'
        elif str1[i] == 'd':
            str1[i] = 'b'
        elif str1[i] == 'p':
            str1[i] = 'q'
        else:
            str1[i] = 'p'
    for i in range(N):
        str1[i], str1[-1-i] = str1[-1-i], str1[i]  # 앞뒤 거울위치 바꾸기
    result = ''.join(str1)  # 리스트를 문자열로
    print(f'#{tc} {result}')
