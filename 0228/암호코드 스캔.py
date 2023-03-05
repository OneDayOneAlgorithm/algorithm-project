import sys

sys.stdin = open('암호코드스캔.txt')

code_num = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}


def solve():
    sum_v = 0
    for i in range(1,N):  # 첫행부터 탐색
        idx = M*4 -1
        while idx > 54:
            if data[i][idx] == 1 and data[i-1][idx] == 0:  # 암호코드의 시작점을 찾으면
                password = []  # 여기에 8개의 암호코드를 담에 정상적인 암호인지 판별한다.
                for _ in range(8):  # 반복 하나당 암호코드 하나를 생성한다.
                    w1 = w2 = w3 = w4 = 0  # 0과 1의 너비를 저장하기 위한 변수
                    while data[i][idx] == 1:  # 1이 계속 나오면 w4 증가 그리고 0이나오면 w3은 그곳에서부터 센다
                        w4 += 1
                        idx -= 1
                    while data[i][idx] == 0:  # 0의 갯수 세기
                        w3 += 1
                        idx -= 1
                    while data[i][idx] == 1:  # 1의 갯수 세기
                        w2 += 1
                        idx -= 1
                    rate = min(w2, w3, w4)  # 가장 작은 값을 찾고 나중에 전체 값에서 그 값을 나눈다
                    w1 = 7 * rate - (w2 + w3 + w4)  # 7의 배수에서 나머지 숫자들을 빼서 w1을 구한다
                    idx -= w1  # 다음 숫자 마지막 1로 위치 옮기기
                    # print(code_num[(w1,w2,w3,w4)], end=' ')
                    w1 //= rate
                    w2 //= rate
                    w3 //= rate
                    w4 //= rate
                    password.append(code_num[(w1, w2, w3, w4)])  # 7개의 숫자 중 1이 있으면 이들을 리스트에 담는다
                odd_nums = password[1] + password[3] + password[5] + password[7]  # 홀수 값들의 합
                even_nums = password[0] + password[2] + password[4] + password[6]  # 짝수 값들의 합
                if (odd_nums * 3 + even_nums) % 10 == 0:  # 홀수*3+짝수 가 10의 배수일시
                    sum_v+= odd_nums + even_nums
            idx -= 1
    return sum_v



def hex_to_binary(n):  # 16진수를 10진수로 바꾸는 코드
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


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N*M 개의 숫자 배열이 주어짐
    lst = [list(input()) for _ in range(N)]
    data = []
    for i in range(N):
        tmp = ''
        for j in range(M):
            tmp += hex_to_binary(lst[i][j])  # 16진수를 2진수로 바꾸어 붙인다
        data.append(list(map(int, tmp)))  # 이제 data에는 16진수가 2진수로 변환된 값이 들어간다.
    result = solve()  # 함수실행
    print(f'#{tc} {result}')  # 출력
