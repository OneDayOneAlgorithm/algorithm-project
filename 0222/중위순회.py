def func(arr_lst,p):
    if p > N:
        return
    func(arr_lst,p*2)
    tree.append(arr_lst[p-1])
    func(arr_lst,p*2+1)


for tc in range(1,11):
    N = int(input())
    tree = []
    arr_lst = []
    for i in range(N):
        arr = list(input().split())
        arr_lst.append(arr[1])
    func(arr_lst,1)
    print(f"#{tc} {''.join(tree)}")