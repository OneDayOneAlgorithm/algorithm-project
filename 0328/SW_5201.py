T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # M은 트럭
    wi = list(map(int, input().split()))    # wi는 화물
    ti = list(map(int, input().split()))    # ti는 트럭
    wi.sort(reverse=True)   # 내림차순 정렬
    ti.sort(reverse=True)
    sum_v = 0               # 트럭이 싣을 수 있는 화물의 무게
    for i in range(M):      # 트럭의 갯수만큼 순환하고
        for j in range(len(wi)):    # 화물의 갯수만큼 순환하여
            if ti[i] >= wi[j]:  # 트럭이 화물을 싣을 수 있으면
                sum_v += wi.pop(j)  # 화물을 싣고 그 화물은 없앤다.
                break   # 그리고 다음 트럭을 순환한다.
        else:       # 싣을 수 있는게 없으면 그 뒤의 트럭도 마찬가지 이므로
            break   # 트럭 순환 종료
    print(f'#{tc} {sum_v}')
