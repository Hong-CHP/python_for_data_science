import cv2


def ft_load(path: str) -> array:
    """
        Using opencv lib to read image in BGR format returning an numpy array;
        using opencv method to covert BGR to RGB color
    """
    img_bgr = cv2.imread(path)

    if img_bgr is None:
        raise ValueError("Please enter a validate image or path.")

    print(f"The shape of image is : {img_bgr.shape}")
    
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb.tolist()
