T = int(input())
for tc in range(1,T+1):
    arr = input()
    lst = [arr[0]]
    lst2 = []
    same = 0
    compare = 1
    for i in range(1,30):
        if arr[i] == lst[i-compare]:
            same += 1
            lst2.append(arr[i])
            if same == compare:
                ans = compare
                break
        else:
            lst = lst + lst2
            lst2 = []
            lst.append(arr[i])
            compare += 1
            compare += same
            same =0
    print(f'#{tc} {ans}')