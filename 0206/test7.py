arr = ['a', 'b', 'c']
N = 3
for i in range(1 << N):
    for j in range(N):
        if i & (1 << j) != 0:  # 이 자리 비트는 1이므로
            print(arr[j], end=',')
    print('')
