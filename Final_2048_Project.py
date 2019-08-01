##########################################################################################

import random

def board(n):
    '''Creates an n*n matrix for the playing board'''
    main_board = []
    for i in range(n):
        main_board.append([])
        
    for i in main_board:
        for j in range(n):
            i.append(0)

    return(main_board)

def print_as_a_matrix(board):
    for row in board:
        print(row)

def generate(row):
    value_list = [2,2,2,2,4]
    ctr = 0
    while ctr < len(row):
        if row[ctr] == 0:
            row[ctr] = random.choice(value_list)
            break
        
        ctr += 1
        

def check_zero(row):
    '''Returns True if the row has zero in it for the generate function'''
    for element in row:
        if element == 0:
            return(True)
    return(False)
        
def generate_for_board(passedboard,direction):
    '''Generates a value for a random row in a matrix if the row has a zero'''
    board = passedboard[:]

    if direction is 'left' or direction is 'right':
        ctr = 0

        while ctr < len(board):
            rand_row_of_board = random.randint(0,len(board)-1)

            if check_zero(board[rand_row_of_board]):
                generate(board[rand_row_of_board])
                break

            ctr += 1
    elif direction is 'up':
        board = transpose(board)
        board = generate_for_board(board,'left')
        board = transpose(board)
        
    elif direction is 'down':
        board = transpose(board)
        board = generate_for_board(board,'right')
        board = transpose(board)
        
    elif direction is 'random':
        k = random.randint(0,4)
        if k == 1:
            board=generate_for_board(board,'right')
        elif k == 2:
            board=generate_for_board(board,'left')
        elif k == 3:
            board=generate_for_board(board,'up')
        elif k == 4:
            board = generate_for_board(board,'down')

    return(board)
            
##########################################################################################

'''Merges a single row of the matrix into desired '''
def merge(x):
    y = x[:]
    i = 0
    j = 1
    while j < len(y):
        if y[j] == 0:
            j += 1
            
        elif y[i] == 0 and y[j] != 0:
            y[i] = y[j]
            y[j] = 0
            j += 1
        elif y[i] == y[j]:
            y[i] = 2*y[j]
            y[j] = 0
            i += 1
            j += 1
        else:
            if (j-i) > 1:
                i += 1
                y[i] = y[j]
                y[j] = 0
                j += 1
            else:
                i += 1
                j += 1
    return(y)

##########################################################################################

def transpose(y):
    '''Transposes a given matrix y'''
    c = board(len(y))  #creates an empty matrix with equivalent size
    for i in range(len(y)):
        for j in range(len(y)):
            c[i][j] = y[j][i]
    return(c)

def reverse_row(z):
    '''Reverses the individual rows in a given matrix y'''
    y = z[:]
    ctr = 0
    while ctr < len(y):
        y[ctr].reverse()
        ctr += 1
    return(y)
    
def row_merge(z):
    '''Merges a given matrix to the left row-by-row'''
    c = board(len(z))  #creates an empty matrix with equivalent size
    ctr=0
    while ctr < len(z):
        c[ctr] = merge(z[ctr])
        ctr += 1
    return(c)

def column_merge(z):
    '''Merges a given matrix column-by-column'''
    c = board(len(z))  #creates an empty matrix with equivalent size
    transposed_matrix = transpose(z)
    ctr = 0
    while ctr < len(transposed_matrix):
        c[ctr] = merge(transposed_matrix[ctr])
        ctr += 1
    return(transpose(c))

def merge_matrix_direction(matrix,direction):
    '''Merges the given matrix in a specific direction'''
    if direction is 'up':
        return(column_merge(matrix))

    elif direction is 'left':
        return(row_merge(matrix))
    
    elif direction is 'down':
        transposed_matrix = transpose(matrix)

        reversed_transposed = reverse_row(transposed_matrix)

        merged_reversed_transposed = row_merge(reversed_transposed)

        reversed_merged = reverse_row(merged_reversed_transposed)

        return(transpose(reversed_merged)) 
    elif direction is 'right':
        reversed_rows = reverse_row(matrix)

        merged_rows = row_merge(reversed_rows)

        return(reverse_row(merged_rows))

##########################################################################################
def game_over_condition(matrix):
    '''Returns False if 2048 is in the matrix anywhere'''
    for row in matrix:
        if 2048 in row:
            return(False)
    return(True)

##########################################################################################

import os

def clear_screen():  #clears screen after every move for a fresher console
    os.system('cls' if os.name=='nt' else 'clear')
    
def game():
    game_board = board(int(input("How big do you want your board to be? ")))

    print_as_a_matrix(game_board)

    game_board = generate_for_board(game_board, 'random')

    game_board = generate_for_board(game_board, 'random')

    while game_over_condition(game_board):
        clear_screen()

        print_as_a_matrix(game_board)

        k = input("Use w/s/a/d to control board: ")
        if k == 's':
            game_board = merge_matrix_direction(game_board,'down')
            game_board = generate_for_board(game_board,'down')
        if k == 'w':
            game_board = merge_matrix_direction(game_board,'up')
            game_board = generate_for_board(game_board,'up')
        if k == 'a':
            game_board = merge_matrix_direction(game_board,'left')
            game_board = generate_for_board(game_board,'left')
        if k == 'd':
            game_board = merge_matrix_direction(game_board,'right')
            game_board = generate_for_board(game_board,'right')

        print_as_a_matrix(game_board)
    print("You Won!")
    input()
game()
