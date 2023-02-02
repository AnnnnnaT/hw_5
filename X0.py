#поле
def board(elem):
    y0 = f"    x1    x2   x3  "
    y1 = f"y1  {elem['y1']['x1']}  |  {elem['y1']['x2']}  | {elem['y1']['x3']}  "
    y2 = "  -----+-----+-----"
    y3 = f"y2  {elem['y2']['x1']}  |  {elem['y2']['x2']}  | {elem['y2']['x3']}  "
    y4 = f"y3  {elem['y3']['x1']}  |  {elem['y3']['x2']}  | {elem['y3']['x3']}  "
    print(y0)
    print(y1)
    print(y2)
    print(y3)
    print(y2)
    print(y4)

#проверка введенных пользователем координат
def check(player, moves_):
    if len(player) == 4:
        if player[0].lower() == 'y' and player[2].lower() == 'x':
            if player[1] in '123' and player[-1] in '123':
                if moves_[player[:2]][player[-2:]] == ' ':
                    return True
                else:
                    print('Данная клетка уже занята.')
            else:
                print('Значения координат выходят за пределы поля')
        else:
            print('Введите координаты в формате y1x1')
    else:
        print('Введено недопустимое количество символов.')
    print('Попробуйте ещё раз')
    return False

#комбинации победителя
def wins_comb(moves_):
    if ((moves_['y1']['x1'] == moves_['y1']['x2'] == moves_['y1']['x3']
            or moves_['y1']['x1'] == moves_['y2']['x1'] == moves_['y3']['x1']
            or moves_['y1']['x1'] == moves_['y2']['x2'] == moves_['y3']['x3'])
            and moves_['y1']['x1'] != ' '):
        return moves_['y1']['x1']
    elif ((moves_['y2']['x1'] == moves_['y2']['x2'] == moves_['y2']['x3']
           or moves_['y1']['x2'] == moves_['y2']['x2'] == moves_['y3']['x2']
           or moves_['y1']['x3'] == moves_['y2']['x2'] == moves_['y3']['x1'])
          and moves_['y2']['x2'] != ' '):
        return moves_['y2']['x2']
    elif ((moves_['y3']['x1'] == moves_['y3']['x2'] == moves_['y3']['x3']
           or moves_['y1']['x3'] == moves_['y2']['x3'] == moves_['y3']['x3'])
          and moves_['y3']['x3'] != ' '):
        return moves_['y3']['x3']
    return False
#заполнение словаря символами
def move(symbol, moves_, player):
    print('\nТекущий ход y{}x{}:\n'.format(player[1], player[-1]))
    if player[1] == '1':
        if player[-1] == '1':
            moves_['y1']['x1'] = symbol
        elif player[-1] == '2':
            moves_['y1']['x2'] = symbol
        else:
            moves_['y1']['x3'] = symbol
    elif player[1] == '2':
        if player[-1] == '1':
            moves_['y2']['x1'] = symbol
        elif player[-1] == '2':
            moves_['y2']['x2'] = symbol
        else:
            moves_['y2']['x3'] = symbol
    else:
        if player[-1] == '1':
            moves_['y3']['x1'] = symbol
        elif player[-1] == '2':
            moves_['y3']['x2'] = symbol
        else:
            moves_['y3']['x3'] = symbol
    return moves_

#словарь, который будем заполнять
moves_ = {
    'y1': {'x1': ' ', 'x2': ' ', 'x3': ' '},
    'y2': {'x1': ' ', 'x2': ' ', 'x3': ' '},
    'y3': {'x1': ' ', 'x2': ' ', 'x3': ' '}
}

print('\nНачнем игру!')

count = 0
win = False
while not win and count < 9:
    player = input('Введите координаты хода(пример - y1x1): ')
    while not check(player, moves_):
        player = input('Введите координаты хода(пример - y1x1): ')
    count += 1

    if count % 2:
        symbol = 'X'
    else:
        symbol = 'O'

    moves_ = move(symbol, moves_, player)

    board(moves_)
    win = wins_comb(moves_)
if count == 9:
    print('Ничья!')
else:
    print('ПОБЕДА!')
