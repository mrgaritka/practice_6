cell1, cell2 = map(str, input().split('-'))

letter1 = ord(cell1[0])
num1 = int(cell1[1])
letter2 = ord(cell2[0])
num2 = int(cell2[1])

if (letter2-letter1==2 and num2-num1==1) or (letter2-letter1==1 and num2-num1==2):
    print('верно')
else:
    print('ошибка')