N = int(input())
arr = list(map(int,input().split()))
q = []
for i in range(N):
    q.append((i+1,arr[i]))  #앞에는 인덱스, 뒤에는 벨류를 저장
ans = []    # 정답 리스트
idx = 0 # 최초 인덱스는 0
while len(q) > 1:   # 최종적으로 q가 하나 남았을 때 반복을 종료하고 이후 마지막 1개를 정답 리스트에 넣는다. - 인덱스 에러 방지
    ans.append(q[idx][0])   # 정답 리스트에 인덱스를 넣는다.
    c = q[idx][1]   # 현재 벨류를 c에 저장하고
    q.pop(idx)  # pop해버린다.
    if c > 0:  # 양수일때
        idx = (idx+c-1) % len(q)
    else: # 음수일때
        idx = (idx+c) % len(q)
ans.append(q[0][0])
print(*ans)
