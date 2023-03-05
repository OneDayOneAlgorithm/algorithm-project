def solve():
    danjo = []  # 빈 리스트를 만들고
    for i in range(0, len(arr) - 1):
        k = 1
        while i + k != len(arr):
            danjo.append((arr[i] * arr[i + k]))  # 빈 리스트에 두수의 곱들을 모두 넣어준다
            k += 1
    danjo.sort()
    danjo = list(map(str,danjo))
    for i in range(len(danjo) - 1, -1, -1):  # 리스트의 맨 뒷값이 가장크니 뒤에서 단조를 찾는다
        right = 0
        for j in danjo[i]:
            if right <= int(j):
                right = int(j)
            else:  # 단조가 아니면
                break  # 반복문을 종료하고 다음 큰 값을 확인한다
        else:  # 단조면
            return danjo[i]  # 이 값을 반환한다
    return -1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = solve()
    print(f'#{tc} {ans}')
