from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main():
    img_rgb = ft_load("animal.jpeg")
    if img_rgb is None:
        return
    
    sliced = img_rgb[0:400, 300:700, 0:1]
    print(f"The shape of image is: {sliced.shape}")
    print(sliced)

    if len(sliced.shape) == 2:
        display = sliced
    else:
        display = sliced[:, :, 0]
    display = np.rot90(display)
    print(f"New shape after Transpose: {display.shape}")
    print(display)
    
    plt.imshow(display, cmap="gray")
    plt.show()
    plt.close()


if __name__ == "__main__":
    main()