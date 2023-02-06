import os

import colorama

a = [
    ['  ', 'bc', '  ', 'bc', '  ', 'bc', '  ', 'bc'],
    ['bc', '  ', 'bc', '  ', 'bc', '  ', 'bc', '  '],
    ['  ', 'bc', '  ', 'bc', '  ', 'bc', '  ', 'bc'],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  '],
    ['wc', '  ', 'wc', '  ', 'wc', '  ', 'wc', '  '],
    ['  ', 'wc', '  ', 'wc', '  ', 'wc', '  ', 'wc'],
    ['wc', '  ', 'wc', '  ', 'wc', '  ', 'wc', '  ']
]


def show_board():
    print('   ', end='')
    for i in 'ABCDEFGH':
        print(i, end='  ')
    print()

    print('  -------------------------')
    counter = 8
    for i in range(len(a)):
        print(counter, end=' |')
        for j in range(len(a[i])):
            print(a[i][j], end='|')
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
