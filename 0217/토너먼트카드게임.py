def solve(left,right):
    if left == right:
        return left
    # 전체범위의 승자를 알기 위해서 절반의 승자들을 구해야 한다
    mid = (left + right) // 2
    winner1 = solve(left,mid)
    winner2 = solve(mid +1, right)
    # winner1과 winner2의 대결의 승자를 반환
    result = winner1
    if data[winner1] == 1:
        if data[winner2] == 2:
            result = winner2
    elif data[winner1] == 2:
        if data[winner2] == 3:
            result = winner2
    elif data[winner1] == 3:
        if data[winner2] == 1:
            result = winner2
    return result

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    data = [0] + list(map(int,input().split()))
    winner = solve(1,N)
    print(f'#{tc} {winner}')