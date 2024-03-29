hole_w, hole_l = map(int, input().split('x'))
brick_w, brick_l, brick_h = map(int, input().split('x'))

brick = [brick_w, brick_l, brick_h]
brick.remove(max(brick))

brick_dgnl = (brick[0]**2 + brick[1]**2)**0.5
hole_dgnl = (hole_w**2 + hole_l**2)**0.5

if hole_dgnl >= brick_dgnl:
    print('да')
else:
    print('нет')