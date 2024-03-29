cell = input()
letter = ord(cell[0])
num = int(cell[1])

if num%2 == letter%2:
    print('черный')
else:
    print('белый')