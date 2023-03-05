T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    set_str1 = set(str1)  # 셋으로 만들어 중복 글자 제거
    str1 = str(set_str1)  # 다시 문자열로 만들기
    max = 0
    for i in str1:  # str1 중 하나 고른다
        max2 = 0            #
        for j in str2:  # 방금 고른 문자가 str2에 몇개 있는지 세기
            if i == j:
                max2 += 1
        if max < max2:  # 그 중 가장 많은 횟수 max에 저장
            max = max2
    print(f'#{tc} {max}')
