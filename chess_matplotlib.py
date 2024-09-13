import matplotlib.pyplot as plt

WHITE_COLOR = [255, 255,255]
BLACK_COLOR = [0, 0, 0]

chess_matrix = [[[None,None,None] for _ in range(8)] for _ in range(8)]

for iR, r in enumerate(chess_matrix):
    for iC, _ in enumerate(r):
        if iR % 2 == 0:
            if iC % 2 == 0:
                chess_matrix[iR][iC] = WHITE_COLOR
            else:
                chess_matrix[iR][iC] = BLACK_COLOR
        else:
            if iC % 2 == 0:
                chess_matrix[iR][iC] = BLACK_COLOR
            else:
                chess_matrix[iR][iC] = WHITE_COLOR

plt.imshow(chess_matrix)
plt.axis('off')
plt.show()