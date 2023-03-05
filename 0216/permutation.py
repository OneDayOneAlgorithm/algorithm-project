arr = [1,2,3]
N = len(arr)
perm_arr = [0] * N
used = [0] * N


# idx번째에 넣을 수 있는 숫자 다 넣기
def perm(idx):
    #마지막 인덱스 까지 모두 선택했으면 출력하기
    if idx == N:    
        print(perm_arr)
        return

    #해당 idx에 넣을 수 있는 모든 경우의 수 넣어보기 
    for i in range(N):
        if not used[i]: # 이전 인덱스에서 사용하지 않았으면 사용하기
            perm_arr[idx] = arr[i]
            used[i] = 1     # 사용했음을 표시
            perm(idx+1)     # 다음 인덱스 숫자 선택하기
            used[i] = 0     # 다음 수를 사용할테니..사용한 표시 없애주기
# 0번 인덱스 부터 숫자 선택하기
perm(0)
