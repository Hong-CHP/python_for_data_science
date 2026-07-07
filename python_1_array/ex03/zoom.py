from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    """
        Entrypoint of program
        1. slicing numpy array result to gray
        2. convert 3d array to 2d array to create a matplotlib table to display sliced image
    """
    img_rgb = ft_load("animal.jpeg")
    if img_rgb is None:
        return
    print(img_rgb)
    zoom = img_rgb[100:500, 200:600, 0:1]

    print(f"New shape after slicing: {zoom.shape}")
    print(zoom)

    if len(zoom.shape) == 2:
        display = zoom
    else:
        display = zoom[:,:,0]

    plt.imshow(display, cmap="gray")
    # plt.savefig("zoom.jpg")
    plt.show()
    plt.close()

if __name__ == "__main__":
    main()