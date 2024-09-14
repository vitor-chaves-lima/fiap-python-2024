import matplotlib.pyplot as plt

WHITE_COLOR = [255, 255,255]
BLACK_COLOR = [0, 0, 0]

chess_matrix = [[[255*((i+j)%2),255*((i+j)%2),255*((i+j)%2)] for i in range(8)] for j in range(8)]

plt.imshow(chess_matrix)
plt.axis('off')
plt.show()