T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    cnt = 0
    for i in range(len(str2) - len(str1) + 1):  # str2의 길이가 4고 str1의 길이가 4면 1번반복
        if str1 == str2[i: i + len(str1)]:  # 일치하는게 있을시 카운트 + 1
            cnt += 1
    print(f'#{tc} {cnt}')
