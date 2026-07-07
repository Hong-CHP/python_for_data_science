import cv2


def ft_load(path: str) -> array:
    """
        Loading a image
    """
    img_bgr = cv2.imread(path)

    if img_bgr is None:
        raise ValueError("Please enter a validate image or path.")
    

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb
