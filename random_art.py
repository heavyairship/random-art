import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import numpy as np
from PIL import Image

MAX_X = 500
MAX_Y = 500
COLOR_WHITE = 255
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def random_x_y():
    def random_coord(max_dim):
        return int(random.random()*max_dim)
    return random_coord(MAX_X), random_coord(MAX_Y)

def random_width_height(x, y):
    factor = 4
    def random_dim(coord, max_dim):
        return min(max_dim, int(random.random()*(max_dim-coord)))
    return (random_dim(x, MAX_X)/factor, random_dim(y, MAX_Y)/factor)

def random_color():
    return tuple(random.random() for _ in range(3))

def random_filename():
    out = []
    length = 16
    for _ in range(length):
        out.append(ALPHABET[int(random.random()*len(ALPHABET))])
    return ''.join(out)

def random_art():
    img_array = np.full((MAX_X, MAX_Y, 3), COLOR_WHITE, dtype = np.uint8)
    image = Image.fromarray(img_array)

    # Create figure and axes
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(image)

    for i in range(50):
        # Create a Rectangle patch
        (x, y) = random_x_y()
        (width, height) = random_width_height(x, y)
        color = random_color()
        rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor=color, facecolor=color)
        print(f"(x, y, width, height, color) = ({x}, {y}, {width}, {height}, {color})")

        # Add the patch to the Axes
        ax.add_patch(rect)

    plt.axis('off')
    print(random_filename())
    plt.savefig(f"gallery/{random_filename()}.png")
    plt.clf()

for _ in range(10):
    random_art()