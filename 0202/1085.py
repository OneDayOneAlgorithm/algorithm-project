x, y, w, h = map(int, input().split())
if w - x < x:
    x = w - x
if h - y < y:
    y = h - y
if x < y:
    print(x)
else:
    print(y)
