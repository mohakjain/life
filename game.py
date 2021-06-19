import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import patterns
import random

DIM = 150
COL = random.choice(['y', 'x', 'xy'])
CMAP = random.choice(['magma', 'hot', 'inferno'])

def init(pattern):
    return pattern

def update(fnum, board, img):
    new_board = board.copy()
    for i in range(DIM):
        for j in range(DIM):
            neighbors = np.ceil(board[(i-1)%DIM][(j+1)%DIM]) + np.ceil(board[i][(j+1)%DIM]) + np.ceil(board[(i+1)%DIM][(j+1)%DIM]) + np.ceil(board[(i-1)%DIM][j]) + np.ceil(board[(i+1)%DIM][j]) + np.ceil(board[(i-1)%DIM][(j-1)%DIM]) + np.ceil(board[i][(j-1)%DIM]) + np.ceil(board[(i+1)%DIM][(j-1)%DIM])

            if board[i][j] == 0:
                if neighbors == 3:
                    new_board[i][j] = patterns.color(COL, i, j, DIM)
            elif neighbors < 2 or neighbors > 3:
                    new_board[i][j] = 0

    img.set_data(new_board)
    board[:] = new_board[:]
    return img

board = init(patterns.RAND(DIM))
# print("Color Scheme: " + COL, "| Size: " + str(DIM))

fig, ax = plt.subplots()
img = ax.imshow(board, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(board, img, ), frames=10, interval=50, save_count=50)
plt.axis('off')
img.set_cmap(CMAP)

# ani.save('test.mp4', fps=30)

plt.show()
