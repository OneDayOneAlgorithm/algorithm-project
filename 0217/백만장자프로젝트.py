T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    i = 0
    ans = 0
    while i<N:
        # i 부터 끝까지 최대값의 idx 찾기
        i_mx = i
        for j in range(i+1,N):
            if lst[i_mx]<lst[j]:
                i_mx = j
        # i~i_mx 까지의 최대값과의 차이 누적
        for j in range(i, i_mx):
            ans += lst[i_mx] - lst[j]
        i = i_mx + 1
    print(f'#{tc} {ans}')






# T = int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     buy_score = 0
#     bye_score = 0
#     cnt = 0
#     for idx in range(N):
#         buy = 0
#         if idx == N - 1:
#             bye_score += (cnt * arr[idx])
#         else:
#             for i in range(idx+1,N):
#                 if arr[idx] < arr[i]:
#                     buy = 1
#                     break
#             else:
#                 bye_score += (cnt * arr[idx])
#                 cnt = 0
#             if buy == 1:
#                 buy_score += arr[idx]
#                 cnt += 1
#                 buy = 0
#     ans = bye_score - buy_score
#     print(f'#{tc} {ans}')

