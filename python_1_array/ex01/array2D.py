import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
        Using numpy to get the shape of list and slicing list as same as python native method
    """
    if not isinstance(family, list):
        raise TypeError("slice_me necessite a list")
    if len(family) == 0:
        raise ValueError("List length cannot be zero")
    row_len = len(family[0])
    for row in family:
        if not isinstance(row, list):
            raise TypeError("Each row should be a list")
        if len(row) != row_len:
            raise ValueError("All rows must have same size.")

    temp = np.array(family)
    print(f"My shape is : {temp.shape}")
    if start < 0:
        raise ValueError("Start is smaller than zero!")
    if end < (0 - len(family)):
        raise ValueError("End is smaller than length!")
    res = temp[start:end]
    print(f"My new shape is : {res.shape}")
    return res.tolist()