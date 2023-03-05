import sys

sys.stdin = open('암호코드스캔.txt')

hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101',
    '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}
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
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    bin_data = []

    # 기존 16진수 문자열을 2진수 문자열로 바꿔주기
    for i in range(N):
        bin_line = ''
        for j in range(M):
            bin_line += hex_to_bin[data[i][j]]
        bin_data.append(bin_line)
    data = bin_data
    # for row in bin_data:
    #     print(row)
    # print('===========================================================')
    # 2진수 문자열로 바꿨으니...단순2진 암호코드와 비슷하게 시작
    # 뒤에서 부터 1찾기
    result = 0  # 정상 암호코드를 모두 더하기 위한 변수 선언(결과)
    for i in range(1, N):
        # 16진수를 2진수로 바꾸면서 길이가 4배로 늘어남..마지막 인덱스 : M*4-1
        idx = M * 4 - 1
        # 근데.. 한 번 찾으면 끝이 아니라 같은 줄에 또다른 코드가 있을 수 있음
        # 그래서 인덱스 조절 해가면서 다시 찾아야 하는데, for문은 인덱스 조절이 안됨
        # while문 사용
        while idx > 54:
            # 근데 1인녀석을 모조리 찾아버리면....윗줄 동일한 코드도 중복계산됨..그래서
            # 암호코드 중에서 제일 위에 있는 녀석만 찾아야함 data[i-1][idx] == '0' >> 윗줄이 0임
            if data[i - 1][idx] == '0' and data[i][idx] == '1':  # 암호 끝자리 찾음...8자리 숫자 찾는건 단순 2진 암호코드와 동일
                password = []
                for _ in range(8):
                    w1 = w2 = w3 = w4 = 0
                    while data[i][idx] == '1':
                        w4 += 1
                        idx -= 1
                    while data[i][idx] == '0':
                        w3 += 1
                        idx -= 1
                    while data[i][idx] == '1':
                        w2 += 1
                        idx -= 1
                    # 단순 2진 암호코드와는 다르게, 너비가 7로 고정되어 있지 않음
                    # 따라서 암호코드 너비가 몇인지 계산해야 한다.
                    # 비율중에 가장 작은 값이 확대된 배수(1이 항상포함됨 ex:3211)
                    rate = min(w2, w3, w4)
                    w2 //= rate
                    w3 //= rate
                    w4 //= rate
                    w1 = 7 - w2 - w3 - w4
                    idx -= w1 * rate  # 최종 0개수만큼 이동
                    password.append(code_num[(w1, w2, w3, w4)])
                # 숫자 8개 암호코드를 찾음
                # 정상 암호코드인지 확인
                # 찾았다고 바로 끝내는 것이 아니라 저장해야 함. 모든 정상 암호 코드를 더해야 함
                odd_nums = password[1] + password[3] + password[5] + password[7]
                even_nums = password[0] + password[2] + password[4] + password[6]
                # print(odd_nums,even_nums)
                # 홀수자리*3 + 짝수자리 => 10의 배수이면 정상 >> 모든자리 합반환
                if (odd_nums * 3 + even_nums) % 10 == 0:
                    result += (odd_nums + even_nums)
                # 아니라면 비정상 >>> 0 반환
            idx -= 1  # 다 검사했으니 1 감소
    print(f'#{tc} {result}')