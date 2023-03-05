import sys
sys.stdin = open('GNS_test_input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = input()
    words = list(input().split())
    N_len = int(N[3:])
    dict = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}
    lst = []
    for i in range(N_len):
        lst.append(dict[words[i]])  # lst에 7040개의 숫자 값을 추가
    # lst.sort()
    for i in range(N_len):
        min_idx = i
        for j in range(i + 1, N_len):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]

    lst_2 = []
    for i in lst:
        for j in dict:
            if i == dict[j]:
                lst_2.append(j)

    print(f'#{tc}')
    print(*lst_2)
