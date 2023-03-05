T = int(input())
for tc in range(T):
    word = input()
    words = input()
    if word in words:
        print(f'#{tc + 1} 1')
    else:
        print(f'#{tc + 1} 0')