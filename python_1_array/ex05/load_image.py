import cv2


def ft_load(path):
    """
        Loading a image
    """
    img_bgr = cv2.imread(path)

    if img_bgr is None:
        raise ValueError("The image not exist or is empty.")
    
    print(f"The shape of image is : {img_bgr.shape}")

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    print(img_rgb)

    return img_rgb
