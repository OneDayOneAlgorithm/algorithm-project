# 10진수 소수점 2진수로 표현하기
# 2를 곱해가면서 자연수부가 1이면 1, 0이면 0
T = int(input())
for tc in range(1, T + 1):
    # 소수점 입력이 주어짐
    N = float(input())
    # 2곱하고 결과 보기...
    result = ''
    while N > 0:
        if len(result) == 13:
            #더 이상 수행할 필요가 없음...overflow
            result = 'overflow'
            break
        N = N * 2
        if N >= 1:
            result += '1'
            N -= 1
        else:
            result += '0'
    print(f'#{tc} {result}')
