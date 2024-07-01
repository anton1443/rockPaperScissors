import random

game_elements = ['rock', 'paper', 'scissors']

player = str(input('Камень, ножница, бумага, раз-два-три (выберите "rock", "paper", "scissors"): '))
computer = random.choice(game_elements)
print('Компьютер выбрал: ', computer)
if player == computer:
    print('Победителя нет, вы выбрали одинаковые знаки')
elif player == 'rock':
    if computer == 'paper':
        print('Компьютер выиграл')
    elif computer == 'scissors':
        print('Игрок выиграл')
elif player == 'paper':
    if computer == 'rock':
        print('Игрок выиграл')
    elif computer == 'scissors':
        print('Компьютер выиграл')
elif player == 'scissors':
    if computer == 'rock':
        print('Компьютер выиграл')
    elif computer == 'paper':
        print('Игрок выиграл')
elif player not in game_elements:
    print('Игрок допустил ошибку при выборе знака. Запустите программу заново')