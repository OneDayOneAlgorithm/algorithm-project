def hex_to_binary(n):
    # 10진수로 변경해서 2진수로 변경
    n = int(n, 16)  # 10진수로 변경하기
    result = ''
    exp = 3
    while n > 0:
        if n >= 2 ** exp:
            result += '1'
            n -= 2 ** exp
        else:
            result += '0'
        exp -= 1

    while len(result) < 4:
        result += '0'
    return result


N, M = map(int, input().split())
# N*M 개의 숫자 배열이 주어짐
lst = [list(input()) for _ in range(N)]
data = []
for i in range(N):
    tmp = ''
    for j in range(M):
        tmp += hex_to_binary(lst[i][j])  # 16진수를 2진수로 바꾸어 붙인다
    data.append(list(map(int, tmp)))  # 이제 data에는 16진수가 2진수로 변환된 값이 들어간다.
print(data)