def check(arr2, arr3):
    for i in range(len(num_2)):
        if num_2[i] == '1':
            num_2[i] = '0'
            for j in range(len(num_3)):
                if num_3[j] == '1':
                    for k in ['0', '2']:
                        num_3[j] = k
                        if int("".join(num_2), 2) == int("".join(num_3), 3):
                            return int("".join(num_2), 2)
                    num_3[j] = '1'

                if num_3[j] == '2':
                    for k in ['0', '1']:
                        num_3[j] = k
                        if int("".join(num_2), 2) == int("".join(num_3), 3):
                            return int("".join(num_2), 2)
                    num_3[j] = '2'

                if num_3[j] == '0':
                    for k in ['2', '1']:
                        num_3[j] = k
                        if int("".join(num_2), 2) == int("".join(num_3), 3):
                            return int("".join(num_2), 2)
                    num_3[j] = '0'
            num_2[i] = '1'
        else:
            num_2[i] = '1'
            for j in range(len(num_3)):
                if num_3[j] == '1':
                    for k in ['0', '2']:
                        num_3[j] = k
                        if int("".join(num_2), 2) == int("".join(num_3), 3):
                            return int("".join(num_2), 2)
                    num_3[j] = '1'

                if num_3[j] == '2':
                    for k in ['0', '1']:
                        num_3[j] = k
                        if int("".join(num_2), 2) == int("".join(num_3), 3):
                            return int("".join(num_2), 2)
                    num_3[j] = '2'

                if num_3[j] == '0':
                    for k in ['2', '1']:
                        num_3[j] = k
                        if int("".join(num_2), 2) == int("".join(num_3), 3):
                            return int("".join(num_2), 2)
                    num_3[j] = '0'
            num_2[i] = '0'


t = int(input())
for tc in range(1, t + 1):
    num_2 = list(input())
    num_3 = list(input())
    ans = check(num_2, num_3)
    print(f'#{tc} {ans}')