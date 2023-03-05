T = int(input())
for tc in range(1,T+1):
    board = [0]*4
    arr = input()
    lst =[]
    for i in range(0,len(arr),3):
        lst.append(arr[i:i+3])
        if arr[i] == 'S':
            board[0] += 1
        elif arr[i] == 'D':
            board[1] += 1
        elif arr[i] == 'H':
            board[2] += 1
        else:
            board[3] += 1
    a,b,c,d = 13-board[0],13-board[1],13-board[2],13-board[3]
    if len(lst) != len(set(lst)):
        print(f'#{tc} ERROR')
    else:
        print(f'#{tc} {a} {b} {c} {d}')