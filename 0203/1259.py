
while True:
    non_pelind = False
    N = input()
    if N == str(0):
        break
    for idx in range(len(N)):
        if str(N[idx]) != str(N[-idx - 1]):
            non_pelind = True
    if non_pelind == True:
        print('no')
    else:
        print('yes')