import numpy as np


def color(col, i, j, DIM):

    if col == 'white':
        return 1
    if col == 'y':
        return i/DIM
    if col == 'x':
        return j/DIM
    if col == 'xy':
        return min((i + j) / (2*DIM), 1)
    if col == 'random':
        return max(min(np.random.normal(0.5, 0.25), 1), 0.1)

def ZEROS(DIM, col='x'):
    return np.zeros((DIM, DIM))

def RAND(DIM, col='x'):
    return np.random.choice([0, 1], DIM*DIM, p=[0.7, 0.3]).reshape(DIM, DIM)

def X(DIM, length=2, col='x'):
    board = np.zeros((DIM, DIM))
    board[(DIM-1)//2][(DIM-1)//2] = 1
    for x in range(length):
        board[(DIM-1)//2 + x][(DIM-1)//2 + x] = color(col, (DIM-1)//2 + x, (DIM-1)//2 + x, DIM)
        board[(DIM-1)//2 + x][(DIM-1)//2 - x] = color(col, (DIM-1)//2 + x, (DIM-1)//2 + x, DIM)
        board[(DIM-1)//2 - x][(DIM-1)//2 - x] = color(col, (DIM-1)//2 + x, (DIM-1)//2 + x, DIM)
        board[(DIM-1)//2 - x][(DIM-1)//2 + x] = color(col, (DIM-1)//2 + x, (DIM-1)//2 + x, DIM)
    return board


def ELBOW(DIM, col='x'):

    board = np.zeros((DIM,DIM))
    board[1][1] = 1
    board[1][2] = 1
    board[2][2] = 1
    return board


def RING(DIM, col='x'):
    board = np.zeros((DIM, DIM))
    return board
