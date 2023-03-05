T = int(input())
for tc in range(1, T + 1):
    word = input()
    N = len(word) // 2  # 반 짜른다 가운데 글자가 있으면 자동 제외시켜 줌
    for i in range(N):
        if word[i] != word[-1-i]:  # 대칭 단어가 다르면 0 출력
            print(f'#{tc} 0')
            break
    else:
        print(f'#{tc} 1')   # 대칭 단어가 다른게 없으면 1 출력
