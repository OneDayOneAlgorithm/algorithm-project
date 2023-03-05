A = [1, 2, 3, 4]
bit = [0, 0, 0, 0]
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit, end='')
                s = 0
                for p in range(4):
                    if bit[p]:
                        print(A[p], end=' ')
                        s += A[p]
                print()
