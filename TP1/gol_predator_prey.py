import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt


# import time
def init_grids(length=5, width=5):
    grid = DataFrame(np.random.randint(0, 3, (length + 2, width + 2)),
                     index=range(length + 2),
                     columns=range(width + 2))
    grid[0] = 0
    grid[width + 1] = 0
    grid[0: 1] = 0
    grid[length + 1: length + 2] = 0

    grid_lifespan = DataFrame(np.zeros((length + 2, width + 2), dtype=int),
                              index=range(length + 2),
                              columns=range(width + 2))
    grid_lifespan[0] = 0
    grid_lifespan[width + 1] = 0
    grid_lifespan[0: 1] = 0
    grid_lifespan[length + 1: length + 2] = 0

    for x in range(1, width + 1):
        for y in range(1, length + 1):
            if grid[x][y] == 1 or grid[x][y] == 2:
                grid_lifespan[x][y] = 1

    grid_fasting = DataFrame(np.zeros((length + 2, width + 2), dtype=int),
                             index=range(length + 2),
                             columns=range(width + 2))
    grid_fasting[0] = 0
    grid_fasting[width + 1] = 0
    grid_fasting[0: 1] = 0
    grid_fasting[length + 1: length + 2] = 0
    for x in range(1, width + 1):
        for y in range(1, length + 1):
            if grid[x][y] == 1 or grid[x][y] == 2:
                grid_fasting[x][y] = 1

    return grid, grid_lifespan, grid_fasting


def gol_predator_prey(length=10, width=10, gen=5, lifespan=3, fasting=2):
    grid, grid_lifespan, grid_fasting = init_grids(length, width)

    for i in range(gen):
        # to get an image of the grid
        fig, ax = plt.subplots()
        draw = grid[1:length + 1].drop([0, width + 1], axis=1)

        image = draw
        #grass: green, sheep: blue, wolf: red
        colors = {0: np.array([0, 255, 0]), 1: np.array([0, 0, 255]), 2: np.array([255, 0, 0])}
        image_3d = np.ndarray(shape=(image.shape[0], image.shape[1], 3), dtype=int)

        for j in range(1, image.shape[0] + 1):
            for k in range(1, image.shape[1] + 1):
                image_3d[j - 1][k - 1] = colors[image[j][k]]
        ax.imshow(image_3d)
        ax.set_title("Game of life: Prey/Predator Ecosystem")

        plt.show()

        next_grid = grid
        next_grid_lifespan = grid_lifespan

        next_grid_fasting = grid_fasting

        for x in range(1, width + 1):
            for y in range(1, length + 1):
                env_grass = ((1 if grid[x][y - 1] == 0 else 0) + (1 if grid[x - 1][y] == 0 else 0) +
                             (1 if grid[x + 1][y] == 0 else 0) + (1 if grid[x][y + 1] == 0 else 0))

                env_wolf = ((1 if grid[x][y - 1] == 2 else 0) + (1 if grid[x - 1][y] == 2 else 0) +
                            (1 if grid[x + 1][y] == 2 else 0) + (1 if grid[x][y + 1] == 2 else 0))
                env_sheep = ((1 if grid[x][y - 1] == 1 else 0) + (1 if grid[x - 1][y] == 1 else 0) +
                             (1 if grid[x + 1][y] == 1 else 0) + (1 if grid[x][y + 1] == 1 else 0))

                if grid[x][y] == 2 and env_wolf == 1 and env_sheep == 1:
                    next_grid[x][y] = 2
                    next_grid_lifespan[x][y] = grid_lifespan[x][y] + 1
                    next_grid_fasting[x][y] = grid_fasting[x][y] - 1
                    continue
                if grid[x][y] == 0 and env_wolf == 2 and env_sheep != 1:
                    next_grid[x][y] = 2
                    next_grid_fasting[x][y] = 1
                    next_grid_lifespan[x][y] = 1
                    continue
                if grid[x][y] == 0 and env_sheep == 2:
                    next_grid[x][y] = 1
                    next_grid_fasting[x][y] = 1
                    next_grid_lifespan[x][y] = 1
                    continue
                if grid[x][y] == 1 and env_sheep < 1 and env_grass >= 1:
                    next_grid[x][y] = 1
                    next_grid_lifespan[x][y] = grid_lifespan[x][y] + 1
                    next_grid_fasting[x][y] = grid_fasting[x][y] - env_grass
                    continue
                if grid[x][y] == 1 and env_wolf > 1:
                    next_grid[x][y] = 0
                    next_grid_lifespan[x][y] = 0
                    next_grid_fasting[x][y] = 0
                if grid[x][y] == 1:
                    next_grid[x][y] = 1
                    next_grid_lifespan[x][y] = grid_lifespan[x][y] + 1
                    next_grid_fasting[x][y] = grid_fasting[x][y] - 1
                    continue
                if grid[x][y] == 2:
                    next_grid[x][y] = 2
                    next_grid_lifespan[x][y] = grid_lifespan[x][y] + 1
                    next_grid_fasting[x][y] = grid_fasting[x][y] - 1
                    continue

        for x in range(1, width + 1):
            for y in range(1, length + 1):
                if next_grid[x][y] != 0 and (next_grid_fasting[x][y] > fasting+1 or next_grid_lifespan[x][y] > lifespan+1):
                    next_grid[x][y] = 0
                    next_grid_fasting[x][y] = 0
                    next_grid_lifespan[x][y] = 0

        grid = next_grid
        grid_fasting = next_grid_fasting
        grid_lifespan = next_grid_lifespan


if __name__ == '__main__':
    gol_predator_prey()
