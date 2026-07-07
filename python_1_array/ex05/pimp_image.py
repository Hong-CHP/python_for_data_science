import matplotlib.pyplot as plt

def ft_invert(array) -> array:
    """
    Inverts the color of the image received.
    """
    #your code here
    invert_img = array.copy()
    
    invert_img = 255 - invert_img
    plt.imshow(invert_img)
    plt.axis('off')
    # plt.savefig("invert.jpg")
    plt.show()
    plt.close()
        

def ft_red(array) -> array:
    """
    Get the red color of the image received.
    """
    #your code here
    red_img = array.copy()

    red_img[:, :, 1] = 0
    red_img[:, :, 2] = 0
    plt.imshow(red_img)
    plt.axis('off')
    # plt.savefig("red.jpg")
    plt.show()
    plt.close()
    

def ft_green(array) -> array:
    """
    Get the green color of the image received.
    """
    #your code here
    green_img = array.copy()

    green_img[:, :, 0] = 0
    green_img[:, :, 2] = 0
    plt.imshow(green_img)
    plt.axis('off')
    # plt.savefig("green.jpg")
    plt.show()
    plt.close()


def ft_blue(array) -> array:
    """
    Get the blue color of the image received.
    """
    #your code here
    blue_img = array.copy()

    blue_img[:, :, 0] = 0
    blue_img[:, :, 1] = 0
    plt.imshow(blue_img)
    plt.axis('off')
    # plt.savefig("blue.jpg")
    plt.show()
    plt.close()


def ft_grey(array) -> array:
    """
    Get the gray color of the image received.
    """
    #your code here
    gray_img = array.copy()

    r_channel = gray_img[:, :, 0] / 1
    gray_img[:, :, 0] = r_channel
    gray_img[:, :, 1] = r_channel
    gray_img[:, :, 2] = r_channel
    plt.imshow(gray_img)
    plt.axis('off')
    # plt.savefig("gray.jpg")
    plt.show()
    plt.close()