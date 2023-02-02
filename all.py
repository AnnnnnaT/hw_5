import random

sweets = int(input('Input number of sweets: \n'))
take = 0
player1 = 0
player2 = 0

def rules_start():
    print('На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\n'
        'За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.\n')
    starter()


def starter():
    
    x = random.randint(1,2)
    if x == 1:
        player1_turn()
    else:
        player2_turn()
            
def player1_turn():
    global sweets
    global take 
    global player1
    print(f'Your turn, player1! There are {sweets} now')
    take = int(input('How many you take? -> '))
    while take > 28 or take < 0 or take > sweets:
        take = int(input('You take too much. Try again: '))
    sweets -= take
    if sweets > 0:
        player2_turn()
    else:
        print('You won!')

def player2_turn():
    global sweets
    global take 
    global player2
    print(f'Your turn, player2! There are {sweets} now')
    take = int(input('How many you take? -> '))
    while take > 28 or take < 0 or take > sweets:
        take = int(input('You take too much. Try again: '))
    sweets -= take
    if sweets > 0:
        player1_turn()
    else:
        print('You won!')
