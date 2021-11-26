import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt


def conway_gol(length=10, width=10, gen=5):
    grid = DataFrame(np.random.randint(0, 2, (length + 2, width + 2)),
                     index=range(length + 2),
                     columns=range(width + 2))
    grid[0] = 0
    grid[width + 1] = 0
    grid[0: 1] = 0
    grid[length + 1: length + 2] = 0

    for i in range(gen):
        # to get an image of the grid
        fig, ax = plt.subplots()
        draw = grid[1:length + 1].drop([0, width + 1], axis=1)

        image = draw
        colors = {0: np.array([0, 0, 255]), 1: np.array([255, 0, 0])}
        image_3d = np.ndarray(shape=(image.shape[0], image.shape[1], 3), dtype=int)

        for j in range(1, image.shape[0] + 1):
            for k in range(1, image.shape[1] + 1):
                image_3d[j - 1][k - 1] = colors[image[j][k]]
        ax.imshow(image_3d)
        ax.set_title("Conway's Game of Life.")

        plt.show()

        next_grid = grid

        for x in range(1, width + 1):
            for y in range(1, length + 1):
                env = (grid[x - 1][y - 1] + grid[x][y - 1] +
                       grid[x + 1][y - 1] + grid[x - 1][y] +
                       grid[x + 1][y] + grid[x - 1][y + 1] +
                       grid[x][y + 1] + grid[x + 1][y + 1])

                if (not grid[x][y] and env == 3):
                    next_grid[x][y] = 1
                if (grid[x][y] and env in (2, 3)):
                    next_grid[x][y] = 1

            grid = next_grid


if __name__ == '__main__':
    conway_gol()
