import os

import colorama

figure = {
    0: '  ',
    1: 'wc',
    2: 'bc'
}

board = [
    [0, 2, 0, 2, 0, 2, 0, 2],
    [2, 0, 2, 0, 2, 0, 2, 0],
    [0, 2, 0, 2, 0, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]

step_counter = 0


def show_board():
    print('   ', end='')
    for i in 'abcdefgh':
        print(i, end='  ')
    print()

    print('  -------------------------')

    counter = 8

    for i in range(len(board)):
        print(counter, end=' |')
        for j in range(len(board[i])):
            print(figure[board[i][j]], end='|')
        print(' ', end='')
        print(counter)
        counter -= 1
        print('  -------------------------')

    print('   ', end='')
    for i in 'abcdefgh':
        print(i, end='  ')
    print()


def move():
    print("выберите фигуру которой будите ходит:", end="\t")
    start_move = input()
    first_part_move = start_move[0]
    second_part_move = start_move[1]
    print(first_part_move)
    print(second_part_move)


def start_game():
    while True:
        if step_counter % 2 == 0:
            os.system('clear')
            show_board()
            print('Ход белых')
            move()
        else:
            print('Ход черных')


if __name__ == '__main__':
    start_game()
