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


def show_board():
    print('   ', end='')
    for i in 'ABCDEFGH':
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
    for i in 'ABCDEFGH':
        print(i, end='  ')
    print()


if __name__ == '__main__':
    show_board()
