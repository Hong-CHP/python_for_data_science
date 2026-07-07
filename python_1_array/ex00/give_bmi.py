import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
        Using numpy method calculating the bmi result
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight must have same length")
    
    h = np.array(height)
    w = np.array(weight)
    
    if np.any(h == 0):
        raise ValueError("Height cannot be zero")

    bmi = w / (h ** 2)

    return bmi.tolist()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
        Applying limit with bmi results
    """
    res = []
    for x in bmi:
        if x > limit:
            res.append(True)
        else:
            res.append(False)
    return res