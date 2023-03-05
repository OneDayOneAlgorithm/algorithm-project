T = int(input())
for tc in range(1, T + 1):
    arr = input()
    cnt = 0
    for i in arr:
        if cnt == 0 and i == ')':
            print('NO')
            break
        if i == arr[-1] and i == '(':
            print('NO')
            break
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
    else:
        if cnt == 0:
            print('YES')
        else:
            print('NO')
