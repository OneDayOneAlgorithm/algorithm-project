arr = [1,2,3,4,5]
N = len(arr)
#idx 번째 요소를 조합에 포함할지 안 할지 결정
selected = [0] * N

# cnt = 여태까지 선택한 요소의 개수
def comb(idx, cnt):
    if cnt == K:
        print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i], end=' ')
        print()
        return
    if idx == N:    #마지막 인덱스까지 모두 결정했으나 K를 선택하지 못함
        return

    #내가 할 수 있는거 다 해보기
    for i in range(1,-1,-1):
        selected[idx] = i
        #요소를 선택하면 +1
        comb(idx + 1,cnt + 1*i)
        # selected[idx] = 0


    # selected[idx] = 1
    # #요소를 선택하면 +1
    # comb(idx + 1,cnt + 1)
    #
    # selected[idx] = 0
    # # 요소를 선택하면 +1
    # comb(idx + 1, cnt)

K = 3   # N개 중에 K개 선택해라
comb(0,0)