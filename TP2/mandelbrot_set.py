import matplotlib.pyplot as plt
import numpy as np


def input_number(message):
    while True:
        try:
            user_input = int(input(message))
        except ValueError:
            print("Not an integer! Try again.")
            continue
        else:
            return user_input


def mandelbrot_set(max_iter):
    num_pts = 300
    # plan (x;y)
    x = np.linspace(-2, 1, 2 * num_pts)
    y = np.linspace(-1, 1, num_pts)

    # les coordonnees du plan
    # c = z + iy
    c = x[:, None] + 1J * y
    # initial value is always zero
    z = np.zeros_like(c)

    exit_times = max_iter * np.ones(c.shape, np.int32)
    mask = exit_times > 0

    for k in range(max_iter):
        z[mask] = z[mask] * z[mask] + c[mask]
        mask, old_mask = abs(z) < 2, mask
        # use XOR to detect the area which has changed
        exit_times[mask ^ old_mask] = k

    plt.imshow(exit_times.T,
               cmap=plt.cm.prism,
               extent=(x.min(), x.max(), y.min(), y.max()))
    plt.show()


if __name__ == "__main__":
    mandelbrot_set(input_number("Entrez le rang pour fixer la qualité du rendu final: "))
