import os
from platform import mac_ver

player_row = 0
player_col = 0
cpu_row = 0
cpu_col = 0
board = [[0 for x in range(0,9)] for y in range(0,9)]
os.system('cls')
def show_board():
    os.system("cls")
    global player_row, player_col
    global cpu_row, cpu_col
    global board
    print("\n  1 2 3 4 5 6 7 8 9")
    for x in range(0,9):
        data = str(x+1)
        for y in range(0,9):
            if board[x][y] == 0:
                data += ' +'
            elif board[x][y] == 1:
                data += ' ▲'
            elif board[x][y] == 2:
                data += ' ■'
        print(data)

def player_round():
    global player_row, player_col
    global cpu_row, cpu_col
    global board
    player_row,player_col = int(input()),int(input())
    board[player_row-1][player_col-1] = 1

def is_player_win():
    global board
    global player_row
    global player_col
    count = 1
    for x in range(1,10):
        if board[player_row-1+x][player_col-1] == 1:
            count += 1
        if count < 5 and board[player_row-1+x][player_col-1] != 1 or player_row-1+x >= 8:
            break
        elif count >= 5:
            print('player win' )
    for x in range(1,10):
        if board[player_row-1-x][player_col-1] == 1:
            count += 1
        if count < 5 and board[player_row-1-x][player_col-1]  != 1 or player_row-1-x <= 0:
            break
        elif count >= 5:
            print('player win' )
    count = 1
    for x in range(1,10):
        if board[player_row-1][player_col-1+x] == 1:
            count += 1
        if count < 5 and board[player_row-1][player_col-1+x] != 1 or player_col-1+x >= 8:
          break
        elif count >= 5:
            print('player win' )
    for x in range(1,10):
        if board[player_row-1][player_col-1-x] == 1:
            count += 1
        if count < 5 and board[player_row-1][player_col-1-x] != 1 or player_col-1-x <= 0:
            break
        elif count >= 5:
            print('player win' )
    count = 1
    for x in range(1,10):
        if board[player_row-1-x][player_col-1-x] == 1:
            count += 1
        if count < 5 and board[player_row-1-x][player_col-1-x] != 1 or player_col-1-x <= 0 and player_row-1-x <= 0:
            break
        elif count >= 5:
            print('player win' )
    for x in range(1,10):
        if board[player_row-1+x][player_col-1+x] == 1:
            count += 1
        if count < 5 and board[player_row-1+x][player_col-1+x] != 1 or player_col-1+x >= 8 and player_row-1+x >= 8:
            break
        elif count >= 5:
            print('player win' )
    count = 1
    for x in range(1,10):
        if board[player_row-1+x][player_col-1-x] == 1:
            count += 1
        if count < 5 and board[player_row-1+x][player_col-1-x] != 1 or player_col-1-x <= 0 and player_row-1+x >= 8:
            break
        elif count >= 5:
            print('player win' )
    for x in range(1,10):
        if board[player_row-1-x][player_col-1+x] == 1:
            count += 1
        if count < 5 and board[player_row-1-x][player_col-1+x] != 1 or player_col-1-x <= 0 and player_row-1+x >= 8:
            break
        elif count >= 5:
            print('player win' )

