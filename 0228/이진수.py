# 16진수 한 자리 수를 2진수 네자리 수로 변경
def hex_to_binary(n):
    # 10진수로 변경해서 2진수로 변경
    n = int(n,16)   # 10진수로 변경하기
    result = ''
    exp = 3
    while n > 0:
        if n >= 2**exp:
            result += '1'
            n -= 2**exp
        else:
            result += '0'
        exp -= 1

    while len(result) < 4:
        result += '0'
    return result

T = int(input())
for tc in range(1,T+1):
    N, hex_nums = input().split()
    result = ''
    for hex_num in hex_nums:
        result += hex_to_binary(hex_num)
    print(f'#{tc} {result}')