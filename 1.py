r = 6.5

a,b = map(int, input().split('x'))
half_dgl = ((a**2 + b**2)**0.5)/2

if half_dgl <= r:
    print('да')
else:
    print('нет')