def cpu_round():
    global board
    global cpu_row, cpu_col
    global player_row, player_col
    count = 1
    max_count = 1
    for x in range(1,9):
        if board[player_row-1-x][player_col-1] == 1:
            count += 1
        if count < 5 and board[player_row-1-x][player_col-1] != 1:
                if board[player_row-1-x][player_col-1] == 0:
                    cpu_row = player_row-1-x
                    cpu_col = player_col-1
                break
    for x in range(1,9):
        if board[player_row-1+x][player_col-1] == 1:
            count += 1
        if count < 5 and board[player_row-1+x][player_col-1] != 1:
                if board[player_row-1+x][player_col-1] == 0 and max_count < count:
                    cpu_col = player_col-1
                    cpu_row = player_row-1-x
                    max_count = count
                break
    count = 1
    for x in range(1,9):
        if board[player_row-1][player_col-1+x] == 1:
            count += 1
        if count < 5 and board[player_row-1][player_col-1+x] != 1:
                if board[player_row-1][player_col-1+x] == 0 and max_count < count:
                    cpu_col = player_col-1+x
                    cpu_row = player_row-1
                    max_count = count
                break
    for x in range(1,9):
        if board[player_row-1][player_col-1-x] == 1:
            count += 1
        if count < 5 and board[player_row-1][player_col-1-x] != 1:
            if board[player_row-1][player_col-1-x] == 0 and max_count < count:
                cpu_col = player_col-1-x
                cpu_row = player_row-1
                max_count = count
            break
    count = 1
    for x in range(1,9):
        if board[player_row-1+x][player_col-1-x] == 1:
            count += 1
        if count < 5 and board[player_row-1+x][player_col-1-x] != 1:
            if board[player_row-1+x][player_col-1-x] == 0 and max_count < count:
                cpu_col = player_col-1-x
                cpu_row = player_row-1+x
                max_count = count
            break
    for x in range(1,9):
        if board[player_row-1-x][player_col-1+x] == 1:
            count += 1
        if count < 5 and board[player_row-1-x][player_col-1+x] != 1:
            if board[player_row-1-x][player_col-1+x] == 0 and max_count < count:
                cpu_col = player_col-1+x
                cpu_row = player_row-1-x
                max_count = count
            break
    count = 1
    for x in range(1,9):
        if board[player_row-1-x][player_col-1-x] == 1:
            count += 1
        if count < 5 and board[player_row-1-x][player_col-1-x] != 1:
            if board[player_row-1-x][player_col-1-x] == 0 and max_count < count:
                cpu_col = player_col-1-x
                cpu_row = player_row-1-x
                max_count = count
            break
    for x in range(1,9):
        if board[player_row-1+x][player_col-1+x] == 1:
            count += 1
        if count < 5 and board[player_row-1+x][player_col-1+x] != 1:
            if board[player_row-1+x][player_col-1+x] == 0 and max_count < count:
                cpu_col = player_col-1+x
                cpu_row = player_row-1+x
                max_count = count
            break
    board[cpu_row][cpu_col] = 2


def is_cpu_win():
    global board
    global cpu_row, cpu_col
    count = 1
    for x in range(1, 10):
        if board[cpu_row-1+x][cpu_col - 1] == 2:
            count += 1
        if count < 5 and board[cpu_row-1+x][cpu_col - 1] != 2 or cpu_row-1+x >=8:
            break
        elif count >= 5:
            print('cpu win')
    for x in range(1,10):
        if board[cpu_row-1-x][cpu_col - 1] == 2:
            count += 1
        if count < 5 and board[cpu_row-1-x][cpu_col - 1] != 2 or cpu_row-1-x <= 0:
            break
        elif count >= 5:
            print('cpu win')
    count = 1
    for x in range(1, 10):
        if board[cpu_row - 1][cpu_col-1+x] == 2:
            count += 1
        if count < 5 and board[cpu_row - 1][cpu_col-1+x] != 2 or cpu_col-1+x >=8:
                break
        elif count >= 5:
                print('player win')
    for x in range(1,10):
        if board[cpu_row - 1][cpu_col-1-x] == 2:
            count += 1
        if count < 5 and board[cpu_row - 1][cpu_col-1-x] != 2 or cpu_col-1-x <= 0:
                break
        elif count >= 5:
                print('cpu win')
    count = 1
    for x in range(1, 10):
        if board[cpu_row - 1 - x][cpu_col - 1 - x] == 2:
            count += 1
        if count < 5 and board[cpu_row - 1 - x][cpu_col - 1 - x] != 2 or cpu_col - 1 - x <= 0 and cpu_row - 1 - x <= 0:
                break
        elif count >= 5:
                print('cpu win')
    for x in range(1, 10):
        if board[cpu_row - 1 + x][cpu_col - 1 + x] == 2:
            count += 1
        if count < 5 and board[cpu_row - 1 + x][cpu_col - 1 + x] != 2 or cpu_col - 1 + x >= 8 and cpu_row - 1 - x >= 8:
                break
        elif count >= 5:
                print('cpu win')
    count = 1
    for x in range(1, 10):
        if board[cpu_row - 1 + x][cpu_col - 1 - x] == 2:
            count += 1
        if count < 5 and board[cpu_row - 1 + x][cpu_col - 1 - x] != 2 or cpu_col - 1 - x <= 0 and cpu_row - 1 + x >= 8:
                break
        elif count >= 5:
                print('cpu win')
    for x in range(1, 10):
        if board[cpu_row - 1 - x][cpu_col - 1 + x] == 2:
            count += 1
        if count < 5 and board[cpu_row - 1 - x][cpu_col - 1 + x] != 2 or cpu_col - 1 + x >= 8 and cpu_row - 1 - x <= 0:
                break
        elif count >= 5:
                print('cpu win')



while True:
    show_board()
    player_round()
    if is_player_win():
        break
    cpu_round()
    if is_cpu_win():
        break
