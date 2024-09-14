import matplotlib.pyplot as plt

RESOLUTION = 256

color_matrix = [[[0,0,0] for _ in range(RESOLUTION)] for _ in range(RESOLUTION)]

for iR, r in enumerate(color_matrix):
    for iC, c in enumerate(r):
        color_matrix[iR][iC] = [iR, iC, iC]

plt.imshow(color_matrix)
plt.axis('off')
plt.show()