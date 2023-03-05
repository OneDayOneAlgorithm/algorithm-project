n = int(input())
total_cnt = 0
for i in range(1, 5001):
    cnt = 0
    cnt += n // i  # 그 열로 몇개의 직사각형을 만들 수 있느냐
    if cnt >= i:  # 만약 중복되지 않으면
        total_cnt += cnt - i + 1  # 중복되지 않는 만큼 카운트하라
print(total_cnt)
